# # Question: Finally, implement some or all of the fourth-order methods; HOT4, AB4, AM4 and RK4, again
# using the perfect method for the first few steps of AB4 and AM4. You should easily get to the
# rounding error limit; what approximate value of t gives this?


import numpy as np
import matplotlib.pyplot as plt
T=1
N_array=[1e2,3e2,5e2,8e2,1e3,1e4,2e4]




global_errors=[]

for N in N_array:
    print(N)
    N=int(N)
    dt=T/(N-1)

    t_array=np.linspace(0,T,N)
   
    u=np.zeros(N)
    v=np.zeros(N)
    u[0]=0
    v[0]=1
    for n in [0,1,2]:
        u[n+1]=u[n]*np.cos(dt)+v[n]*np.sin(dt)
        v[n+1]=v[n]*np.cos(dt)-u[n]*np.sin(dt) #now,0,1,2,3 in u and v arrays have values
 
    for n in range(3,N-1):
        u[n+1]=u[n]+1/24*(55*v[n]-59*v[n-1]+37*v[n-2]-9*v[n-3])*dt
        v[n+1]=v[n]+1/24*(-55*u[n]+59*u[n-1]-37*u[n-2]+9*u[n-3])*dt
    
    # plt.plot(t_array,u,'.',label='simulated')
    # plt.plot(t_array,np.sin(t_array),label='analytical')
    # plt.legend()
    # plt.grid()
    # plt.xlabel('time')
    # plt.ylabel('displacement')
    # plt.show()
    error=abs(u[-1]-np.sin(T))
    global_errors.append(error)
    
    
plt.plot(N_array,global_errors,'o-')
plt.xlabel('Timesteps N')
plt.ylabel('global error')
plt.grid()
plt.show()