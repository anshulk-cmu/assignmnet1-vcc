from fastapi import FastAPI
import requests

app = FastAPI()

VM2_URL = "http://10.0.2.4:8002"

@app.get("/")
def home():
    return {"message": "API Gateway (VM1)"}

@app.post("/ping")
def ping(data: dict):
    response = requests.post(f"{VM2_URL}/validate", json=data)
    return response.json()
