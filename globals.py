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
    global rotationLocal
    rotationLocal = 0
    