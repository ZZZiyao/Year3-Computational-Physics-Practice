#Adopt this question from ps7 Q1, where we are required to minimized a 2D function by Newton's method by hand

import numpy as np
import matplotlib.pyplot as plt

def func(x,y,a=0.1):
    return -np.exp(-x**2-a*y**2)

def grad_f(x,y,a=0.1):
    grad=np.zeros(2)
    grad[0]=-2*x
    grad[1]=-2*a*y
    return grad*func(x,y,a)

def outer_product(vec1,vec2):
    M=np.zeros((2,2))
    for i in range(0,2):
        for j in range(0,2):
            M[i][j]=vec1[i]*vec2[j]
    return M

def update_G(G,gamma,delta):
    outer_p_d=outer_product(delta,delta)
    outer_p_g=outer_product(gamma,gamma)
    second_term=outer_p_d/(np.dot(gamma,delta))
    three1=np.dot(np.dot(G,outer_p_g),G)
    three2=np.dot(np.dot(gamma,G),gamma)
    return G+second_term-three1/three2


x0=0.1
y0=0.5
xn=np.array([x0,y0])
gradn=grad_f(xn[0],xn[1])

Gn=np.eye(2,2)
alpha=0.5

for i in range(int(1e3)):


    next_xn=xn-alpha*np.dot(Gn,gradn)
    next_grad=grad_f(next_xn[0],next_xn[1])
    gamma=next_grad-gradn
    delta=next_xn-xn
    next_G=update_G(Gn,gamma,delta)


    print(next_xn)

    if abs(sum((next_xn))-sum((xn)))<1e-9:
        print(f'solution is {next_xn}, converged in {i} iterations')
        break


    
    xn=next_xn
    gradn=next_grad
    Gn=next_G
    
    
else:
    print('cannot converge')