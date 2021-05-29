import falcon
from sqlalchemy import create_engine
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

from .file_parser import FileParser, FileStore

# Initiating the mysql server
engine = create_engine("mysql+pymysql://root@localhost/camembert_ner_islaib")

conn = engine.connect()

# starting Server
print("[INFO] Starting server...")
app = application = falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='localhost', allow_credentials='*'))

# Load and initialize the transformer model
print("[INFO] Loading Tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
print("[INFO] Tokenizer loaded", tokenizer.name_or_path)
print("[INFO] Loading Model...")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
print("[INFO] Model loaded", model.name_or_path)

nlp = pipeline('ner', model=model, tokenizer=tokenizer, grouped_entities=True)

fileStore = FileStore('temp/')
fileParser = FileParser(fileStore, nlp)

app.add_route('/fileParser', fileParser)

print("[INFO] Server Running")

