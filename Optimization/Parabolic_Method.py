#Adopt this question from ps7 Q1, where we are required to minimized a 2D function by Newton's method by hand

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.exp(-x)+(x-1)**2

def lagrange3(x0,x1,x2):
    y0=func(x0)
    y1=func(x1)
    y2=func(x2)

    nume=(x2**2-x1**2)*y0+(x0**2-x2**2)*y1+(x1**2-x0**2)*y2
    deno=(x2-x1)*y0+(x0-x2)*y1+(x1-x0)*y2
    return 0.5*nume/deno



x=[0,0.7,2]

for _ in range(int(1e3)):
    y0=func(x[0])
    y1=func(x[1])
    y2=func(x[2])
    x3=lagrange3(x[0],x[1],x[2])
    x.append(x3)
    y3=func(x3)
    y=[y0,y1,y2,y3]
    index=y.index(max(y))
    y.remove(y[index])
    x.remove(x[index])
    print(x)







    
