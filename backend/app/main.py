from fastapi import FastAPI
from app.db import engine, Base
from app.routes import users

app = FastAPI(title="MehrKaan API")

# create tables if you want local quick start (if you're using Alembic, you can skip this)
Base.metadata.create_all(bind=engine)

@app.get("/ping")
def ping():
    return {"message": "pong 🪷"}

app.include_router(users.router, prefix="/users", tags=["Users"])
