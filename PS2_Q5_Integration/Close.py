# Integrate the function sin(x^2)/x between 0 and 10 using an extended Trapezoidal Rule which is:
# (a) Closed at both ends
# (b) Using a mid-point step at 0 and closed at 10
# Given that this function cannot be evaluated directly at 0, for the closed rule take the first point to be one
# step, h, away (i.e. x0 = 0 + h).
# Compare these results as you reduce the stepsize from 1.0 to 1×10−2 then 1×10−4. 
# How do they compare to the true value (feel free to take this from Wolfram Alpha or equivalent)?

import numpy as np
from scipy.special import sici


h=1e-4
x0=h
num_points=round(((10-x0)/h)+1) #number of points in range (x0,10) when stepsize=10
x_array=np.linspace(h,10,num_points)
func_x=np.sin(x_array**2)/x_array
Integration=h*(0.5*(func_x[0]+func_x[-1])+(sum(func_x[1:-1])))


real_integration=0.5*sici(100)[0]
print('Numerical:',Integration)
print('Python build-in:',real_integration)



