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
        print('leftMotor ' + str(percent))
        DMCC.setMotor(0, 1, int(percent * 100 * self.leftMax))

    def setRightMotor(self, percent):
        print('rightMotor ' + str(percent))
        DMCC.setMotor(0, 2, int(-percent * 100 * self.rightMax))


