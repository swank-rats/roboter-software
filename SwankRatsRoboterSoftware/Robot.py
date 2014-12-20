__author__ = 'Johannes'
#import Adafruit_BBIO.GPIO as GPIO
import DMCC


class Robot:


    def setLeftMotor(self, percent):
        print('leftMotor ' + str(percent))
        DMCC.setMotor(0, 1, percent * 100/2)

    def setRightMotor(self, percent):
        print('rightMotor ' + str(percent))
        DMCC.setMotor(0, 2, percent * 100/2)

    def driveStraight(self):
        self.setLeftMotor(80)
        self.setRightMotor(80)

    def driveLeft(self):
        self.setRightMotor(100)
        self.setLeftMotor(40)

    def driveRight(self):
        self.setLeftMotor(100)
        self.setRightMotor(40)