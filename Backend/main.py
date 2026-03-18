from fastapi import FastAPI
from predict import predict_output

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Machine Output Prediction API Running"}

@app.post("/predict")
def predict(data: list):

    result = predict_output(data)

    return {"Predicted Parts Per Hour": result}