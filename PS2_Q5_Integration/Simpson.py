# Calculate the extended Simpson’s rule integral at each step size. Comment on the accuracy of
# Simpson’s rule and the trapezoidal rule.

import numpy as np
from scipy.special import sici

h=1
x0=h
num_points=round(((10-x0)/h)+1) #number of points in range (x0,10) when stepsize=10
x_array=np.linspace(h,10,num_points)
func_x=np.sin(x_array**2)/x_array

odd_terms=[]
even_terms=[]
for i in range(1,len(func_x)-1):
    if i%2==1:
        odd_terms=np.append(func_x[i],odd_terms)
    if i%2==0:
        even_terms=np.append(func_x[i],even_terms)


Integration=h*(1/3*(func_x[0]+func_x[-1])+4/3*(sum(odd_terms))+2/3*(sum(even_terms)))

real_integration=0.5*sici(100)[0]
print('Numerical:',Integration)
print('Python build-in:',real_integration)


