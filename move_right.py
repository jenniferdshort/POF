# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:26:59 2020

@author: chans
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#################PIN DEFINITION#################
xPul = 29                    #change to real pin
GPIO.setup(xPul, GPIO.OUT)
xDir = 31                    #change to real pin
GPIO.setup(xDir, GPIO.OUT)
xSensor = 15
GPIO.setup(xSensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

rPul = 33                    #change to real pin
GPIO.setup(rPul, GPIO.OUT)
rDir = 35                    #change to real pin
GPIO.setup(rDir, GPIO.OUT)
rSensor = 13
GPIO.setup(rSensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#################PULSE FUNCTION#################
def pulse(pin, delay):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)
    
pd = 0.002
offset = 0

#################MOVEMENT#################
GPIO.output(rDir, GPIO.LOW)

#for i in range(800):
#    pulse(xPul, pd)
#    offset += 1

#print("prelim offset = %d"%offset)

while(GPIO.input(rSensor) == 0):
    pulse(rPul, pd)
    offset += 1

offset = offset + round(25 / 360 * 800)
print("Offset = %d"%offset)