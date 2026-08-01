from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class Customer(BaseModel):
    Age: int
    Subscription_Type: str
    Contract_Length: str
    Usage_Frequency: int
    Total_Spend: float

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}

@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame([{
        "Age": customer.Age,
        "Subscription Type": customer.Subscription_Type,
        "Contract Length": customer.Contract_Length,
        "Usage Frequency": customer.Usage_Frequency,
        "Total Spend": customer.Total_Spend
    }])

    prediction = model.predict(data)[0]

    return {
        "prediction": int(prediction)
    }