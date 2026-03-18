import os
import pickle
import numpy as np

# Get current file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct paths
model_path = os.path.join(BASE_DIR, "..", "model", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "..", "model", "scaler.pkl")

# Load model and scaler
model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))

def predict_output(data):
    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)
    prediction = model.predict(data)
    return float(prediction[0])