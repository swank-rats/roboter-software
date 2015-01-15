__author__ = 'Johannes'

from Robot import Robot
import time

if __name__ == '__main__':
    robot = Robot()
    robot.setRightMotor(100)
    time.sleep(5)
    robot.setRightMotor(0)
