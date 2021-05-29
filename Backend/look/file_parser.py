import io
import mimetypes
import os
import uuid
import falcon
import json
import numpy as np

from look.convertDocxToText import convertDocxToText
from look.convertPDFToText import convertPDFToText
from look.convertRTFToText import convertRTFToText


class FileParser(object):

    def __init__(self, file_store, nlp):
        self._storage_path = './temp'
        self._file_store = file_store
        self.nlp = nlp

    def on_post(self, req, resp):

        secure_name = ''
        entity_list = []
        form = req.get_media()
        for part in form:
            print(part.content_type)
            file_path, secure_name = self.saveFileToTemp(part)

            if part.content_type == 'application/pdf':
                # convert the PDF file To text
                parsed_text = convertPDFToText(file_path)

            elif part.content_type == 'application/rtf':
                # convert the RTF file To text
                parsed_text = convertRTFToText(file_path)

            elif part.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                # convert the Docx file to text
                parsed_text = convertDocxToText(file_path)
            else:
                resp.status = falcon.HTTP_415
                resp.media = json.dumps("Filetype not supported")
                return
            os.remove(os.path.join(self._storage_path, secure_name))
            entity_list.append(
                {
                    "file_name": part.secure_filename,
                    "parsed_data":  parsed_text,
                    "extracted_entites": self.nlp(parsed_text)
                }
            )

        # prepare the response data
        resp.media = json.dumps(entity_list, cls=NpEncoder)
        resp.status = falcon.HTTP_200

    def saveFileToTemp(self, part):
        # save the file in temp
        secure_name = self._file_store.save(part, part.content_type)
        file_path = os.path.join(self._storage_path, secure_name)
        return file_path, secure_name


class FileStore:
    _CHUNK_SIZE_BYTES = 4096

    # Note the use of dependency injection for standard library
    # methods. We'll use these later to avoid monkey-patching.
    def __init__(self, storage_path, uuidgen=uuid.uuid4, fopen=io.open):
        self._storage_path = storage_path
        self._uuidgen = uuidgen
        self._fopen = fopen

    def save(self, file_stream, file_content_type):
        ext = mimetypes.guess_extension(file_content_type)
        name = '{uuid}{ext}'.format(uuid=self._uuidgen(), ext=ext)
        file_path = os.path.join(self._storage_path, name)

        with open(file_path, 'wb') as dest:
            file_stream.stream.pipe(dest)

        return name


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)
