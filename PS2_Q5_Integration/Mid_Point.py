# (b) Using a mid-point step at 0 and closed at 10

import numpy as np
from scipy.special import sici


#first, same as close path method, we calculate the integral from x0=h to 10
h=1
num_points_exclude_1st=round(((10-h)/h)+1) #number of points in range (x0,10) when stepsize=10
x_array_exclude_1st=np.linspace(h,10,num_points_exclude_1st)
func_x_exclude_1st=np.sin(x_array_exclude_1st**2)/x_array_exclude_1st
Integration_exclude_1st=h*(0.5*(func_x_exclude_1st[0]+func_x_exclude_1st[-1])+(sum(func_x_exclude_1st[1:-1])))

#and then, we include the estimation of the integral from 0 to x=h
x_0_1=(0+h)/2
func_1st=np.sin(x_0_1**2)/x_0_1
Integration_1st=h*func_1st

Integration=Integration_1st+Integration_exclude_1st
real_integration=0.5*sici(100)[0]


print('Numerical:',Integration)
print('Python build-in:',real_integration)