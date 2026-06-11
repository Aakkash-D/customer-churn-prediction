from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict whether a customer will churn",
    version="1.0"
)

# Load model once
model = joblib.load("customer_churn_model.joblib")


# Input schema
class CustomerInput(BaseModel):
    tenure_months: int
    monthly_charges: float
    support_calls: int
    contract: str
    internet_service: str
    payment_method: str
    senior_citizen: int


# Prediction endpoint
@app.post("/predict")
def predict(data: CustomerInput):

    # Convert input to DataFrame
    input_df = pd.DataFrame([data.model_dump()])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Get probability
    probability = model.predict_proba(input_df)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": round(float(probability), 4)
    }