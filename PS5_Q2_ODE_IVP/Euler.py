# Question:Write a program to use the Euler method with two variables to solve the (scaled) simple harmonic
# oscillator equation d2u/dt2 + u = 0 for u(t) from t = 0 to 1, for initial conditions u(0) = 0 and
# velocity v(0) = 1. You should compare your result to the analytic solution u = sin(t) and also
# to the (scaled) energy proportional to u^2 + v^2 which should be constant. Play around with the step size to see
# how it affects the accuracy of the solution, including trying both large and small step sizes. (You
# are unlikely to reach the computational rounding error limit even at small step sizes, assuming you
# work with a 64-bit floating point representation.)

import numpy as np
import matplotlib.pyplot as plt
T=1
N_array=[5,10,50,100,500,1000,1e4]
for N in N_array:
    N=int(N)
    dt=T/(N-1)
    t_array=np.linspace(0,T,N)
    u=[]
    v=[]
    un=0 #initial u
    vn=1 #initial v
    u.append(un)
    v.append(vn)
    for _ in range(1,N):
        next_u=un+vn*dt
        next_v=vn-un*dt
        u.append(next_u)
        v.append(next_v)
        un=next_u
        vn=next_v

    plt.plot(t_array,u,label=f'simulated with stepsize {dt}')
    
plt.plot(t_array,np.sin(t_array),label='analytical')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend()
plt.grid()
plt.show()


    

