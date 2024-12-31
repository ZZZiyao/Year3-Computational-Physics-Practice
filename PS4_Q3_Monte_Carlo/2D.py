import numpy as np
import matplotlib.pyplot as plt

def func_2D(x, y, r=0.5):
    condition=(x - r)**2 + (y - r)**2
    if condition <1/4:
        return 1
    else:
        return 0
    
errors=[]
N=1e7
V=1
x_array=np.random.rand(int(N)) #floats between 0 and 1
y_array=np.random.rand(int(N))
fi=[func_2D(x,y) for x,y in zip(x_array,y_array)]

I=V/N*np.sum(fi)
print(I)
print(1/4*np.pi)
