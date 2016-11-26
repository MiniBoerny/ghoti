#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import os
import time
import datetime
import RPi.GPIO as GPIO

#Variablen
fwdLPin = 18
bwdLPin = 23
writeFileDir = "remote/move/"

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup(fwdLPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bwdLPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def output():
        command = ""
        
        if GPIO.input(fwdLPin):
                command += "_FR_"
        elif GPIO.input(bwdLPin):
                command += "_BR_"

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
