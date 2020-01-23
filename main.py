# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:38:17 2019

@author: Teal
"""

# Imports
import moveFunctions as move  # Functions for axis movement
import globals # Function for storing global variables
import sys # Imports a large library of system functions

# Global variables
#global.py



# Function for deposition 
def deposite(orientation, mass):
    
    print("***** Deposition Step *****")
    # Pads the length of the mass array, such that mass can be defined once instead of once per rotaiton
    while len(orientation) > len(mass):
        mass.append(mass[-1])
    
    # Move to initial location and angle
    move.rotate(0)
    move.x("feeder")

    # For each deposition required, perform feed and rotation
    # Using "float()" command to convert the strings to numbers
    # Using try and except to find errors
    
    try: 
        for stepNum, angle in enumerate(orientation):
            move.rotate(float(angle))
            move.feed(float(mass[stepNum]))
    except:
        print("Error in reading feeder data, skipping step")
    
# Function for deposition 
def heat(temp, time, prevStep, nextStep):
    
    print("***** Heater Step *****")
    # Moves to staging area on left or right of heater, depending on previous step
    # Move to near (but not under) heater, as function of where current position is
    # turn on heater with PID temperature control
    # Wait for temp to reach
    # Move under heater for specified time
    # Move away from heater towards next step
    
    move.rotate(0)
    move.x("heater")
    
    try:
        move.heat(float(temp), float(time))
    except:
        print("Error in reading heating data, skipping step")
    
def compress(compressTime):
    
    print("***** Compression Step *****")
    
    # Move to compression platform
    # Assure correct orientation of platform
    # Perform compression
    
    move.rotate(0)
    move.x("compress")
    
    try:
        move.compress(float(compressTime))
    except:
        print("Error in reading compression data, skipping step")

def readDataFile(fileName):
    # Opens files, and reads contents into list format
    # Checks if file name is valid
    try: inputFile = open(fileName)
    except FileNotFoundError: 
        sys.exit("Error with file name")
    except: print("Unknown file error")
    
    
    rawInput = inputFile.readlines()
    
    inputFile.close()   #Closes the input file when done with it
    
    rawInput = [s.strip("\n") for s in rawInput] # strips out newline char
    rawInput = [s.replace(" ","") for s in rawInput] # Removes all spaces
    

    inputData = [] # Initializes input data as list
    # Iteratively reads each line, and splits by the ':' char to make a 2d list array
    for line in rawInput:
        
        line = line.split(";") #splits by ";" to make easier to deal with
        inputData.append(line)
      
    return inputData


def main():
     
    # Calls the function to read the data file, switch to change recipes 
    inputData = readDataFile("testInputFileTXT.txt")
    
    
    # Iteratively reads each line in input data, and performs the desired task
    # stepNum is iterator, so know what step we're on as per
    # https://stackoverflow.com/questions/3162271/get-loop-count-inside-a-python-for-loop
    for stepNum, step in enumerate(inputData):
        
        print(step)
        
        if "Deposition" in step:
            
            # Extracts mass as list
            mass = step[step.index("Mass")+1]
            mass = mass.split(',')

            # Extracts orientation as list
            orientation = step[step.index("Orientation")+1]
            orientation = orientation.split(',')
            
            # Calls deposition function
            deposite(orientation, mass)
            
        elif "Heater" in step:
            
            # Extracts temp as a number
            temp = step[step.index("Temp")+1]
            
            # Extracts time as a number
            time = step[step.index("Time")+1]
            
            prevStep = inputData[stepNum-1][1] # finds previous step
            
            # Finds next step, if it exists
            if stepNum < len(inputData):
                nextStep = inputData[stepNum+1][1]
            else: 
                nextStep = -1
            
            # Calls heater function            
            heat(temp, time, prevStep, nextStep)
            
        elif "Compress" in step:
            
            # Extracts compression time as time in seconds
            compressTime = step[(step.index("Time")+1)]
            
            compress(compressTime)
        
        # If nothing is readable, print error
        else:
            print("Error in figuring out what operation in step: ", stepNum+1)
            
    
    print("Program End")

            


# Reason for doing this: https://stackoverflow.com/questions/419163/what-does-if-name-main-do     
if __name__ == "__main__":
    globals.initialize()
    
    main()