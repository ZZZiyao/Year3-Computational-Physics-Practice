import numpy as np
import matplotlib.pyplot as plt

def func_2D(x,y):
    return (x-0.5)**2+(y-0.5)**2

errors=[]
N=1e7
V=1
x_array=np.random.rand(int(N))
y_array=np.random.rand(int(N))
fi=func_2D(x_array,y_array)
fi_acc=[]
for f in fi:
    if f<1/4:
      fi_acc.append(1)
I=V/N*np.sum(fi_acc)
print(I)
print(1/4*np.pi)
