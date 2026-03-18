import os
import pickle
import numpy as np

# -------------------------------
# Load Model (CORRECT PATH)
# -------------------------------
current_dir = os.path.dirname(__file__)

# Model is in root folder (same level as Backend)
model_path = os.path.abspath(
    os.path.join(current_dir, "..", "model", "model.pkl")
)

# Check if file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)


# -------------------------------
# Prediction Function
# -------------------------------
def predict_output(input_data: dict):
    try:
        # If frontend sends {"data": [...]}
        if "data" in input_data:
            features = input_data["data"]
        else:
            features = list(input_data.values())

        final_input = np.array(features).reshape(1, -1)

        prediction = model.predict(final_input)

        return {
            "prediction": prediction[0]
        }

    except Exception as e:
        return {
            "error": str(e)
        }