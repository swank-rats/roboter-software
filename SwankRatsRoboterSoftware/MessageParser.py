__author__ = 'Johannes'
import json

from Robot import Robot
import StateClasses


class MessageParser:
    """Parses JSON messages an performs the according SwankRatsRobot action"""

    def __init__(self):
        self.id = 123
        self.robot = Robot()
        self.currentState = StateClasses.Stop()

    def parse(self, jsonString):
        data = json.loads(jsonString)
        if data["to"] == "robot":
            if data["params"]["started"]:
                self.currentState = self.currentState.press(data["cmd"])
            if not data["params"]["started"]:
                self.currentState = self.currentState.release(data["cmd"])

            print self.currentState.__class__.__name__
            self.robot.set(self.currentState.getLeft(), self.currentState.getRight())

        json.dumps(data)
