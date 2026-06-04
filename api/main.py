from fastapi import FastAPI

app = FastAPI()
data = []

@app.get("/")
def home():
    return {"msg": "running"}

@app.get("/metrics")
def metrics():
    return data
