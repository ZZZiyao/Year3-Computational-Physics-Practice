import numpy as np
from scipy.special import sici


#first, same as close path method, we calculate the integral from x0=h to 10
h=1e-4
num_points_exclude_1st=round(((10-h)/h)+1) #number of points in range (x0,10) when stepsize=10
x_array_exclude_1st=np.linspace(h,10,num_points_exclude_1st)
func_x_exclude_1st=np.sin(x_array_exclude_1st**2)/x_array_exclude_1st

odd_terms=[]
even_terms=[]
for i in range(1,len(func_x_exclude_1st)-1):
    if i%2==1:
        odd_terms=np.append(func_x_exclude_1st[i],odd_terms)
    if i%2==0:
        even_terms=np.append(func_x_exclude_1st[i],even_terms)

Integration_exclude_1st=h*(1/3*(func_x_exclude_1st[0]+func_x_exclude_1st[-1])+4/3*(sum(odd_terms))+2/3*(sum(even_terms)))


#and then, we include the estimation of the integral from 0 to x=h
x_0_1=(0+h)/2
func_1st=np.sin(x_0_1**2)/x_0_1
Integration_1st=h*func_1st

Integration=Integration_1st+Integration_exclude_1st
real_integration=0.5*sici(100)[0]


print('Numerical:',Integration)
print('Python build-in:',real_integration)