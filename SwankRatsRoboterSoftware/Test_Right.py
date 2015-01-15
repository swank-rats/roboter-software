__author__ = 'Johannes'

import time

from Robot import Robot

if __name__ == '__main__':
    robot = Robot()
    robot.setRightMotor(100)
    time.sleep(5)
    robot.setRightMotor(0)
