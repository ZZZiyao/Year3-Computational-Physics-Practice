import numpy as np
import matplotlib.pyplot as plt

def f_x(x,xi,x_post,fi,f_post,fi2,f_post2):
    A_x=(x_post-x)/(x_post-xi)
    B_x=1-A_x
    C_x=1/6*(A_x**3-A_x)*(x_post-xi)**2
    D_x=1/6*(B_x**3-B_x)*(x_post-xi)**2
    return A_x*fi+B_x*f_post+C_x*fi2+D_x*f_post2

def generate_M(x):
    N=len(x)
    M=np.zeros((N,N))
    M[0][0]=1
    M[N-1][N-1]=1
    for i in range(1,N-1):
        M[i][i]=(x[i+1]+x[i-1])/3
        M[i][i-1]=(x[i]+x[i-1])/6
        M[i][i+1]=(x[i+1]+x[i])/6
    return M

def generate_b(x,f):
    N=len(x)
    b=np.zeros(N)
    b[0]=b[-1]=0
    for i in range(1,N-1):
        b[i]=(f[i+1]-f[i])/(x[i+1]-x[i])-(f[i]-f[i-1])/(x[i]-x[i-1])
    return b

x=np.linspace(0,10,20)
f=np.sin(x) 

b=generate_b(x,f)
M=generate_M(x)
f_dash=np.dot(np.linalg.inv(M),b)

fx=[]
x_to_inter=[]

for i in range(len(x)-1):
    interp_x=np.linspace(x[i],x[i+1],100)
    x_to_inter=np.concatenate([x_to_inter,interp_x])
    f_inter=f_x(interp_x,x[i],x[i+1],f[i],f[i+1],f_dash[i],f_dash[i+1])
    fx=np.concatenate([fx,f_inter])

plt.plot(x,f,'o')
plt.plot(x_to_inter,fx)
plt.show()




