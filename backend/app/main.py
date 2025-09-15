from fastapi import FastAPI

app = FastAPI(title="MehrKaan API")

@app.get("/ping")
def ping():
    return {"message": "pong 🪷"}
