# Question: Without deleting your Euler code, add the implicit Euler method. As this is a linear system, you
# can solve the resulting equations for un+1 and vn+1 directly and so do not need to use a predictorcorrector. This is also a first-order method so a comparison to the Euler method should show a
# similar accuracy.

import numpy as np
import matplotlib.pyplot as plt
T=1
N_array=[5,10,50,100,500,1000,1e4]


I=np.eye(2)
A=[[0,1],
   [-1,0]] 


for N in N_array:

    N=int(N)
    dt=T/(N-1)

    #calculating update matrix G_inver
    G=I-np.dot(A,dt)
    G_inver=np.zeros((2,2))
    det_G=(G[1,1]*G[0,0])-(G[0,1]*G[1,0])
    G_inver[0,0]=G[1,1]
    G_inver[0,1]=-G[0,1]
    G_inver[1,0]=-G[1,0]
    G_inver[1,1]=G[0,0]
    G_inver/=det_G

    t_array=np.linspace(0,T,N)

    u=np.zeros((N,2))
    un=[0,1]
    u[0]=un

    for i in range(1,N):
        next_u=np.dot(G_inver,un)
        u[i]=next_u
        un=next_u
  
    displacement=u[:,0] #first col
    velocity=u[:,1]#second col
    plt.plot(t_array,displacement,label=f'simulated with stepsize {dt}')
    
plt.plot(t_array,np.sin(t_array),label='analytical')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend()
plt.grid()
plt.show()