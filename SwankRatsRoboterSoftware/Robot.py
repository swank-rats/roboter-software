__author__ = 'Johannes'
# import Adafruit_BBIO.GPIO as GPIO

import DMCC
import time
import RobotConfig
from thread import start_new_thread
import threading

class Robot:
    def __init__(self):
        self.rightMax = RobotConfig.Config.getfloat('robot', 'rightMax')
        self.leftMax = RobotConfig.Config.getfloat('robot', 'leftMax')
        self.rightMax = self.rightMax / 100.0
        self.leftMax = self.leftMax / 100.0
        self.right = 0
        self.left = 0

    def setLeftMotor(self, percent):
        #start_new_thread(setMotor, (self.left,percent,5,"left",self.leftMax,0.02))
        t = threading.Thread(target=setMotor, args=(self.right,percent,5,"left",self.rightMax,0.02))
        t.start()
        self.left = percent

    def setRightMotor(self, percent):
        t = threading.Thread(target=setMotor, args=(self.right,percent,5,"right",self.rightMax,0.02))
        t.start()
        #start_new_thread(setMotor, (self.right,percent,5,"right",self.rightMax,0.02))
        self.right = percent

def setMotor(start, stop, step, motor, max, pause):
    if(start < stop):
        up(start, stop, step, motor, max, pause)
    if(start > stop):
        down(start, stop, step, motor, max, pause)

def up(start, stop, step, motor, max, pause):
    print "up"
    while start <= stop:
        start += step
        time.sleep(pause)
        print(start)
#        try:
#            if motor == "left":
#                DMCC.setMotor(0, 1, int(start * 100 * max))
#            if motor == "right":
#                DMCC.setMotor(0, 2, int(start * 100 * max))
#        except:
#            print "Error setting " + motor + " motor, trying again"

def down(start, stop, step, motor, max, pause):
    print "down "+str(start)+ " "+str(stop)
    while start >= stop:
        start -= step
        time.sleep(pause)
        print(start)
#        try:
#            if motor == "left":
#                DMCC.setMotor(0, 1, int(start * 100 * max))
#            if motor == "right":
#                DMCC.setMotor(0, 2, int(start * 100 * max))
#        except:
#            print "Error setting " + motor + " motor, trying again"

