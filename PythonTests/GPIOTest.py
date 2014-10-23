__author__ = 'Johannes'
import Adafruit_BBIO.GPIO as GPIO
import time

P = "USR3"

GPIO.setup(P, GPIO.OUT)
for i in xrange(100):
        if i % 2 == 0:
                GPIO.output(P, GPIO.HIGH)
                print "HIGH"
        else:
                GPIO.output(P, GPIO.LOW)
                print "LOW"
        time.sleep(0.5)
GPIO.cleanup()