from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Customer Churn Prediction API")

model = joblib.load("models/churn_model.pkl")

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def read_root():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict(data: CustomerData):
    input_df = pd.DataFrame([data.model_dump()])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df).max()

    return {
        "prediction": prediction,
        "probability": float(probability)
    }