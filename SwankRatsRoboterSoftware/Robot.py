__author__ = 'Johannes'
# import Adafruit_BBIO.GPIO as GPIO

import DMCC
import time
import RobotConfig

class Robot:

    def __init__(self):
        self.rightMax = RobotConfig.Config.getfloat('robot', 'rightMax')
        self.leftMax = RobotConfig.Config.getfloat('robot', 'leftMax')
        self.rightMax = self.rightMax / 100.0
        self.leftMax = self.leftMax / 100.0

    def setLeftMotor(self, percent):
        try:
            print('leftMotor ' + str(percent))
            DMCC.setMotor(0, 1, int(percent * 100 * self.leftMax))
        except:
            print "Error setting left motor, trying again"
            self.setLeftMotor(percent)

    def setRightMotor(self, percent):
        try:
            print('rightMotor ' + str(percent))
            DMCC.setMotor(0, 2, int(percent * 100 * self.rightMax))
        except:
            print "Error setting right motor, trying again"
            #time.sleep(0.01)
            self.setRightMotor(percent)


