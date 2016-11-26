#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import os
import time
import RPi.GPIO as GPIO

#Variablen
statusPin = 20
outputPin = 21
readFileDir = "status/"

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup(statusPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(outputPin, GPIO.OUT, initial=GPIO.LOW)

def _read():
    readFileList = sorted(os.listdir(readFileDir))
    
    if len(readFileList) > 0:
        readFile = readFileDir + readFileList.pop(0)
        
        with open(readFile, "r") as f:
            fcont = f.read()
            
            print readFile + ": " + fcont
            if "F" in fcont:
                fwd(True)
            else:
                fwd(False)

        os.remove(readFile)
    else:
        print "no file"
        fwd(False)

def fwd(enabled):
    if enabled:
        GPIO.output(outputPin, GPIO.HIGH)
    else:
        GPIO.output(outputPin, GPIO.LOW)

try:
    #Initial
    for f in os.listdir(readFileDir):
        os.remove(readFileDir + f)
    
    #Loop
    while True:
        _read()
	time.sleep(0.05)

finally:
    print "Cleaning up..."
    GPIO.cleanup()
