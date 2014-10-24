__author__ = 'Johannes'
import Adafruit_BBIO.PWM as PWM
import time

P = "P8_10"

PWM.start(P, 50)

for i in xrange(100):      
	PWM.set_duty_cycle(P, i)
	print "Up"       
	time.sleep(0.5)

i = 0		
for i in xrange(100):      
	PWM.set_duty_cycle(P, 100-i)
	print "Down"       
	time.sleep(0.5)		
		
PWM.stop(P)
PWM.cleanup()