import numpy as np
import matplotlib.pyplot as plt
r=0.5
V_ball=4/3*np.pi*r**3
def func_3D(x,y,z):
    return (x-0.5)**2+(y-0.5)**2+(z-0.5)**2

V=1
N=1e7
x_array=np.random.rand(int(N))
y_array=np.random.rand(int(N))
z_array=np.random.rand(int(N))
fi=func_3D(x_array,y_array,z_array)
N_acc=0
for f in fi:
    if f<1/4:
      N_acc+=1
p=N_acc/N
I=V*p
I_error=np.sqrt(p*(1-p)/N)
print(f'estimated volume of sphere is {I} +/-{I_error}')
print(f'Theoretical value is {V_ball}')