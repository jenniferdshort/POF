# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:31:55 2020

@author: chans
"""
import move
import peripherals
import time

def make_layer(mass, angle):
    move.x("deposition") #select station from deposition, heating, compression, or end
   
    move.r(angle) #select plate angle (not done yet due to still unknown scaling factor)

    peripherals.auger_pulse("long")
    time.sleep(3)
    peripherals.auger_pulse("short")
    time.sleep(3)
    
    move.r(0)
    
    peripherals.heat_on()
    
    move.x("heating")
    time.sleep(30)
    peripherals.heat_off()
    
    move.x("compression")
    time.sleep(0.1)
    
    time.sleep(5)
    time.sleep(0.1)
    
    peripherals.heat_on()
    
    move.x("heating")
    time.sleep(10)
    
    peripherals.heat_off()