# For a challenge, try and extend your integral from 0 to positive infinity. You can assume that the
# function evaluates to 0 at x=0.


import numpy as np
from scipy.special import sici


h=1e-4
x0=h
num_points=round(((10-x0)/h)+1) #number of points in range (x0,10) when stepsize=10
x_array=np.linspace(x0,10,num_points)
func_x=np.sin(x_array**2)/x_array
Integration_10=h*(0.5*(func_x[0]+func_x[-1])+(sum(func_x[1:-1])))

h_01=1e-8
x0_01=h_01
#compute 10 to inf, converting to 0 to 0.1
num_points_01=round(((1/10-x0_01)/h_01)+1) #number of points in range (x0,10) when stepsize=10
x_array_01=np.linspace(x0_01,1/10,num_points_01)
func_x_01=np.sin(x_array_01**-2)/x_array_01
Integration_01=h_01*(0.5*(func_x_01[0]+func_x_01[-1])+(sum(func_x_01[1:-1])))

Integration=Integration_10+Integration_01


print('Numerical:',Integration)
print('Actural:', np.pi/4)
