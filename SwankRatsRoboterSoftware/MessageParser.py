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
            self.execute(data["cmd"], data["params"]["started"])
        elif data["to"] == "server" and data["cmd"] == "stop":
            self.currentState = StateClasses.Stop()

        self.robot.set(self.currentState.getLeft(), self.currentState.getRight())
        json.dumps(data)

    def execute(self, key, pressed):
        if pressed:
            self.currentState = self.currentState.press(key)
        else:
            self.currentState = self.currentState.release(key)
