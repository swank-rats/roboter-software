__author__ = 'Johannes'
# import Adafruit_BBIO.GPIO as GPIO

import DMCC
import time
import RobotConfig
from thread import start_new_thread

class Robot:

    def __init__(self):
        self.rightMax = RobotConfig.Config.getfloat('robot', 'rightMax')
        self.leftMax = RobotConfig.Config.getfloat('robot', 'leftMax')
        self.rightMax = self.rightMax / 100.0
        self.leftMax = self.leftMax / 100.0

    def setLeftMotor(self, percent):
        if(percent == 0):
            DMCC.setMotor(0, 1, 0)
        else:
            start_new_thread(setMotor, (10,percent,5,"left",self.leftMax,0.01))

    def setRightMotor(self, percent):
        if(percent == 0):
            DMCC.setMotor(0, 2, 0)
        else:
            start_new_thread(setMotor, (10,percent,5,"right",self.rightMax,0.01))

def setMotor(start, stop, step, motor, max, pause):
    while start <= stop:
        start += step
        time.sleep(pause)
        print(start)
        try:
            if motor == "left":
                DMCC.setMotor(0, 1, int(start * 100 * max))
            if motor == "right":
                DMCC.setMotor(0, 2, int(start * 100 * max))
        except:
            print "Error setting " + motor + " motor, trying again"

