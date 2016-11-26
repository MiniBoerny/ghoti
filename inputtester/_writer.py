#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import os
import time
import datetime
import random
#import RPi.GPIO as GPIO

#Variablen
#inputPin = 18
writeFileDir = "status/"

#Numerierung dper Board-Beschriftung
#GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
#GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def listen():
        command = ""
        
        if random.randint(0, 1):
                command += "F"
        
        return command

try:
        #Initial
        for f in os.listdir(writeFileDir):
                os.remove(writeFileDir + f)
        
	#Loop
	while True:
                ts = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
                with open(writeFileDir + ts, "w") as f:
                        ret = listen()
                        f.write(ret)
                        print ts + ": " + ret
		time.sleep(0.05)

finally:
        print "Cleaning up..."
	#GPIO.cleanup()
