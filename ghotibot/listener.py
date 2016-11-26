#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import time
import RPi.GPIO as GPIO

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup([16, 20, 21], GPIO.OUT, initial=GPIO.LOW)

def read():
    key_fwd =
    key_left =
    key_right =
    key_light = 

def drive(dir):
    

try:
	#Port-Listeners
	#GPIO.add_event_detect(21, GPIO.RISING, , bouncetime=200)
	
	#Loop
	while True:
		time.sleep(0.005)
		read()
finally:
        print "Cleaning up..."
	GPIO.cleanup()
