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

def avg_s(T,s_i,H):
    si=s_i
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

Th=1.5
Tl=1e-10
Hn=np.arange(2.0,-2.0,-0.01)
Hp=np.arange(-2.0,2.0,0.01)
avgshn=np.array([avg_s(Th,0.5,H) for H in Hn])
avgshp=np.array([avg_s(Th,-0.5,H) for H in Hp])
avgsln=np.array([avg_s(Tl,0.5,H) for H in Hn])
avgslp=np.array([avg_s(Tl,-0.5,H) for H in Hp])

maghn=M(avgshn)
maghp=M(avgshp)
magln=M(avgsln)
maglp=M(avgslp)

net_energy_hn=E(avgshn)
net_energy_hp=E(avgshp)
net_energy_ln=E(avgsln)
net_energy_lp=E(avgslp)


#plt.plot(Hn,maghn,label='hn')
plt.plot(Hn,magln,label='ln')
#plt.plot(Hp,maghp,label='hp')
plt.plot(Hp,maglp,label='lp')
plt.legend()

#plt.plot(temps,net_energy)

plt.show()