from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import re
from bs4 import BeautifulSoup
from pathlib import Path

app = FastAPI()

# chemins robustes
try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    BASE_DIR = Path.cwd()

ROOT_DIR = BASE_DIR.parent

model_path = ROOT_DIR / "models" / "Models" / "model.joblib"
vectorizer_path = ROOT_DIR / "models" / "Models" / "vectorizer.joblib"

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

class Product(BaseModel):
    designation: str
    description: str

def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = text.lower()
    text = re.sub(r"[^a-zàâçéèêëîïôûùüÿñæœ0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(product: Product):
    text = clean_text(product.designation + " " + product.description)
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    return {"prediction": int(prediction)}
