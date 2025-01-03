#Question: Try redoing part (a) but using the Runge-Kutta fourth-order method (RK4) instead of Euler. You
# should see much better agreement with the analytic solution, possibly dominated by rounding errors, which will look quite random.


import numpy as np
import matplotlib.pyplot as plt
T=1
N=100
N=int(N)
dt=T/(N-1)
t_array=np.linspace(0,T,N)


u=np.zeros(N)
v=np.zeros(N)
u[0]=0 #initial u
v[0]=1/3 #initial v

def v_grad(t):
    return t


for n in range(0,N-1):
    tn=t_array[n]
    fa_v=v_grad(tn)
    fb_v=v_grad(tn+dt/2)
    fc_v=v_grad(tn+dt/2)
    fd_v=v_grad(tn+dt)
    fa_u=v[n]
    fb_u=v[n]+fa_v*dt/2
    fc_u=v[n]+fb_v*dt/2
    fd_u=v[n]+fc_v*dt
    u[n+1]=u[n]+dt/6*(fa_u+2*fb_u+2*fc_u+fd_u)
    v[n+1]=v[n]+dt/6*(fa_v+2*fb_v+2*fc_v+fd_v)


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

plt.plot(t_array,abs(analytical_func(t_array)-u))

plt.xlabel('time')
plt.ylabel('error')

plt.grid()
plt.show()