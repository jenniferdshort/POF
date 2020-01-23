# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:28:40 2020

@author: Teal
"""

# Using global variables stored as described in this article
# https://instructobit.com/tutorial/108/How-to-share-global-variables-between-files-in-Python

def initialize():
    
    # Stores step number for x axis
    global xAxisLocal
    xAxisLocal = 0
    
    # Stores step number for rotation axis
    global rotateAxisLocal
    rotateAxisLocal = 0
    
    # Stores step number for z axis
    global zAxisLocal
    zAxisLocal = 0
    
    # Stores total mass fed
    global fedMass
    fedMass = float(0)
    