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
A = AOI(2,4,2,0,1,1,4,'A')
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
    t.append(t[-1]+np.random.normal(0.03,0.003))
    #pick next state
    state = state.stochnext()
    states.append(state.name)

#plt.step(t,states, where = 'post')

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
        #how long are we inbetween for?
        t += np.random.normal(0.03,0.003)
        #how long are we at this state for?
        tplus = np.random.lognormal(0,0.5)
        t+=tplus
        myStates[state.name] += tplus
        #pick next state
        state = state.stochnext()
        
    myStates = {k: v / t for k, v in myStates.items()}
    return myStates

count = 0
for i in range(0,1000):
    count +=1
    myStates = montecarlo()
    try:
        mytotalStates = {k: v+myStates[k] for k, v in mytotalStates.items()}
    except:
        mytotalStates = myStates

mytotalStates = {k: v / count for k, v in mytotalStates.items()}

print(mytotalStates)

def WindTime(start = A):
    t = np.random.lognormal(0,0.5) #how much time did we spend on starting state
    state = start    
    noticed = False
    while not noticed:
        t+=np.random.normal(0.03,0.003) #time spent inbetween
        state = state.stochnext() #this is where we go next
        tplus = np.random.lognormal(0,0.5) #this is how long we spend there
        if state == D and t > 10 and np.random.random()>0.8:
            noticed= True
            t += np.random.random()*tplus
            break
        elif state == D and t + tplus > 10 and np.random.random()>0.8:
            noticed= True
            t = 10 + (t+ tplus - 10)*np.random.random()
            break
        else:
            t+=tplus
            

        if t>1000:
            break
        
    return t


times = []
for i in range(0,1000):
    times.append(WindTime(A))
m = round(np.median(times),2)
CI = [round(np.percentile(times,5),2), round(np.percentile(times,95),2)]
plt.hist(times)
title = 'mean: ' + str(m) + '. 5th - 95th percentile: '+ str(CI) + '.'
plt.title(title)

