# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:42:55 2019

@author: Teal
"""

# Tests interfacing with YAML

import yaml


with open("example_runfile.yml") as file:

    prog = yaml.load(file, Loader=yaml.FullLoader)
    #prog = file.read()
    #prog = prog.replace('\n\n', '\n---\n')

    print(prog)
    
