class RobotControlModel:
    def __init__(self):
        self.state = "stopped"

    def move_forward(self):
        self.state = "moving forward"
        return self.state

    def move_backward(self):
        self.state = "moving backward"
        return self.state

    def turn_left(self):
        self.state = "turning left"
        return self.state

    def turn_right(self):
        self.state = "turning right"
        return self.state

    def stop(self):
        self.state = "stopped"
        return self.state
