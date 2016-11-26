#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import os
import time
import RPi.GPIO as GPIO

#Variablen
runPin = 21
fwd1Pin = 26
bwd1Pin = 19
readFileDir = "remote/move/"

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup(runPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(fwd1Pin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(bwd1Pin, GPIO.OUT, initial=GPIO.HIGH)

def listen():
    empty = True
    readFileList = sorted(os.listdir(readFileDir))
    
    if len(readFileList) > 0:
        readFile = readFileDir + readFileList.pop(0)
        
        with open(readFile, "r") as f:
            fcont = f.read()
        os.remove(readFile)

        if "F1" in fcont:
            fwd1(True)
            bwd1(False)
            empty = False
        elif "B1" in fcont:
            fwd1(False)
            bwd1(True)
            empty = False
        else:
            idle()

        print readFile + ": " + fcont
    else:
        print "no input"
        idle()

    return empty

def idle():
    fwd1(False)
    bwd1(False)

def fwd1(enabled):
    if enabled:
        GPIO.output(fwd1Pin, GPIO.LOW)
    else:
        GPIO.output(fwd1Pin, GPIO.HIGH)

def bwd1(enabled):
    if enabled:
        GPIO.output(bwd1Pin, GPIO.LOW)
    else:
        GPIO.output(bwd1Pin, GPIO.HIGH)

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
