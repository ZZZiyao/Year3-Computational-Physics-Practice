# # Question: Finally, implement some or all of the fourth-order methods; HOT4, AB4, AM4 and RK4, again
# using the perfect method for the first few steps of AB4 and AM4. You should easily get to the
# rounding error limit; what approximate value of t gives this?


import numpy as np
import matplotlib.pyplot as plt
T=1
N_array=[1e2,5e2,1e3]



global_errors=[]

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
        fa_u=vn
        fa_v=-un
        fb_u=vn+fa_v*dt/2
        fb_v=-(un+fa_u*dt/2)
        fc_u=vn+fb_v*dt/2
        fc_v=-(un+fb_u*dt/2)
        fd_u=vn+fc_v*dt
        fd_v=-(un+fc_u*dt)

        next_u=un+dt/6*(fa_u+2*fb_u+2*fc_u+fd_u)
        next_v=vn+dt/6*(fa_v+2*fb_v+2*fc_v+fd_v)
        un=next_u
        vn=next_v
        u.append(un)
        v.append(vn)
    
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