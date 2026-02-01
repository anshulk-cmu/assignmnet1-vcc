from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Greeter Service (VM3)"}

@app.post("/greet")
def greet(data: dict):
    name = data.get("name", "Guest")
    
    timenow = datetime.now().strftime("%H:%M:%S")
    datenow = datetime.now().strftime("%Y-%m-%d")
    
    output = f"""
==============================
           OUTPUT
==============================

Name: {name}
Date: {datenow}
Time: {timenow}

------------------------------

Path : VM1 to VM2 to VM3

------------------------------

Message: Hello {name}, Welcome to VCC!

------------------------------

Status : Success!!!
==============================
"""
    return {"output": output}
