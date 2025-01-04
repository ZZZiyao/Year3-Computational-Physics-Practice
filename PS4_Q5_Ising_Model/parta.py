import matplotlib.pyplot as plt
import numpy as np
import math
import random as rnd

N = 1.0
mu = 1.0
kb = 1.0
Tc = 1.0
Hc=1
iterations = 1000

def avg_s(T,H=0):
    si=-0.1
    for _ in range(int(1e3)):
        si_new=np.tanh((Tc/T)*(H/Hc+si))
        if abs(si_new-si)<1e-5:
            break
        si=si_new

    return si_new

def M(s):
    return mu*N*s

def E(s,H=0):
    return -N*kb*Tc*(H/Hc+s)*s

def C(E,T):
    c=[]
    for i in range(len(E)-1):
        heat_c=(E[i+1]-E[i])/(T[i+1]-T[i])
        c.append(heat_c)

    return c

temps = np.arange(0.01,2.0,0.01)
avgs=np.array([avg_s(temp) for temp in temps])
mag=M(avgs)
net_energy=E(avgs)
heat_capa=C(net_energy,temps)

#plt.plot(temps,mag)
#plt.plot(temps,net_energy)
plt.plot(temps[1:],heat_capa,'.')

plt.show()







