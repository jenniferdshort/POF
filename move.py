# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:07:25 2020

@author: chans
"""
import RPi.GPIO as GPIO
import time
import global_variables

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#################PIN DEFINITION#################
xPul = 29                    #change to real pin
GPIO.setup(xPul, GPIO.OUT)
xDir = 31                    #change to real pin
GPIO.setup(xDir, GPIO.OUT)

rPul = 33                    #change to real pin
GPIO.setup(rPul, GPIO.OUT)
rDir = 35                    #change to real pin
GPIO.setup(rDir, GPIO.OUT)

zPul = 38                    #change to real pin
GPIO.setup(zPul, GPIO.OUT)
zDir = 40                    #change to real pin
GPIO.setup(zDir, GPIO.OUT)

#################PULSE FUNCTION#################
def pulse(pin, delay):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)
    
#################X MOVEMENT FUNCTION#################
def x(position):
    x0 = global_variables.get("x")
    
    #################CONVERTING LOCATION TO STEP COUNT#################
    position = position.lower()         #converts to lower case
    if position == "deposition":
        xGoal = 7400
        
    elif position == "heating":
        xGoal = 131400                   #TBD Experimentally
    
    elif position == "compression":
        xGoal = 130600 + 94300                   #TBD Experimentally
        
    elif position == "end":
        xGoal = 1 * (68800 + 130600 + 94400)                  #TBD Experimentally
    
    difference = xGoal - x0
    distance = abs(difference)
    midpoint = round(distance / 2)
    cruiseSteps = 0
    moveSteps = 0
    
    #################MOVEMENT PARAMETERS#################
    acceleration = (39 / 1000000)
    delayMin = 0.000075
    delayMin2 = 0.00004
    delayMax = 0.004
    delay = delayMax
    
    #################DIRECTION SET#################
    if difference >= 0:
        GPIO.output(xDir, GPIO.HIGH)
        
    else:
        GPIO.output(xDir, GPIO.LOW)
        
    #################MOVEMENT BLOCK#################
    while moveSteps != distance:
        pulse(xPul, delay)
        
        if moveSteps <= midpoint:
            if delay >= delayMin:           #accelerating
                delay -= (acceleration / 3)
            
            else:                           #cruising
                cruiseSteps += 1
                if (delay > delayMin2):
                    delay -= (acceleration / 10400)

        else:
            if cruiseSteps:                 #cruising
                cruiseSteps -= 1
                
            else:                           #decelerating
                delay += (acceleration / 100)
        
        moveSteps += 1
        
    global_variables.set_to("x", int(xGoal))

#################R MOVEMENT FUNCTION#################
def r(angleGoal):
    r0 = global_variables.get("r")
    spr = 800                           #steps per revolution
    
    scaleFactor = 25.93                     #factor compensating for the gearing of the stepper vs the platform
    
    rGoal = round((angleGoal / 360) * spr * scaleFactor)  #converted from degrees into steps
    
    difference = rGoal - r0
    distance = abs(difference)
    midpoint = round(distance / 2)
    cruiseSteps = 0
    moveSteps = 0

    #print("r0 = %d"%r0)
    #print("rGoal = %d" %rGoal)
    #print("difference = %d" %difference)
    #print("distance = %d"% distance)

    #################MOVEMENT PARAMETERS#################
    acceleration = (95 / 1000000)
    delayMin = 0.0007
    delayMax = 0.005
    delay = delayMax
    
    #################DIRECTION SET#################
    if difference >= 0:
        GPIO.output(rDir, GPIO.LOW)

    else:
        GPIO.output(rDir, GPIO.HIGH)
    
    #################MOVEMENT BLOCK#################
    while moveSteps != distance:
        pulse(rPul, delay)
        
        if moveSteps <= midpoint:
            if delay >= delayMin:           #accelerating
                delay -= acceleration
            
            else:                           #cruising
                cruiseSteps += 1

        else:
            if cruiseSteps:                 #cruising
                cruiseSteps -= 1
                
            else:                           #decelerating
                delay += acceleration

        moveSteps += 1 #adds new step
        
    global_variables.set_to("r", int(rGoal))

#################Z MOVEMENT FUNCTION#################
def z(heightGoal):
    z0 = global_variables.get("z")
    
    spr = 800                           #steps per revolution
    
    heightGoal = heightGoal.lower()
    if heightGoal == "up":
        zGoal = round(spr * 0.75)
    elif heightGoal == "down":
        zGoal = 0
    
    difference = zGoal - z0
    distance = abs(difference)
    midpoint = round(distance / 2)
    cruiseSteps = 0
    moveSteps = 0
    
    #################MOVEMENT PARAMETERS#################
    acceleration = (95 / 1000000)
    delayMin = 0.001
    delayMax = 0.002
    delay = delayMax
    
    #################DIRECTION SET#################
    if difference >= 0:
        GPIO.output(zDir, GPIO.HIGH)

    else:
        GPIO.output(zDir, GPIO.LOW)
        
    #################MOVEMENT BLOCK#################
    while moveSteps != distance:
        pulse(zPul, delay)
        
        if moveSteps <= midpoint:
            if delay >= delayMin:           #accelerating
                delay -= acceleration
            
            else:                           #cruising
                cruiseSteps += 1

        else:
            if cruiseSteps:                 #cruising
                cruiseSteps -= 1
                
            else:                           #decelerating
                delay += acceleration
                
        moveSteps += 1
    global_variables.set_to("z", int(zGoal))