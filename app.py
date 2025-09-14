from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model and feature list
model, feature_names = joblib.load("pm25_model.pkl")

@app.post("/predict")
def predict(data: dict):
    # Convert input JSON → DataFrame
    df = pd.DataFrame([data])

    # Add missing features with default value (e.g., 0)
    for feature in feature_names:
        if feature not in df.columns:
            df[feature] = 0  # you can change 0 to mean value if you prefer

    # Reorder columns to match training
    df = df[feature_names]

    # Make prediction
    pred = model.predict(df)[0]
    return {"prediction": float(pred)}
