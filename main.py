from fastapi import FastAPI
from app.endpoints import robot_control

app = FastAPI()

app.include_router(robot_control.router, prefix="/robot", tags=["robot control"])

@app.get("/")
def read_root():
    return {"message": "Robot Control API"}
