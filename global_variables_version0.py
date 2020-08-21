# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:25:10 2020

@author: chans
"""
x = 0
r = 0
z = 0

def set_to(axis, setting):
    global x
    global r
    global z
    
    if axis == "x":
        x = setting
        return x
        
    elif axis == "r":
        r = setting
        return r
        
    elif axis == "z":
        z = setting
        return z
    
def get(axis):
    global x
    global r
    global z
    
    if axis == "x":
        return x
        
    elif axis == "r":
        return r
        
    elif axis == "z":
        return z