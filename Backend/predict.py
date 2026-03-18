import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("../model/model.pkl", "rb"))
scaler = pickle.load(open("../model/scaler.pkl", "rb"))

def predict_output(data):

    # Convert input into numpy array
    data = np.array(data).reshape(1, -1)

    # Scale the input
    data = scaler.transform(data)

    # Predict using model
    prediction = model.predict(data)

    return float(prediction[0])