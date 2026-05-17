from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import mlflow
import re
from bs4 import BeautifulSoup

app = FastAPI(title="Rakuten Product Classification API")

# --------------------------------------------------
# ✅ MLflow config
# --------------------------------------------------
mlflow.set_tracking_uri("file:///C:/Users/user/Rakuten-Challenge/mlruns")

model = mlflow.pyfunc.load_model("models:/rakuten_model/Production")

# --------------------------------------------------
# ✅ DATA MODEL
# --------------------------------------------------
class Product(BaseModel):
    designation: str
    description: str | None = ""

# --------------------------------------------------
# ✅ PREPROCESSING
# --------------------------------------------------
def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = text.lower()
    text = re.sub(r"[^a-zàâçéèêëîïôûùüÿñæœ0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# --------------------------------------------------
# ✅ ROUTES
# --------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(product: Product):
    text = clean_text(product.designation + " " + product.description)

    prediction = model.predict([text])[0]

    return {"prediction": int(prediction)}
