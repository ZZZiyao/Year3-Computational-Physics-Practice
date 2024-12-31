import numpy as np
import matplotlib.pyplot as plt



def func_arbitrary_dimen(dimen,N,r):
    dimen=int(dimen)
    N=int(N)
    matrix=2*r*np.random.rand(dimen,N)
    f_array=np.sum((matrix-r)**2, axis=0)
    return f_array


dimen=10
r=1
V=(2*r)**dimen
N=1e7
f_array=func_arbitrary_dimen(dimen,N,r)
N_acc=0
for f in f_array:
    if f<r**2:
      N_acc+=1
p=N_acc/N
I=V*p
I_error=np.sqrt(p*(1-p)/N)
print(f'estimated volume of sphere is {I} +/-{I_error}')