# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:38:10 2020

@author: chans
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#################PIN DEFINITION#################
mediaDep = 23
GPIO.setup(mediaDep, GPIO.OUT)

#scaleIn = 1
#GPIO.setup(scaleIn, GPIO.IN)

heater = 21
GPIO.setup(heater, GPIO.OUT)

solenoid = 19
GPIO.setup(solenoid, GPIO.OUT)

#################MEDIA DEPOSITION#################
def auger_pulse(duration):
    if duration == "long":
        pd = 0.2
        
    elif duration == "short":
        pd = 0.1

    GPIO.output(mediaDep, GPIO.HIGH)
    time.sleep(pd)
    GPIO.output(mediaDep, GPIO.LOW)

#################SCALE READING#################
def tare():
    dothingstotarethescale

def mass_dispense(massGoal): #Looks like 20g is a decent guesstimate for one layer
    largeDiff = 7 #grams
    tolerance = 2 #grams
    
    mass = serial.read.mass.stuff
    difference = massGoal - mass
    
    while(difference > tolerance):
        if(abs(difference) > largeDiff):
            auger_pulse("long")
            time.sleep(0.5)
            
        else:
            auger_pulse("short")
            time.sleep(2.5)
        
        mass = serial.read.mass.stuff
        difference = massGoal - mass

#################IR HEATER CONTROL#################
def heat_on():
    GPIO.output(heater, GPIO.HIGH)

def heat_off():
    GPIO.output(heater,GPIO.LOW)

#################SOLENOID ACTUATION#################
def compress():
    GPIO.output(solenoid, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(solenoid, GPIO.LOW)
    time.sleep(0.25)