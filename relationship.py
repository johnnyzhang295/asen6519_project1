import numpy as np

class AOI():
    def __init__(self, S, Ex, Ef, V):
        self.S = S
        self.Ex = Ex
        self.Ef = Ef
        self.V = V
        self.t = 0
    
    def fixate():
        #Return a random sample from log normal dist mu=0, sigma=.5
        return np.random.lognormal(0,.5)
        
        
        
class Observer():
    def __init__(self):
         self.currentAOI = None
         self.nextAOI = None
         
    def move(currentAOI, nextAOI):
        #Return a random sample from normal dist mu=.03, sigma=.003
        return np.random.normal(.03,.003)
        
        
A_Ef = {'B':1, 'C':1, 'D':5}
B_Ef = {'A':1, 'C':3, 'D':6}
C_Ef = {'A':1, 'B':3, 'D':4}
D_Ef = {'A':5, 'B':6, 'C':4}
