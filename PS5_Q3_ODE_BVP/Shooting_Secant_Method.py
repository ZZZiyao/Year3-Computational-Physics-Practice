# Question: Treat this as a boundary problem with x(0) = 0 as before but now use x'(1) = 1/2 as the second
# condition, instead of the initial condition. Use your Euler function in a shooting method
# to solve for x(t) and compare with the analytic method. You will need to choose an appropriate
# method to do the root-finding for the t = 1 boundary condition. 

import numpy as np
import matplotlib.pyplot as plt


T=1
N=100
N=int(N)
dt=T/(N-1)
t_array=np.linspace(0,T,N)


def v_end(v0): #the root finding problem is v_end(v0)-vN=0
    u=np.zeros(N)
    v=np.zeros(N)
    u[0]=0 #initial u
    v[0]=v0 #initial v

    for n in range(0,N-1):
        u[n+1]=u[n]+v[n]*dt
        v[n+1]=v[n]+t_array[n]*dt

    value=u[-1]-0.5

    return(value)

print(v_end(1/3))

def solve_u(v0): #solve the ode
    u=np.zeros(N)
    v=np.zeros(N)
    u[0]=0 #initial u
    v[0]=v0 #initial v

    for n in range(0,N-1):
        u[n+1]=u[n]+v[n]*dt
        v[n+1]=v[n]+t_array[n]*dt

    return u


vi=10000*np.random.rand()
v_00=10*np.random.rand()
print(vi,v_00)
print(v_end(vi),v_end(v_00))

for i in range(int(1e7)):

    next_vi=vi-v_end(vi)*((vi-v_00)/(v_end(vi)-v_end(v_00)))
    
    
    #print(v_end(next_vi))
    print(f'update v is {next_vi}')

    error=abs(next_vi-vi)/vi

    #print(f'error is {error}')

    if error<1e-7:
        print(f'converged to {next_vi} in {i} iterations, now u end is {v_end(next_vi)+0.5}')
        break

    v_00=vi
    vi=next_vi

else:
    print('cannot converge')


plt.plot(t_array,solve_u(next_vi),label='simulated with N=100')


def analytical_func(t):
    return t*(t**2+2)/6


plt.plot(t_array,analytical_func(t_array),label='analytical')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend()
plt.grid()
plt.show()