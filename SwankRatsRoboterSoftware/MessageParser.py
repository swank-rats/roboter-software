__author__ = 'Johannes'
import json
from Robot import  Robot

class MessageParser:

    """Parses JSON messages an performs the according SwankRatsRobot action"""

    def __init__(self):
        self.id = 123
        self.robot = Robot()

    def parse(self, jsonString):
        try:
            data = json.loads(jsonString)
            if( data["to"] == "robot"):
                if(data["cmd"].lower() == "left"):
                    self.robot.driveLeft()
                if(data["cmd"].lower() == "right"):
                    self.robot.driveStraight()
                if(data["cmd"].lower() == "straight"):
                    self.robot.driveStraight()
            if(data["to"] == "print"):
                 json.dumps(data)
            json.dumps(data)
        except:
            print "Oops!  That was no valid json.  Try again..."