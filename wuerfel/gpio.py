#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import time
import random
import RPi.GPIO as GPIO

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup([4, 17, 18, 22, 23, 24, 27], GPIO.OUT, initial=GPIO.LOW)

def roll(_):
	GPIO.output([4, 17, 18, 22, 23, 24, 27], GPIO.LOW)
	
	i = random.randint(1, 6)
	if i == 1:
		GPIO.output(27, GPIO.HIGH)
	elif i == 2:
		GPIO.output([4, 24], GPIO.HIGH)
	elif i == 3:
                GPIO.output([4, 24, 27], GPIO.HIGH)
	elif i == 4:
		GPIO.output([4, 18, 22, 24], GPIO.HIGH)
	elif i == 5:
		GPIO.output([4, 18, 22, 24, 27], GPIO.HIGH)
	elif i == 6:
		GPIO.output([4, 17, 18, 22, 23, 24], GPIO.HIGH)
	else:
                GPIO.output([4, 17, 18, 22, 23, 24, 27], GPIO.HIGH)
	print i

try:
	#Initial-Roll
	roll('')
	
	#Port-Listeners
	GPIO.add_event_detect(25, GPIO.RISING, callback=roll, bouncetime=200)
	
	#Loop
	while True:
		time.sleep(0.005)
finally:
        print "Cleaning up..."
	GPIO.cleanup()
