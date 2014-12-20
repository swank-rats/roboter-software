__author__ = 'Johannes'
#import Adafruit_BBIO.GPIO as GPIO
import DMCC


class Robot:


    def setLeftMotor(self, percent):
        actuel = 0
        if percent == 0:
            print('leftMotor ' + str(percent))
            DMCC.setMotor(0, 1, percent * 100/2)
        if percent > 0:
            while actuel <= percent:
                print('leftMotor ' + str(actuel))
                DMCC.setMotor(0, 1, actuel * 100/2)
                actuel += 1
        if percent < 0:
            while actuel >= percent:
                print('leftMotor ' + str(actuel))
                DMCC.setMotor(0, 1, actuel * 100/2)
                actuel -= 1

    def setRightMotor(self, percent):
        actuel = 0
        if percent == 0:
            print('rightMotor ' + str(percent))
            DMCC.setMotor(0, 2, percent * 100/2)
        if percent > 0:
            while actuel <= percent:
                print('rightMotor ' + str(actuel))
                DMCC.setMotor(0, 2, actuel * 100/2)
                actuel += 1
        if percent < 0:
            while actuel >= percent:
                print('rightMotor ' + str(actuel))
                DMCC.setMotor(0, 2, actuel * 100/2)
                actuel -= 1

    def driveStraight(self):
        self.setLeftMotor(80)
        self.setRightMotor(80)

    def driveLeft(self):
        self.setRightMotor(100)
        self.setLeftMotor(40)

    def driveRight(self):
        self.setLeftMotor(100)
        self.setRightMotor(40)