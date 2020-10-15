# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:54:33 2020

@author: chans
"""
import RPi.GPIO as GPIO
import time
import peripherals

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#################TESTING EACH PERIPHERAL#################
#peripherals.auger_pulse("long")
#time.sleep(3)
#peripherals.auger_pulse("short")
#time.sleep(1)

peripherals.heat_on()
time.sleep(60)
peripherals.heat_off()
time.sleep(1)

#peripherals.compress()
#peripherals.compress()