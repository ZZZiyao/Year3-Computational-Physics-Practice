#Use rejection sampling to generate data follow normal distribution

import numpy as np
import matplotlib.pyplot as plt

def prob_y(y,sig=1,mu=0):
    A=1/(np.sqrt(2*np.pi)*sig)
    power=-0.5*((y-mu)/sig)**2
    return A*np.exp(power)

C=1

y_acc=[]

for _ in range(int(1e7)):
    yi=np.random.uniform(-100,100)
    pyi=prob_y(yi)
    pi=np.random.uniform(0,C)
    if pyi>pi:
        y_acc.append(yi)

plt.hist(y_acc,bins=1000)
plt.show()