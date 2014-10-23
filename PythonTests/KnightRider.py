__author__ = 'Johannes'
#Import Libraries
##################

#Tell python we need the library "os" for executing system commands directly
import os

#Tell python we need the library "time" so we can use the "sleep" command
import time

##################


#Define Variables
##################

#Define commands to be executed later on based on logic
#Command for turning led0 "On"
led0_on = 'echo 1 > /sys/class/leds/beaglebone\:green\:usr0/brightness'
#Command for turning led0 "Off"
led0_off = 'echo 0 > /sys/class/leds/beaglebone\:green\:usr0/brightness'


#Command for turning led1 "On"
led1_on = 'echo 1 > /sys/class/leds/beaglebone\:green\:usr1/brightness'
#Command for turning led1 "Off"
led1_off = 'echo 0 > /sys/class/leds/beaglebone\:green\:usr1/brightness'

#Command for turning led2 "On"
led2_on = 'echo 1 > /sys/class/leds/beaglebone\:green\:usr2/brightness'
#Command for turning led2 "Off"
led2_off = 'echo 0 > /sys/class/leds/beaglebone\:green\:usr2/brightness'

#Command for turning led3 "On"
led3_on = 'echo 1 > /sys/class/leds/beaglebone\:green\:usr3/brightness'
#Command for turning led3 "Off"
led3_off = 'echo 0 > /sys/class/leds/beaglebone\:green\:usr3/brightness'
##################



#Begin Execution
##################

#Infinite On/off loop to make light blink
#Define "i" variable
i = 0;

#Begin Infinite loop
while(True):
        if i == 0:
                #Tell Beaglebone that we want LED0 "on"
                os.system(led0_on)

                #Tell Beaglebone that we want LED0, LED1 and LED3 "off"
                os.system(led1_off)
                os.system(led2_off)
                os.system(led3_off)

                #Tell python to turn led1 on next
                i = 1

        elif i == 1:
                #Tell BeagleBone that we want LED1 "on
                os.system(led1_on)

                #Tell Beaglebone that we want LED0, LED2 and LED3 "off"
                os.system(led0_off)
                os.system(led2_off)
                os.system(led3_off)

                #Tell python to turn led2 on next
                i = 2

        elif i == 2:
                #Tell BeagleBone that we want LED2 "on
                os.system(led2_on)

                #Tell Beaglebone that we want LED0, LED1 and LED3 "off"
                os.system(led0_off)
                os.system(led1_off)
                os.system(led3_off)

                #Tell python to turn led3 on next
                i = 3

        elif i == 3:
                #Tell BeagleBone that we want LED3 "on
                os.system(led3_on)

                #Tell Beaglebone that we want LED0, LED1 and LED2 "off"
                os.system(led0_off)
                os.system(led1_off)
                os.system(led2_off)

                #Tell python to turn led0 on next
                i = 4

        elif i == 4:
                #Tell BeagleBone that we want LED2 "on
                os.system(led2_on)

                #Tell Beaglebone that we want LED0, LED1 and LED3 "off"
                os.system(led0_off)
                os.system(led1_off)
                os.system(led3_off)

                #Tell python to turn led0 on next
                i = 5

        elif i == 5:
                #Tell BeagleBone that we want LED1 "on
                os.system(led1_on)

                #Tell Beaglebone that we want LED0, LED2 and LED3 "off"
                os.system(led0_off)
                os.system(led2_off)
                os.system(led3_off)

                #Tell python to turn led0 on next
                i = 0

        #Tell python to pause for 1 second then after the 1 second is over then continue with the infinite while loop
        time.sleep(0.15)


##################
#END OF LINE