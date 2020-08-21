# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:53:26 2020

@author: chans
"""
def set_to(axis,value):
    with open("globals.txt", "r") as file:
        data = file.read()
        parsed_data = data.split()
        
        x = parsed_data[2]
        r = parsed_data[5]
        z = parsed_data[8]
        
    if axis == "x":
        x = value
        
    elif axis == "r":
        r = value
        
    elif axis == "z":
        z = value

    with open("globals.txt", "w") as file:
        file.write("x = %s\n"%x)
        file.write("r = %s\n"%r)
        file.write("z = %s"%z)

def get(axis):
    with open("globals.txt", "r") as file:
        data = file.read()
        parsed_data = data.split()
        
        x = parsed_data[2]
        r = parsed_data[5]
        z = parsed_data[8]
        
    if axis == "x":
        return x
    
    elif axis == "r":
        return r
    
    elif axis == "z":
        return z