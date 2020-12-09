# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:29:22 2020

@author: Jack Powers
"""
import numpy as np
import matplotlib.pyplot as plt
import random

def two_dQC (atoms, frequancy, phase, n_rotation):
    x = []
    y = [[]]
    for i in range(atoms):
        l = [i for j in range(atoms)]
        x.append(i)
        y[0].append(l)
    
    
                
    return  x, y


atoms = 100
frequency = random.random() * 50 + 10
phase = random.random() * np.pi
n_rotation = random.randint(10, 20)
print(frequency, phase, n_rotation)


twoDQC = two_dQC(atoms, frequency, phase, n_rotation)

for i in range(0, atoms):
    plt.plot(twoDQC[0], twoDQC[1][0][i], 'ob')

