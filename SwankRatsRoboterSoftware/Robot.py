__author__ = 'Johannes'

import time

import threading

import DMCC
import RobotConfig


class Robot:
    def __init__(self):
        rm = RobotConfig.Config.getfloat('robot', 'rightMax')
        lm = RobotConfig.Config.getfloat('robot', 'leftMax')
        self.rightMax = rm / 100.0
        self.leftMax = lm / 100.0
        self.right = 0
        self.left = 0


    def set(self, left, right):
        threadLeft = self.setLeftMotor(left)
        threadRight = self.setRightMotor(right)

        threadLeft.join()
        threadRight.join()


    def setLeftMotor(self, percent):
        t = threading.Thread(target=setMotor, args=(self.right, percent, 5, "left", self.rightMax, 0.02))
        t.start()
        self.left = percent

        return t

    def setRightMotor(self, percent):
        t = threading.Thread(target=setMotor, args=(self.right, percent, 5, "right", self.rightMax, 0.02))
        t.start()
        self.right = percent

        return t


def setMotor(start, stop, step, motor, max, pause):
    if start < stop:
        up(start, stop, step, motor, max, pause)
    if start > stop:
        down(start, stop, step, motor, max, pause)


def up(start, stop, step, motor, max, pause):
    print "up " + motor + " " + str(start) + " " + str(stop)
    while start <= stop:
        print(start)
        set(motor, start, max)
        start += step
        time.sleep(pause)


def down(start, stop, step, motor, max, pause):
    print "down " + motor + " " + str(start) + " " + str(stop)
    while start >= stop:
        set(motor, start, max)
        start -= step
        time.sleep(pause)


def set(motor, value, max):
    try:
        value = int(value * 100 * max)
        if motor == "left":
            DMCC.setMotor(0, 1, value)
        if motor == "right":
            DMCC.setMotor(0, 2, value)
    except:
        print "Error setting " + motor + " motor, trying again"
