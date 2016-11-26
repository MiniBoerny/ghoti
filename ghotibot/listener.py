#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import os
import time
import RPi.GPIO as GPIO

#Variablen
runPin = 21
fwdPin = 26
bwdPin = 19
readFileDir = "remote/move/"

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup(runPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(fwdPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(bwdPin, GPIO.OUT, initial=GPIO.HIGH)

def listen():
    empty = True
    readFileList = sorted(os.listdir(readFileDir))
    
    if len(readFileList) > 0:
        readFile = readFileDir + readFileList.pop(0)
        
        with open(readFile, "r") as f:
            fcont = f.read()
        os.remove(readFile)

        if "F" in fcont:
            fwd(True)
            bwd(False)
            empty = False
        elif "B" in fcont:
            fwd(False)
            bwd(True)
            empty = False
        else:
            fwd(False)
            bwd(False)

        print readFile + ": " + fcont
        return empty
    else:
        print "no input"
        fwd(False)

def fwd(enabled):
    if enabled:
        GPIO.output(fwdPin, GPIO.LOW)
    else:
        GPIO.output(fwdPin, GPIO.HIGH)

def bwd(enabled):
    if enabled:
        GPIO.output(bwdPin, GPIO.LOW)
    else:
        GPIO.output(bwdPin, GPIO.HIGH)

try:
    #Initial
    for f in os.listdir(readFileDir):
        os.remove(readFileDir + f)
    
    #Loop
    while True:
        if listen():
            time.sleep(0.02)
        else:
            time.sleep(0.05)

finally:
    print "Cleaning up..."
    GPIO.cleanup()
