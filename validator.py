from fastapi import FastAPI
import requests

app = FastAPI()

VM3_URL = "http://10.0.2.5:8003"

@app.get("/")
def home():
    return {"message": "Validator Service (VM2)"}

@app.post("/validate")
def validate(data: dict):
    name = data.get("name", "")
    
    if not name or name.strip() == "":
        return {
            "output": "\n==========ERROR==========\n"
                      " Validation Failed ! \n"
                      " Reason: Name cannot be empty \n"
                      "=========================\n"
        }
    
    response = requests.post(f"{VM3_URL}/greet", json=data)
    return response.json()
