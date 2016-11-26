#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import os
import time
import datetime
import RPi.GPIO as GPIO

#Variablen
inputPin = 18
writeFileDir = "status/"

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def listen():
        command = ""
        
        if GPIO.input(inputPin):
                command += "F"

        print command
        return command

try:
        #Initial
        for f in os.listdir(writeFileDir):
                os.remove(writeFileDir + f)
        
	#Loop
	while True:
                ts = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
                with open(writeFileDir + ts, "w") as f:
                        f.write(listen())
		time.sleep(0.05)

finally:
        print "Cleaning up..."
	GPIO.cleanup()
