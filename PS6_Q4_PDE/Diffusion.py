# Question: consider a metal bar extending from (scaled) x = 0 to 1 held at a (scaled) temperature T = 0 by contact
# at the x = 0 end with a heat bath. At t = 0, the other end is moved into contact with a heat bath at
# temperature T = 1. We want to solve for the temperature u(t, x) within the rod.
# The heat diffuses through the rod so this is a diffusion equation problem. Assume everything is scaled so
# the diffusion coefficient can be assumed to be D = 1. The boundary conditions are fixed with u(t, 0) = 0
# and u(t, 1) = 1 and the initial condition is u(x, 0) = 0 everywhere except for the x = 1 boundary point
# where it is u(1, 0) = 1.
# Write code to solve these equations using the O(∆t)+O(h2) method described in the notes. Use 100 steps
# in x and choose a small enough ∆t, given the value of h. Make a plot of the solution as a function of
# x for several times, scaled by the square of the number of time steps. Specifically, plot the solution for
# t = 0.01, t = 0.09 and t = 0.25. By the time of the last of these, the solution should be getting close to
# the steady state solution (see below)

import numpy as np
import matplotlib.pyplot as plt

X=1
Nx=101
h=X/(Nx-1)
D=1


for t in [0.01,0.09,0.25]:
    T=np.concatenate([np.zeros(Nx-1),[1]]) #initial temperature
    T_inner=T[1:-1]
    #dt=0.5*(h**2/(2*D)) #let's be conservative i,e, 0.5 of the CFL
    dt=1.5*(h**2/(2*D)) #does not satisfy CFL

    
    Nt=int(t/dt)+1
    x_array=np.linspace(0,X,Nx)
    t_array=np.linspace(0,T,Nt)

    d=dt/(h**2)

    for _ in range(Nt):
        T_inner=(1-2*d)*T_inner+d*(T[:-2]+T[2:])
        T[1:-1]=T_inner
        T[0]=0
        T[-1]=1

    plt.plot(x_array,T,label=f'time={t}')

plt.xlabel('position')
plt.ylabel('temperature')
plt.legend()
plt.grid()
plt.show()







