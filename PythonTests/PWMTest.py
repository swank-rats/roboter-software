__author__ = 'Johannes'
import Adafruit_BBIO.PWM as PWM
import time

P = "P8_13"

PWM.start(P, 50)

def fadeUp():
        for i in range(0,100):
                PWM.set_duty_cycle(P, i)
                print "Up"
                time.sleep(0.05)

def fadeDown():
        for i in range(0,100):
                PWM.set_duty_cycle(P, 100-i)
                print "Down"
                time.sleep(0.05)

try:
        while True:
                fadeUp()
                fadeDown()

except (KeyboardInterrupt, SystemExit):
        PWM.stop(P)
        PWM.cleanup()
