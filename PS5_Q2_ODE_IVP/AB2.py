# Question: Now add several second-order methods to your code and again compare to the analytic solution.
# Try some or all of HOT2, AB2, AM2 (again not using predictor-corrector but directly solved, as this
# is a linear system) and RK2 with alpha = 1/2. How well do they all do? Can you reach the rounding
# error limit, where the global error generally increases if you make t any smaller?
# You will need to do a first step using some other method before you can use the AB2 method;
# cheat by using the perfect step solution for that single first step so as to see the ‘pure’ AB2 method
# accuracy


import numpy as np
import matplotlib.pyplot as plt
T=1
N_array=[1e4,1e5,1e6]




global_errors=[]

for N in N_array:
    print(N)
    N=int(N)
    dt=T/(N-1)

    t_array=np.linspace(0,T,N)

    u=[]
    v=[]
    u_pre=0 #uses for u-1
    v_pre=1 #uses for v-1
    u.append(u_pre)
    v.append(v_pre)

    un=np.sin(dt)
    vn=np.cos(dt)
    u.append(un)
    v.append(vn)

    for _ in range(0,N-2):
        next_u=un+0.5*(3*vn-v_pre)*dt
        next_v=vn+0.5*(3*(-un)-(-u_pre))*dt
        u.append(next_u)
        v.append(next_v)
        u_pre=un
        v_pre=vn
        un=next_u
        vn=next_v
    
    # plt.plot(t_array,u,'.',label='simulated')
    # plt.plot(t_array,np.sin(t_array),label='analytical')
    # plt.legend()
    # plt.grid()
    # plt.xlabel('time')
    # plt.ylabel('displacement')
    # plt.show()
    error=abs(u[-1]-np.sin(T))
    global_errors.append(error)
    
    
plt.plot(N_array,global_errors,'.')
plt.xlabel('Timesteps N')
plt.ylabel('global error')
plt.grid()
plt.show()