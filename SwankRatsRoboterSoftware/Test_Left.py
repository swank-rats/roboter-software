__author__ = 'Johannes'

import time

from Robot import Robot

if __name__ == '__main__':
    robot = Robot()
    robot.setLeftMotor(100)
    time.sleep(5)
    robot.setLeftMotor(0)
