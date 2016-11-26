#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import os
import time
import datetime
import RPi.GPIO as GPIO

#Variablen
fwdPin = 18
bwdPin = 23
writeFileDir = "remote/move/"

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup(fwdPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bwdPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def output():
        command = ""
        
        if GPIO.input(fwdPin):
                command += "F"
        elif GPIO.input(bwdPin):
                command += "B"

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
                        print ts + ":" + command
                        time.sleep(0.05)
                else:
                        print "no output"
                	time.sleep(0.02)

finally:
        print "Cleaning up..."
	GPIO.cleanup()
