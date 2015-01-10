__author__ = 'Johannes'
# import Adafruit_BBIO.GPIO as GPIO
import DMCC
import time

class Robot:

    def __init__(self):
        global Config
        print(Config.get('robot', 'max'))

    def setLeftMotor(self, percent):
        print('leftMotor ' + str(percent))
        DMCC.setMotor(0, 1, int(percent * 100))

    def setRightMotor(self, percent):
        print('rightMotor ' + str(percent))
        DMCC.setMotor(0, 2, int(-percent * 100))


    def setLeftMotor2(self, percent):
        actuel = 0
        if percent == 0:
            print('leftMotor ' + str(percent))
            DMCC.setMotor(0, 1, int(percent * 100))
        if percent > 0:
            actuel = 10
            while actuel <= percent:
                print('leftMotor ' + str(actuel))
                DMCC.setMotor(0, 1, int(actuel * 100))
                actuel += 5
                time.sleep(0.30)
        if percent < 0:
            actuel = -10
            while actuel >= percent:
                print('leftMotor ' + str(actuel))
                DMCC.setMotor(0, 1, int(actuel * 100))
                actuel -= 5
                time.sleep(0.300)

    def setRightMotor2(self, percent):
        actuel = 0
        if percent == 0:
            print('rightMotor ' + str(percent))
            DMCC.setMotor(0, 2, int(percent * 100))
        if percent > 0:
            actuel = 10
            while actuel <= percent:
                print('rightMotor ' + str(actuel))
                DMCC.setMotor(0, 2, int(actuel * 100))
                actuel += 5
                time.sleep(0.30)
        if percent < 0:
            actuel = -10
            while actuel >= percent:
                print('rightMotor ' + str(actuel))
                DMCC.setMotor(0, 2, int(actuel * 100))
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
