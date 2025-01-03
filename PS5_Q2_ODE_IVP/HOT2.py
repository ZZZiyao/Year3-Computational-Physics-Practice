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
N_array=[1e6,1e7]


I=np.eye(2)
A=[[0,1],
   [-1,0]] 

A_2=np.dot(A,A)

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
        next_u=dt*np.dot(A,un)+(dt**2/2)*np.dot(A_2,un)+un
        u[i]=next_u
        un=next_u
  
    displacement=u[:,0] #first col
    velocity=u[:,1]#second col
    

    error=abs(displacement[-1]-np.sin(T))
    global_errors.append(error)
    
    
plt.plot(N_array,global_errors,'.')
plt.xlabel('Timesteps N')
plt.ylabel('global error')
plt.grid()
plt.show()