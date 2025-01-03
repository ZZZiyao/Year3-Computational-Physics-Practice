# # Question: Finally, implement some or all of the fourth-order methods; HOT4, AB4, AM4 and RK4, again
# using the perfect method for the first few steps of AB4 and AM4. You should easily get to the
# rounding error limit; what approximate value of t gives this?

import numpy as np
import matplotlib.pyplot as plt
T=1
N_array=[1e2,1e3,1e4]


I=np.eye(2)
A=[[0,1],
   [-1,0]] 

#AM4 coefficients
a=1/24*9
b=1/24*19
c=-1/24*5
d=1/24


global_errors=[]

for N in N_array:
    print(N)
    N=int(N)
    dt=T/(N-1)

    t_array=np.linspace(0,T,N)
    
    #define the update matrices
    G=I-np.dot(A,dt*a)
    inver_G=np.linalg.inv(G)
    F1=I+np.dot(A,dt*b)
    F2=np.dot(A,dt*c)
    F3=np.dot(A,dt*d)

    

    u=np.zeros((N,2))
    u[0]=[0,1]
    exact_update=np.array([[np.cos(dt),np.sin(dt)],
                           [-np.sin(dt),np.cos(dt)]])
    u[1]=np.dot(exact_update,u[0])
    u[2]=np.dot(exact_update,u[1])


    for n in range(2,N-1):
        M=np.dot(F1,u[n])+np.dot(F2,u[n-1])+np.dot(F3,u[n-2])
        u[n+1]=np.dot(inver_G,M)
 
    displacement=u[:,0] #first col
    velocity=u[:,1]#second col
    

    error=abs(displacement[-1]-np.sin(T))
    global_errors.append(error)
    
    
plt.plot(N_array,global_errors,'o-')
plt.xlabel('Timesteps N')
plt.ylabel('global error')
plt.grid()
plt.show()