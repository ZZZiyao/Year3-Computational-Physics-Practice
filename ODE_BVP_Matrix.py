# Try to solve the same BVP as in the ps using boundary value matrix method

import numpy as np
import matplotlib.pyplot as plt

T=1
N=4000
N=int(N)
dt=T/N
t_array=np.linspace(0,T,N+1)
u0=0
vN=5/6


def analytical_func_u(t):
    return t*(t**2+2)/6

def analytical_func_v(t):
    return (3*t**2+2)/6


def v_grad(u,t):#calculate v's derivative
    f=3*u-((t**3)/2)
    return f

def solve_u(b_u,L):
    #forward subsitution to solve u
    u=np.zeros(N)
    u[0]=b_u[0]/L[0][0] #this is u1
    for i in range(1,N):
        u[i]=(b_u[i]-np.sum([L[i][j]*u[j] for j in range(0,i)]))/L[i][i]

    return u

def solve_v(b_v,U):
    #backward subsitution to solve v
    v=np.zeros(N)
    v[N-1]=b_v[N-1]/U[N-1][N-1] #this is vN-1
    for i in range(N-2,-1,-1): #generate N-1 numbers from N-2 to 0
        v[i]=(b_v[i]-np.sum([U[i][j]*v[j] for j in range(i+1,N)]))/U[i][i]

    return v




L=np.zeros((N,N))
U=np.zeros((N,N))

#initialize L
for i in range(0,N): 
    L[i][i]=1
    if i>0:
        L[i][i-1]=-1

#initialize U
for i in range(0,N): 
    U[i][i]=-1
    if i<N-1:
        U[i][i+1]=1



#solving for L.u=b_u, U.v=b_v  can be solved by forward substitution
u=0.5*np.random.rand(N) #u1 to uN
v=5/6*np.random.rand(N) #v0 to vN-1

for _ in range(int(20)):

    v_dash=v_grad(u,t_array[1:]) #returns an array from v'1 to v'N
    u_dash=v #returns an array from u'0 to u'N-1

    b_v=np.concatenate([v_dash[:-1]*dt, [v_dash[-1]*dt-vN]])#initial b_v
    b_u=np.concatenate([[u0+u_dash[0]*dt],u_dash[1:]*dt])#initial u_v
    
    u=solve_u(b_u,L)
    v=solve_v(b_v,U)


    print(u[-1])



u=np.concatenate([[0],u])
v=np.concatenate([v,[5/6]])


plt.plot(t_array,u,label='u solved by matrix equation')
plt.plot(t_array,analytical_func_u(t_array),label='analytical u')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend()
plt.grid()
plt.show()
