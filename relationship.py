import numpy as np
import string
import matplotlib.pyplot as plt

class AOI():
    def __init__(self, ID, S, Ex, Ef, V):
        self.ID = ID
        self.S = S
        self.Ex = Ex
        self.Ef = Ef
        self.V = V
        self.t = 0
    
    def view_AOI_time(self):
        #Return a random sample from log normal dist mu=0, sigma=.5
        time = np.random.lognormal(0,.5)
        self.t += time
        return time
               
class Observer():
    def __init__(self):
         self.currentAOI = None
         self.nextAOI = None
         self.betweenTime = 0
         
    def eye_movement_time(self):
        #Return a random sample from normal dist mu=.03, sigma=.003
        time = np.random.normal(.03,.003)
        self.betweenTime += time
        return time
                
def p_abs(currentAOI, nextAOI):
    #print(nextAOI.S, nextAOI.Ef[currentAOI.ID], nextAOI.Ex, nextAOI.V)
    return nextAOI.S - nextAOI.Ef[currentAOI.ID] + nextAOI.Ex + nextAOI.V

def p(currentAOI, nextAOI, AOI_list):
    if currentAOI.ID == nextAOI.ID:
        return 0
    
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

iterations = 100
mark_watney = Observer()
monte_carlo_iterations = 1000
time = AOI_A.view_AOI_time()
for j in range (0,monte_carlo_iterations):
    current = AOI_A
    for i in range(0,iterations):
        #global current
        time += mark_watney.eye_movement_time()

        nextAOI = current
        #print(current.ID)
        #print(goto_A, goto_B, goto_C, goto_D)
        while current.ID == nextAOI.ID:
            goto_A = p(current, AOI_A, AOI_list)
            goto_B = p(current, AOI_B, AOI_list)
            goto_C = p(current, AOI_C, AOI_list)
            goto_D = p(current, AOI_D, AOI_list)
            random_num = np.random.random() # 0-1.0
            if random_num < goto_D:
                nextAOI = AOI_D
            elif random_num < goto_B + goto_D:
                nextAOI = AOI_B
            elif random_num < goto_C + goto_B + goto_D:
                nextAOI = AOI_C
            else:
                nextAOI = AOI_A

        #print(nextAOI.ID)
        time += nextAOI.view_AOI_time()
        current=nextAOI

data = [AOI_A.t/monte_carlo_iterations, AOI_B.t/monte_carlo_iterations, AOI_C.t/monte_carlo_iterations, 
        AOI_D.t/monte_carlo_iterations, mark_watney.betweenTime/monte_carlo_iterations]
plt.scatter(['A','B','C','D','Between'],data,s=80)
plt.title("100 Fixations for 1000 Monte Carlo Simulations")
plt.savefig("problem2.png")
plt.show()