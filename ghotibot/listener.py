#!/usr/bin/python
# -*- coding: utf-8 -*-

#sudo apt-get install python-rpi.gpio python3-rpi.gpio

import os
import time
import RPi.GPIO as GPIO

#Variablen
runPin = 21
fwdLPin = 26
bwdLPin = 19
fwdRPin = 13
bwdRPin = 6
readFileDir = "remote/move/"

#Numerierung dper Board-Beschriftung
GPIO.setmode(GPIO.BCM)
#Setzen der In-/Outputs der benötigten Pins
GPIO.setup(runPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(fwdLPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(bwdLPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(fwdRPin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(bwdRPin, GPIO.OUT, initial=GPIO.HIGH)

def listen():
    empty = True
    readFileList = sorted(os.listdir(readFileDir))
    
    if len(readFileList) > 0:
        readFile = readFileDir + readFileList.pop(0)
        
        with open(readFile, "r") as f:
            fcont = f.read()
        os.remove(readFile)

        if "_F_" in fcont:
            fwdL(True)
            bwdL(False)
            fwdR(True)
            bwdR(False)
            empty = False
        elif "_B_" in fcont:
            fwdL(False)
            bwdL(True)
            fwdR(False)
            bwdR(True)
            empty = False
        elif "_L_" in fcont:
            fwdL(False)
            bwdL(True)
            fwdR(True)
            bwdR(False)
            empty = False
        elif "_R_" in fcont:
            fwdL(True)
            bwdL(False)
            fwdR(False)
            bwdR(True)
            empty = False
        elif "_FR_" in fcont:
            fwdL(True)
            bwdL(False)
            fwdR(False)
            bwdR(False)
            empty = False
        elif "_BR_" in fcont:
            fwdL(False)
            bwdL(True)
            fwdR(False)
            bwdR(False)
            empty = False
        elif "_FL_" in fcont:
            fwdL(False)
            bwdL(False)
            fwdR(True)
            bwdR(False)
            empty = False
        elif "_BL_" in fcont:
            fwdL(False)
            bwdL(False)
            fwdR(False)
            bwdR(True)
            empty = False
        else:
            idle()

        print readFile + ": " + fcont
    else:
        print "no input"
        idle()

    return empty

def idle():
    fwdL(False)
    bwdL(False)
    fwdR(False)
    bwdR(False)

def fwdL(enabled):
    if enabled:
        GPIO.output(fwdLPin, GPIO.LOW)
    else:
        GPIO.output(fwdLPin, GPIO.HIGH)

def bwdL(enabled):
    if enabled:
        GPIO.output(bwdLPin, GPIO.LOW)
    else:
        GPIO.output(bwdLPin, GPIO.HIGH)

def fwdR(enabled):
    if enabled:
        GPIO.output(fwdRPin, GPIO.LOW)
    else:
        GPIO.output(fwdRPin, GPIO.HIGH)

def bwdR(enabled):
    if enabled:
        GPIO.output(bwdRPin, GPIO.LOW)
    else:
        GPIO.output(bwdRPin, GPIO.HIGH)

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
