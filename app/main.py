from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import mlflow
import re
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


import traceback

@app.post("/predict")
def predict(product: Product):
    try:
        designation = product.designation
        description = product.description or ""
        raw_text = designation + " " + description
        text = clean_text(raw_text)

        print("DEBUG raw_text type:", type(raw_text))
        print("DEBUG cleaned text type:", type(text))
        print("DEBUG cleaned text sample:", text[:80])

        X_in = pd.DataFrame({"text": [text]})
        prediction = model.predict(X_in)[0]
        return {"prediction": int(prediction)}

    except Exception as e:
        tb = traceback.format_exc()
        print("=== ERROR TRACEBACK ===")
        print(tb)
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {str(e)}")


