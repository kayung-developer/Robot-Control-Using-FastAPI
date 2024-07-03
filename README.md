# FastAPI Robot Control

This project provides a FastAPI endpoint interface for controlling a robot. The API supports basic commands such as moving forward, moving backward, turning left, turning right, and stopping.

## Features

- **FastAPI Integration**: Easily create API endpoints using FastAPI.
- **Robot Control**: Control a robot's movement via RESTful API commands.
- **Extensible and Modular**: Designed to be easily extendable for other types of robot commands and functionalities.

## Project Structure

- `app/main.py`: Entry point for the FastAPI application.
- `app/models/robot_control_model.py`: Contains the `RobotControlModel` class for robot control logic.
- `app/endpoints/robot_control.py`: Defines the endpoints for robot control commands.
- `app/schemas/robot_control.py`: Defines request and response schemas (if needed).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/FastApi-Robot-Control.git

```bash
cd FastApi-Robot-Control


```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```bash
pip install -r requirements.txt



## **Usage**

1. Run the FastAPI application:

```bash
uvicorn app.main:app --reload

2. Go to http://127.0.0.1:8000/docs to access the API documentation and test the endpoints.
