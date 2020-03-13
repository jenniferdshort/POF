import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

import globals    #//accesses the global variables file

initialX = globals.xAxisLocal
initialR = globals.rotateAxisLocal
initialZ = globals.zAxisLocal

def pulse(pin,delay):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)

def x(goalX):
    #goal value is a lateral location
    global initialX
    distance = abs(goalX - initialX) #distance necessary to travel
    stepsCurrent = initialX #Initial position
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
             
def r(goalR):
    #goal value is an angle in degrees
    #angle should go from -90 to 90
    
    global initialR
    stepsCurrent = initialR #Initial position
    goalR = abs(goalR)
    
    steps_per_revolution = 800
    distance = round(goalR / 360 * steps_per_revolution)
    ###########################################################: Movement parameters
    acceleration_constant = 0.0000005 #acceleration value
    delay = 0.001 #determines starting speed
    minDelay = 0.0004 #determines maximum speed
    direction = 1
    cruiseSteps = 0
    ###########################################################: Pin setup
    control_pin = 32 #arbitrary pin. Change when everything is plugged in.
    GPIO.setup(control_pin, GPIO.OUT)
    
    dirPin = 36 #arbitrary pin. Change when everything is plugged in.
    GPIO.setup(dirPin, GPIO.OUT)
    ###########################################################: Direction set
    if goalR < 0:
        direction = 1
    else:
        direction = 0
    GPIO.output(dirPin, direction)
    
    ###########################################################: Rotation block    
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
    ###########################################################: End rotation block    
    
def z(goalZ):
    #goal value is either 'up' or 'down'
    global initialZ
    stepsCurrent = initialZ #Initial position
    distance = 2400 #number of steps between up and down position
    
    ###########################################################: Movement parameters
    acceleration_constant = 0.0000005 #acceleration value
    delay = 0.001 #determines starting speed
    minDelay = 0.0004 #determines maximum speed
    direction = 1
    cruiseSteps = 0
    ###########################################################: Pin setup
    control_pin = 32 #arbitrary pin. Change when everything is plugged in.
    GPIO.setup(control_pin, GPIO.OUT)
    
    dirPin = 36 #arbitrary pin. Change when everything is plugged in.
    GPIO.setup(dirPin, GPIO.OUT)
    ###########################################################: Direction set
    if goalZ == "up":
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
    ###########################################################: End Movement block  
    
GPIO.cleanup()