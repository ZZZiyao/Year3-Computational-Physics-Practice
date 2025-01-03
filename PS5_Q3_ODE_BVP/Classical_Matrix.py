# Question: Write a function to solve this system using the “classical physics” second-derivative matrix method
# described in the notes, which also uses the Euler method. Use the same number of steps as for the
# previous method. The inverse of the required matrix is given below. Note, the right-hand side of the
# system equation is only a function of t, not x, so the matrix equations will not need to be iterated.


import numpy as np
import matplotlib.pyplot as plt


T=1
N=99
N=int(N)
dt=T/N
t_array=np.linspace(0,T,N+1)

def analytical_func_u(t):
    return t*(t**2+2)/6

def analytical_func_v(t):
    return (3*t**2+2)/6

def generate_A(N=N-1):
    N=int(N)
    A=np.zeros((N,N))
    for i in range(0,N):
        for j in range(0,N):
            if i==j:
                A[i][j]=-2
            if i+1==j or i-1==j:
                A[i][j]=1
    return A


def generate_b(f_array=t_array,u0=0,uN=0.5,dt=dt):
    b=np.zeros(N-1)
    b[0]=f_array[0]*dt**2-u0
    b[-1]=f_array[N-2]*dt**2-uN
    b[1:N-2]=f_array[1:N-2]*dt**2
    return b

inver_A=np.linalg.inv(generate_A())
b=generate_b()

u=np.dot(inver_A,b)
u=np.concatenate([[0],u,[0.5]])

plt.plot(t_array,u,label='u solved by matrix equation')
plt.plot(t_array,analytical_func_u(t_array),label='analytical u')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend()
plt.grid()
plt.show()











