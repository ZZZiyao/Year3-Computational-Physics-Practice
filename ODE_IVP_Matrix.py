# Try to solve the same IVP as in the ps using initial value matrix method

import numpy as np
import matplotlib.pyplot as plt

T=1
N=99
N=int(N)
dt=T/N
t_array=np.linspace(0,T,N+1)

def analytical_func_u(t):
    return t*(t**2+2)/6

def analytical_func_v(t):
    return (3*t**2+2)/6


L=np.zeros((N,N))

#initialize L
for i in range(0,N): 
    L[i][i]=1
    if i>0:
        L[i][i-1]=-1

def f_value(u,t):#calculate v's derivative
    f=3*u-((t**3)/2)
    return f


#solving for L.u=b_u, L.v=b_v  can be solved by forward substitution
def solve_for_uv(u0=0,v0=1/3):

    b_u=np.zeros(N)
    b_v=np.zeros(N)

    u=np.zeros(N)
    v=np.zeros(N)

    b_u[0]=u0+v0*dt
    b_v[0]=v0+f_value(b_u[0],t_array[0]) #first rows

    u[0]=b_u[0]/L[0][0] #this is u1
    v[0]=b_v[0]/L[0][0]#this is v1

    for i in range(1,N):
        b_u[i]=v[i-1]*dt
        u[i]=(b_u[i]-np.sum([L[i][j]*u[j] for j in range(0,i)]))/L[i][i]
        b_v[i]=f_value(u[i-1],t_array[i])*dt
        v[i]=(b_v[i]-np.sum([L[i][j]*v[j] for j in range(0,i)]))/L[i][i]



    return u,v




u=solve_for_uv()[0]
v=solve_for_uv()[1]

u=np.concatenate([[0],u])
v=np.concatenate([[1/3],v])


plt.plot(t_array,u,label='u solved by matrix equation')
plt.plot(t_array,analytical_func_u(t_array),label='analytical u')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend()
plt.grid()
plt.show()
