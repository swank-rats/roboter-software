__author__ = 'Johannes'
#import Adafruit_BBIO.GPIO as GPIO
import DMCC
import time

class Robot:


    def setLeftMotor(self, percent):
        actuel = 0
        if percent == 0:
            print('leftMotor ' + str(percent))
            DMCC.setMotor(0, 1, percent * 100 * 0.60)
        if percent > 0:
            actuel = 10
            while actuel <= percent:
                print('leftMotor ' + str(actuel))
                DMCC.setMotor(0, 1, actuel * 100 * 0.60)
                actuel += 5
                time.sleep(0.30)
        if percent < 0:
            actuel = -10
            while actuel >= percent:
                print('leftMotor ' + str(actuel))
                DMCC.setMotor(0, 1, actuel * 100 * 0.60)
                actuel -= 5
                time.sleep(0.300)

    def setRightMotor(self, percent):
        actuel = 0
        if percent == 0:
            print('rightMotor ' + str(percent))
            DMCC.setMotor(0, 2, percent * 100 * 0.60)
        if percent > 0:
            actuel = 10
            while actuel <= percent:
                print('rightMotor ' + str(actuel))
                DMCC.setMotor(0, 2, actuel * 100 * 0.60)
                actuel += 5
                time.sleep(0.30)
        if percent < 0:
            actuel = -10
            while actuel >= percent:
                print('rightMotor ' + str(actuel))
                DMCC.setMotor(0, 2, actuel * 100 * 0.60)
                actuel -= 5
                time.sleep(0.30)

    def driveStraight(self):
        self.setLeftMotor(80)
        self.setRightMotor(80)

    def driveBackwards(self):
        self.setLeftMotor(-80)
        self.setRightMotor(-80)

    def driveLeft(self):
        self.setRightMotor(100)
        self.setLeftMotor(40)

    def driveRight(self):
        self.setLeftMotor(100)
        self.setRightMotor(40)

    def stop(self):
        self.setLeftMotor(0)
        self.setRightMotor(0)