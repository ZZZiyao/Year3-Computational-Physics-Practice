#Adopt this question from ps7 Q1, where we are required to minimized a 2D function by Newton's method by hand

import numpy as np
import matplotlib.pyplot as plt

def func(x,y,a=0.1):
    return -np.exp(-x**2-a*y**2)

def H(x,y,a=0.1):
    H=np.zeros((2,2))
    H[0,0]=4*x**2-2
    H[0,1]=H[1,0]=4*a*x*y
    H[1,1]=a*a**2*y**2-2*a
    return H*func(x,y,a)

def grad_f(x,y,a=0.1):
    grad=np.zeros(2)
    grad[0]=-2*x
    grad[1]=-2*a*y
    return grad*func(x,y,a)

x0=0.2
y0=0.2
xn=np.array([x0,y0])

for i in range(int(1e3)):
    next_xn=xn-np.dot(np.linalg.inv(H(xn[0],xn[1])),grad_f(xn[0],xn[1]))
    print(next_xn)
    if abs(sum((next_xn))-sum((xn)))<1e-7:
        print(f'solution is {next_xn}, converged in {i} iterations')
        break
    xn=next_xn
else:
    print('cannot converge')



    