#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:13:17 2022

@author: paul.carre
"""

import sys

print("Nom du programme : ", sys.argv[0])
print("Nombre d'arguments : ", len(sys.argv)-1)
print("Les arguments sont : ")
for arg in sys.argv[1:] :
    print(arg)