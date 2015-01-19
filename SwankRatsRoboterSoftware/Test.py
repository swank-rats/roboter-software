__author__ = 'Johannes'

import time

import Robot

if __name__ == '__main__':
    robot = Robot.Robot()
#    t1 = Robot.doSetMotor("right", 10, 0.25)
 #   t2 = Robot.doSetMotor("left", 10, 0.25)
    while True:
        robot.set(-100, -100)
        time.sleep(2)
        robot.set(0, 0)
        time.sleep(2)
        robot.set(100, 100)
        time.sleep(2)
        robot.set(0, 0)
        time.sleep(2)
