#Question: Write a function to solve this equation using a standard two-variable Euler initial value method
# using N = 100 steps. The initial conditions are x(0) = 0 and v(0) = 1/3. Compare your results to
# the analytic solution.


import numpy as np
import matplotlib.pyplot as plt
T=1
N_array=[100]
for N in N_array:
    N=int(N)
    dt=T/(N-1)
    t_array=np.linspace(0,T,N)
    u=np.zeros(N)
    v=np.zeros(N)
    u[0]=0 #initial u
    v[0]=1/3 #initial v
    
    for n in range(0,N-1):
        u[n+1]=u[n]+v[n]*dt
        v[n+1]=v[n]+t_array[n]*dt
 

    plt.plot(t_array,u,label='simulated u')
    plt.plot(t_array,v,label='simulated v')

   

def analytical_func(t):
    return t*(t**2+2)/6

def analytical_func_v(t):
    return (3*t**2+2)/6

plt.plot(t_array,analytical_func(t_array),label='analytical u')
plt.plot(t_array,analytical_func_v(t_array),label='analytical v')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend()
plt.grid()
plt.show()