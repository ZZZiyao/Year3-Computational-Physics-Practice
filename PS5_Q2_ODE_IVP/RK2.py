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
alpha=0.5
for N in N_array:
    print(N)
    N=int(N)
    dt=T/(N-1)

    t_array=np.linspace(0,T,N)

    u=[]
    v=[]
    un=0
    vn=1
    u.append(un)
    v.append(vn)

    for _ in range(0,N-1):
        u_alpha=un+vn*alpha*dt
        v_alpha=vn+(-un)*alpha*dt
        next_u=un+1/(2*alpha)*((2*alpha-1)*vn+v_alpha)*dt
        next_v=vn+1/(2*alpha)*((2*alpha-1)*(-un)+(-u_alpha))*dt
        un=next_u
        vn=next_v
        u.append(un)
        v.append(vn)
    
    plt.plot(t_array,u,'.',label='simulated')
    plt.plot(t_array,np.sin(t_array),label='analytical')
    plt.legend()
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('displacement')
    plt.show()
    error=abs(u[-1]-np.sin(T))
    global_errors.append(error)
    
    
plt.plot(N_array,global_errors,'.')
plt.xlabel('Timesteps N')
plt.ylabel('global error')
plt.grid()
plt.show()