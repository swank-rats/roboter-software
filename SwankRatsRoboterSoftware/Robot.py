__author__ = 'Johannes'
#import Adafruit_BBIO.GPIO as GPIO

class Robot:


    def setLeftMotor(self, percent):
        print('leftMotor ' + percent)

    def setRightMotor(self, percent):
        print('rightMotor ' + percent)

    def driveStraight(self):
        self.setLeftMotor(80)
        self.setRightMotor(80)

    def driveLeft(self):
        self.setRightMotor(100)
        self.setLeftMotor(40)

    def driveRight(self):
        self.setLeftMotor(100)
        self.setRightMotor(40)