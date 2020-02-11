# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:44:08 2020

@author: jammie

Torin's Class 6519
Spring 2020
The University of Colorado Boulder

Collaborators: Johnny Zhang, Rachel Rise, Alex Baughman
"""

import numpy as np
import matplotlib.pyplot as plt

#definitions
#S = salience
#A = Area of Interest
#Ex = Expectancy of viewing
#V = Value of viewing



#define object AOI
class AOI:

    """ Point class represents and manipulates x,y coords. """

    def __init__(self, S =0, Ex =0, V =0, EfA=0, EfB=0, EfC=0, EfD=0, name = 'a'):
        """ Create a new point at the origin """
        self.S = S
        self.Ex = Ex
        self.V = V
        self.name = name
        if EfA == 0:
            self.selfA = 0
        else:
            self.selfA = S - EfA + Ex + V
            
        if EfB == 0:
            self.selfB = 0
        else:
            self.selfB = S - EfB + Ex + V
            
        if EfC == 0:
            self.selfC = 0
        else:
            self.selfC = S - EfC + Ex + V
            
        if EfD == 0:
            self.selfD = 0
        else:
            self.selfD = S - EfD + Ex + V
            
    #interval function to stochastically determine which state comes next        
    def stochnext(self):
        tot = self.selfA + self.selfB + self.selfC + self.selfD
        x = np.random.random()*tot
        if x <= self.selfA:
            ne = A
        elif self.selfA < x <= self.selfA + self.selfB:
            ne = B
        elif self.selfA + self.selfB < x<= self.selfA + self.selfB + self.selfC:
            ne = C
        else:
            ne = D
        return ne
        

        
#intput data on our AOIs
A = AOI(2,4,2,0,1,1,5,'A')
B = AOI(3,2,1,1,0,3,6,'B')
C = AOI(1,3,1,1,3,0,4,'C')
D = AOI(2,1,5,5,6,4,0,'D')
    


state = A
states= [state.name]
t = [0]

for i in range (0,10):
    #how long are we in this state for?
    t.append(t[-1]+np.random.lognormal(0,0.5))
    #we are now inbetween
    states.append('between')
    #how long are we inbetween for?
    t.append(t[-1]+np.random.lognormal(0,0.5))
    #pick next state
    state = state.stochnext()
    states.append(state.name)

plt.step(t,states, where = 'post')

def montecarlo(fixations = 100, start = A):
    t = 0
    state = start
    myStates = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0
       }
    for i in range(0,fixations):
        t += np.random.lognormal(0,0.5)
        #how long are we inbetween for?
        tplus = np.random.lognormal(0,0.5)
        t+=tplus
        myStates[state.name] += tplus
        #pick next state
        state = state.stochnext()
        
    myStates = {k: v / t for k, v in myStates.items()}
    return myStates