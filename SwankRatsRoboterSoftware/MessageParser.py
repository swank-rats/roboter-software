__author__ = 'Johannes'
import json
from Robot import  Robot
import StateClasses

class MessageParser:

    """Parses JSON messages an performs the according SwankRatsRobot action"""

    def __init__(self):
        self.id = 123
        self.robot = Robot()
        self.currentState = StateClasses.Stop()

    def parse(self, jsonString):
        try:
            data = json.loads(jsonString)
            if( data["to"] == "robot"):
                if(data["params"]["started"] == True):
                    self.currentState = self.currentState.press(data["cmd"])
                if(data["params"]["started"] == False):
                    self.currentState = self.currentState.release(data["cmd"])

                self.robot.setLeftMotor(self.currentState.getLeft())
                self.robot.setRightMotor(self.currentState.getRight())

            if(data["to"] == "print"):
                 json.dumps(data)

            json.dumps(data)
        except:
            print "Oops!  That was no valid json.  Try again..."