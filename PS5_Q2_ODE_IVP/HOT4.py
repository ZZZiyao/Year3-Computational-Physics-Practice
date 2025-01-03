# # Question: Finally, implement some or all of the fourth-order methods; HOT4, AB4, AM4 and RK4, again
# using the perfect method for the first few steps of AB4 and AM4. You should easily get to the
# rounding error limit; what approximate value of t gives this?


import numpy as np
import matplotlib.pyplot as plt
T=1
N_array=[5e2,6e2,7e2,8e2,1e3,2e3,3e3]


I=np.eye(2)
A=[[0,1],
   [-1,0]] 

A_2=np.dot(A,A)
A_3=np.dot(A_2,A)
A_4=np.dot(A_3,A)

global_errors=[]

for N in N_array:
    print(N)
    N=int(N)
    dt=T/(N-1)

    t_array=np.linspace(0,T,N)

    u=np.zeros((N,2))
    un=[0,1]
    u[0]=un

    for i in range(1,N):
        next_u=un+dt*np.dot(A,un)+(dt**2/2)*np.dot(A_2,un)+(dt**3/6)*np.dot(A_3,un)+(dt**4/24)*np.dot(A_4,un)
        u[i]=next_u
        un=next_u
  
    displacement=u[:,0] #first col
    velocity=u[:,1]#second col
    

    error=abs(displacement[-1]-np.sin(T))
    global_errors.append(error)
    
    
plt.plot(N_array,global_errors,'o-')
plt.xlabel('Timesteps N')
plt.ylabel('global error')
plt.grid()
plt.show()