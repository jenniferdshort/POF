# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:38:17 2019

@author: Teal
"""

# Testing some array reading/writing

instructionList = [['Station', 'Deposition', 'Mass','25.1, 25.2','Orientation', '90,0'],
            ['Station', 'Heater', 'Temp', '200','Time', '10'],
            ['Station', 'Compress', 'Time','5'],
            ['Station', 'Deposition', 'Mass','25.3','Orientation', '45,-45']]


# Function for deposition 
def deposite(orientation, mass):
    
    print("Deposition Step")
    # Pads the length of the mass array, such that mass can be defined once instead of once per rotaiton
    while len(orientation) > len(mass):
        mass.append(mass[-1])
        
    # Orient to orientation[0]
    # Move to location of deposition 
    # Deposite until mass[0] achieved
    # Repeat
    
# Function for deposition 
def heat(temp, time, prevStep, nextStep):
    
    print("Heater Step")
    # Moves to staging area on left or right of heater, depending on previous step
    # Move to near (but not under) heater, as function of where current position is
    # turn on heater with PID temperature control
    # Wait for temp to reach
    # Move under heater for specified time
    # Move away from heater towards next step


def main():  

    for stepNum, step in enumerate(instructionList):
        #print(step)
        
        if "Deposition" in step:
            mass = step[step.index("Mass")+1]
            mass = mass.split(',')
    
            orientation = step[step.index("Orientation")+1]
            orientation = orientation.split(',')
            
            deposite(orientation, mass)
        
        if "Heater" in step:
            temp = step[step.index("Temp")+1]
            time = step[step.index("Time")+1]
            
            prevStep = instructionList[stepNum-1][1] # finds previous step
            
            # Finds next step, if it exists
            if stepNum < len(instructionList):
                nextStep = instructionList[stepNum+1][1]
            else: 
                nextStep = -1
            
            #print("Prev step", prevStep)
            #print("Next step", nextStep)
                
            
            heat(temp, time, prevStep, nextStep)

# Reason for doing this: https://stackoverflow.com/questions/419163/what-does-if-name-main-do     
if __name__ == "__main__":   
    main()