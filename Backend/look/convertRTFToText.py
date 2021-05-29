from striprtf import striprtf


def convertRTFToText(file_path):
	with open(file_path, 'r') as file:
		data = file.read().replace('\n', '')
		return striprtf.rtf_to_text(data)
