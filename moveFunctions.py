# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:56:55 2020

@author: Teal
"""
import globals 

# Function to move from step count of A to step count of B, 
# so the trapazoidal velocity curve code can be used for the X, Z, and rotation axis
# Might not be beneficial how I have it? TBD
def moveTrap(start, end, axis):
    
    # Read acceleration and deceleration values
    # Figure out the time/distance for acceleration and decelleration
    # Perform movement
    
    # Figure out which axis to control
    if axis == "x": stepPin = 20
    elif axis == "z": stepPin = 30
    elif axis == "rot": stepPin = 40
    else: print("Error in movement axis")
    

# X movement function
def x(destination):
    
    # Decipher destination from words to numbers
    if destination == "feeder":
        endStep = 100
    elif destination == "heater":
        endStep = 200
    elif destination == "compress":
        endStep = 300
    else:
        print("Error recognizing destination position")
        endStep = -1

    startStep = globals.xAxisLocal
    
    moveTrap(startStep, endStep, "x")
    
    print("Moved to X: ", endStep)
    
    # Code for moving from point A to B

# rotate movement function
def rotate(destinationAngle):
    
    startStep = globals.rotateAxisLocal
    

    # Read current angle
    # Calculate step count of destination angle
    # Move rotation
    
    print("Rotated to angle: ", destinationAngle)

# Z movement function   
def z(desination):
    
    # Decipher destination from words to numbers
    if desination == "up":
        destinationPosition = 500
    elif desination == "down":
        destinationPosition = 100
    else:
        print("Error in determining z destination")
    
    startStep = globals.zAxisLocal
    endStep = destinationPosition
    
    # Code for raising or lowering
    # Read current position
    # Read target position
    # Only a binary movement, "up" or "down"
    
    print("Z moved: ", destination)

# Auger feeder function
def feed(mass):
    
    # Code to feed the specific mass required
    # Track the mass to go, and have diff feed rates dependong on the mass to go
    # since there will be some historisis 
    
    globals.fedMass += mass
    
    print("Fed " , mass , "g")
    print("Total fed mass: ", globals.fedMass)

# Compression function
def compress(compressTime):
    
    # Code to compress the sample for the specified time
    # Just turn on the output for the specified time
    
    print("Compressed for ", compressTime , " seconds")
    
# Heater function
def heat(temp, time):
    
    # Code for makin the heater work
    # I'm not sure if we need to preheat or anything, so for now we'll just turn on after we get to position
    # We'll need some amount of heater controll, and the thermocouple feedback
    
    print("Heated to " , temp , "deg for " , time , " seconds")
    
    
    
    