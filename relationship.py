import numpy as np
import string
import matplotlib.pyplot as plt
matplotlib.rcParams['interactive'] == True

class AOI():
    def __init__(self, ID, S, Ex, Ef, V):
        self.ID = ID
        self.S = S
        self.Ex = Ex
        self.Ef = Ef
        self.V = V
        self.t = 0
    
    def view_AOI_time():
        #Return a random sample from log normal dist mu=0, sigma=.5
        time = np.random.lognormal(0,.5)
        self.t += time
        return time
               
class Observer():
    def __init__(self):
         self.currentAOI = None
         self.nextAOI = None
         self.betweenTime = 0
         
    def eye_movement_time():
        #Return a random sample from normal dist mu=.03, sigma=.003
        time = np.random.normal(.03,.003)
        self.betweenTime += time
        return time
                
def p_abs(currentAOI, nextAOI):
    return nextAOI.S - nextAOI.Ef[currentAOI.ID] + nextAOI.Ex + nextAOI.V

def p(currentAOI, nextAOI, AOI_list):
    numerator = p_abs(currentAOI, nextAOI)
    denominator = 0

    for AOI in AOI_list:
        denominator += p_abs(currentAOI, AOI)

    return numerator/denominator


A_Ef = {'A':0,'B':1,'C':1,'D':5}
B_Ef = {'A':1,'B':0,'C':3,'D':6}
C_Ef = {'A':1,'B':3,'C':0,'D':4}
D_Ef = {'A':5,'B':6,'C':4,'D':0}

AOI_A = AOI('A',2,4,A_Ef,2)
AOI_B = AOI('B',3,2,B_Ef,1)
AOI_C = AOI('C',1,3,C_Ef,1)
AOI_D = AOI('D',2,1,D_Ef,5)

AOI_list = [AOI_A, AOI_B, AOI_C, AOI_D]

iterations = 10
mark_watney = Observer()


time = AOI_A.view_AOI_time()
current = AOI_A
for i in range(0,iterations):
    #global current
    time += mark_watney.eye_movement_time()
    nextAOI_index = np.argmax([p(current, AOI_A, AOI_list),
                    p(current, AOI_B, AOI_list),
                    p(current, AOI_C, AOI_list),
                    p(current, AOI_D, AOI_list)])

    current = AOI_list[nextAOI_index]
    time += current.view_AOI_time()

data = [AOI_A.time, AOI_B.time, AOI_C.time, AOI_D.time, mark_watney.betweenTime]
plt.hist(data, 1)
plt.show()
