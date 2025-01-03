# Question:Add a ‘perfect’ step method to your code derived from the analytic solution
# un+1 = un cos(dt) + vn sin(dt) and vn+1 = vn cos(dt)+un sin(dt) 
# (Convince yourself that the Euler method would correspond to this in the small angle, i.e. small t,
# limit.) This is a ‘cheat’ as we know the analytic solution in this case, but using this for the steps
# and comparing the result to the literal analytic solution u = sin(t) and v = cos(t) should allow you
# to see the rounding errors without any method approximation errors. The global errors at the end of
# the solution should generally get worse as you make t smaller. Check your results are consistent
# with this.

import numpy as np
import matplotlib.pyplot as plt
T=1
N_array=[2,5,10,50,100,500,1000,1e4]
global_errors=[]
for N in N_array:
    dt=T/(N-1)
    N=int(N)
    t_array=np.linspace(0,T,N)
    u=[]
    v=[]
    un=0 #initial u
    vn=1 #initial v
    u.append(un)
    v.append(vn)
    for _ in range(1,N):

        next_u=un*np.cos(dt)+vn*np.sin(dt)
        next_v=vn*np.cos(dt)-un*np.sin(dt)

        u.append(next_u)
        v.append(next_v)
        un=next_u
        vn=next_v

    global_errors.append(abs(u[-1]-np.sin(T)))
    
plt.plot(N_array,global_errors,'.')
plt.xlabel('Timesteps N')
plt.ylabel('Global error')
plt.grid()
plt.show()