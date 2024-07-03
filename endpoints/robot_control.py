from fastapi import APIRouter, HTTPException
from app.models.robot_control_model.py import RobotControlModel

router = APIRouter()
robot = RobotControlModel()

@router.post("/forward")
def move_forward():
    return {"state": robot.move_forward()}

@router.post("/backward")
def move_backward():
    return {"state": robot.move_backward()}

@router.post("/left")
def turn_left():
    return {"state": robot.turn_left()}

@router.post("/right")
def turn_right():
    return {"state": robot.turn_right()}

@router.post("/stop")
def stop():
    return {"state": robot.stop()}
