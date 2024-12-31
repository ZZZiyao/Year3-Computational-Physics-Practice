import numpy as np
import matplotlib.pyplot as plt

def func_1D(x):
    return np.sin(x**2)/x

errors=[]
N_array=np.linspace(1e3,1e7,100)
for N in N_array:
    N=int(N)
    V=10
    x_array=V*np.random.rand(N)
    fi=func_1D(x_array)
    I=V/N*np.sum(fi)
    I_error=V/(np.sqrt(N))*np.std(fi)
    errors.append(I_error)
plt.plot(N_array,errors)
plt.show()