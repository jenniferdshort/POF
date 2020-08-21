# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:50:51 2020

@author: chans
"""
import pandas as pd
import sys
import layer

excel_file = 'POF_recipe_test.xlsx'
data = pd.read_excel(excel_file) #Reads file and makes it a dataframe

print(data)

#layer_num = data['Layer #'][0]
#print()
#print(layer_num)
#print()
#
#data.drop(index = 19, inplace = True) #removes last row from dataframe
#print(data)

for i in range(len(data)):
    try:
        layerNum = data['Layer #'][i]
        layerMass = data['Mass (g)'][i]
        layerAngle = data['Fiber Orientation'][i]
        
        print("Layer #%d, Mass:%d, Orientation:%d"%(layerNum, layerMass, layerAngle))
        
        layer.make_layer(layerMass, layerAngle)
    except:
        print("Error interpreting recipe")
        sys.exit()