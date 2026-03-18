import os
import pickle
import numpy as np

# Get base path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model
model_path = os.path.join(BASE_DIR, "..", "Model", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "..", "Model", "scaler.pkl")

model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))

def predict_output(data):
    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)
    prediction = model.predict(data)
    return float(prediction[0])