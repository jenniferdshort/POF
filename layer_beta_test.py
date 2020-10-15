# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:31:55 2020

@author: chans
"""
import move

def first_layer(mass, angle):
    move.x("deposition")
    move.r(angle)
    move.z("down")
    #zero the scale
    #dispense media using scale and motor
    move.r(0)
    move.z("up")
    move.x("heating")
    #heat for some amount of time

def make_layer(mass, angle):
    move.x("deposition") #select station from deposition, heating, compression, or end
    move.r(angle) #select plate angle (not done yet due to still unknown scaling factor)
    move.z("down") #select up or down
    #zero the scale
    #dispense media using scale and motor
    move.z("up")
    move.r(0)
    move.x("heating")
    #heat for some amount of time
    move.x("compression")
    #actuate pneumatic piston
    move.x("heating")
    #heat for some amount of time
    
def last_layer(mass, angle):
    move.x("deposition") #select station from deposition, heating, compression, or end
    move.r(angle) #select plate angle (not done yet due to still unknown scaling factor)
    move.z("down") #select up or down
    #zero the scale
    #dispense media using scale and motor
    move.r(0)
    move.z("up")
    move.x("heating")
    #heat for some amount of time
    move.x("compression")
    #actuate pneumatic piston
    move.x("end")