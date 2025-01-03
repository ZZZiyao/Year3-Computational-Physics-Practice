# # Question: Check using the analytic solution that the right-hand side of the system equation could alternatively
# be written as x'' = 3x-(t^3/2) for these boundary conditions. Solve this system using your matrix method. 
# The function on the right-hand side is now x dependent; an easy approach to handle this is to iterate. Start with a “guess”
# which goes through the two boundary values, such as the linear function xi = ti/2.


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



def generate_b(u,u0=0,uN=0.5,dt=dt):
    f_array=3*u-((t_array**3)/2)
    b=np.zeros(N-1)
    b[0]=f_array[0]*dt**2-u0
    b[-1]=f_array[N-2]*dt**2-uN
    b[1:N-2]=f_array[1:N-2]*dt**2
    return b

inver_A=np.linalg.inv(generate_A())
inner_u = t_array[1:-1] / 2  # Linear initial guess for interior points
un=np.concatenate([[0],inner_u,[0.5]]) #initial guess of u


for i in range(int(1e3)):
    b=generate_b(un)
    next_inner_u=np.dot(inver_A,b)
    next_u=np.concatenate([[0],next_inner_u,[0.5]])
    error=abs((np.sum(next_u-un)))/(np.sum(un))
    if error<1e-13:
        print(f'converged in {i} iterations')
        break
    un=next_u




plt.plot(t_array,next_u,label='u solved by matrix equation')
plt.plot(t_array,analytical_func_u(t_array),label='analytical u')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend()
plt.grid()
plt.show()