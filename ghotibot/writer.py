#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import os
import time
import datetime
import RPi.GPIO as GPIO

#Variablen
fwd1Pin = 18
bwd1Pin = 23
writeFileDir = "remote/move/"

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup(fwd1Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bwd1Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def output():
        command = ""
        
        if GPIO.input(fwd1Pin):
                command += "F1"
        elif GPIO.input(bwd1Pin):
                command += "B1"

        return command

try:
        #Initial
        for f in os.listdir(writeFileDir):
                os.remove(writeFileDir + f)
        
	#Loop
	while True:
                ts = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
                command = output()

                if command != "":
                        with open(writeFileDir + ts, "w") as f:
                                f.write(command)
                        print writeFileDir + ts + ":" + command
                        time.sleep(0.05)
                else:
                        print "no output"
                	time.sleep(0.02)

finally:
        print "Cleaning up..."
	GPIO.cleanup()
