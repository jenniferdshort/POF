# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:51:23 2020

@author: chans
"""
import global_variables
import RPi.GPIO as GPIO
import time
import move

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#################PIN DEFINITION#################
xPul = 29                    #change to real pin
GPIO.setup(xPul, GPIO.OUT)
xDir = 31                    #change to real pin
GPIO.setup(xDir, GPIO.OUT)
xSensor = 13
GPIO.setup(xSensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

rPul = 33                    #change to real pin
GPIO.setup(rPul, GPIO.OUT)
rDir = 35                    #change to real pin
GPIO.setup(rDir, GPIO.OUT)
rSensor = 11
GPIO.setup(rSensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

zPul = 38                    #change to real pin
GPIO.setup(zPul, GPIO.OUT)
zDir = 40                    #change to real pin
GPIO.setup(zDir, GPIO.OUT)
zSensor = 15
GPIO.setup(zSensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#################PULSE FUNCTION#################
def pulse(pin, delay):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)
    
#################SPEED VALUES#################
pdX = 0.0005
pdR = 0.0012
pdZ = 0.002

def home_axes():
    #################X AXIS HOME#################
    GPIO.output(xDir, GPIO.LOW)
    while(GPIO.input(xSensor)):
        pulse(xPul, pdX)
    global_variables.set_to("x",0)

    #################R AXIS HOME#################
    GPIO.output(rDir, GPIO.LOW)
    
    moveLater = 0
    
    while(GPIO.input(rSensor) == 0):
        pulse(rPul, pdR)
        moveLater = 1
    if(moveLater):
        move.r(25 / 25.93)
    global_variables.set_to("r",0)

    #################Z AXIS HOME#################
    GPIO.output(zDir, GPIO.LOW)
    while(GPIO.input(zSensor) == 0):
        pulse(zPul, pdZ)
    global_variables.set_to("z",0)
    #move.z("up")