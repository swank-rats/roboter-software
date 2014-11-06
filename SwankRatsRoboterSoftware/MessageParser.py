__author__ = 'Johannes'
import json
from Robot import  Robot
from pprint import pprint

class MessageParser:

    """Parses JSON messages an performs the according SwankRatsRobot action"""

    def __init__(self):
        self.id = 123
        self.robot = Robot()

    def parse(self, jsonString):
        data = json.load(jsonString)
        if( data["to"] == "robot"):
            if(data["cmd"].lower() == "left"):
                self.robot.driveLeft()
            if(data["cmd"].lower() == "right"):
                self.robot.driveStraight()
            if(data["cmd"].lower() == "straight"):
                self.robot.driveStraight()
        if(data["to"] == "print"):
            pprint(data)
