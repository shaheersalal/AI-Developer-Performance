from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('AI_Developer_Performance.joblib')

class DeveloperMetrics(BaseModel):
    Lines_of_Code: int
    AI_Usage_Hours: int
    Cognitive_Load: int
    Task_Duration_Hours: float
    Errors: float

@app.post("/predict")  
async def predict(metrics: DeveloperMetrics):
    input_df = pd.DataFrame([metrics.dict()])
    return {"prediction": (model.predict(input_df)[0])}