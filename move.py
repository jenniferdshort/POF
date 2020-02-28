import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

import globals    #//accesses the global variables file

initialX = globals.xAxisLocal
initialR = globals.rotateAxisLocal
initialz = globals.zAxisLocal

def pulse(pin,delay):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)

def x(goalX):
    #goal value is a lateral location
    global initialX
    distance = abs(goalX - initialX) #distance necessary to travel
    stepsCurrent = 0 #Initial position
    cruiseSteps = 0 
    
    ###########################################################: Movement parameters
    acceleration_constant = 0.0000005 #acceleration value
    delay = 0.001 #determines starting speed
    minDelay = 0.0004 #determines maximum speed
    direction = 1
    ###########################################################: Pin setup
    control_pin = 32 #arbitrary pin. Change when everything is plugged in.
    GPIO.setup(control_pin, GPIO.OUT)
    
    dirPin = 36 #arbitrary pin. Change when everything is plugged in.
    GPIO.setup(dirPin, GPIO.OUT)
    ###########################################################: Direction set
    if (goalX - initialX) > 0:
        direction = 1
    else:
        direction = 0

    GPIO.output(dirPin, direction)
    ###########################################################: Movement block    
    while True:
        if stepsCurrent == distance: #End of move
            break
        
        #accelerating/cruising
        elif stepsCurrent < (distance/2):
            if delay >= minDelay: #accelerate
                pulse(control_pin, delay)
                stepsCurrent +=1
                delay -= acceleration_constant
            else: #cruising
                pulse(control_pin, delay)
                stepsCurrent += 1
                cruiseSteps += 1
        #Cruising/decelerating
        else:
            if cruiseSteps: #cruising
                pulse(control_pin, delay)
                stepsCurrent +=1
                cruiseSteps -=1
            else: #decelerating
                pulse(control_pin, delay)     
                stepsCurrent +=1
                delay += acceleration_constant
    ###########################################################: End X movement block
             
    
#def r(goalR):
    #goal value is an angle in degrees
    
    
#def z(goalZ):
    #goal value is up or down
    
x(12800)

GPIO.cleanup()