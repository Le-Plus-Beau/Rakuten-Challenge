from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import mlflow
import re
import pandas as pd
from bs4 import BeautifulSoup
from fastapi import HTTPException

app = FastAPI(title="Rakuten Product Classification API")

mlflow.set_tracking_uri("file:///C:/Users/user/Rakuten-Challenge/mlruns")
model = mlflow.pyfunc.load_model("models:/rakuten_model/Production")

class Product(BaseModel):
    designation: str
    description: str | None = ""

def clean_text(text):
    # ✅ force conversion systématique
    if text is None:
        text = ""
    text = str(text)  # <-- clé : int -> "123"

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
    try:
        print("DEBUG types:", type(product.designation), type(product.description))
        raw_text = product.designation + " " + (product.description or "")
        text = clean_text(raw_text)

        prediction = model.predict([text])[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {str(e)}")

