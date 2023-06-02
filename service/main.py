from fastapi import FastAPI
from recosys.models.serialize import load

app = FastAPI()
DATA = {}


@app.on_event("startup")
def load_model():
    DATA["load"] = load()


@app.get("/")
def read_healthcheck():
    return {"status": "Green", "version": "0.0.1"}


@app.post("/predict")
def predict(user_id="123", course_id="333"):
    return {
        "user_id": user_id,
        "course_id": course_id,
        "res": DATA["load"].print_flower(),
    }
