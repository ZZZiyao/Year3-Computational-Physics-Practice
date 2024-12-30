
import numpy as np
from scipy.integrate import quad



def func_to_evaluate(x):
    return np.sin(x**2)


x_end=1
x0=0
h=x_end-x0
Tj=h*(0.5*(func_to_evaluate(x0)+func_to_evaluate(x_end)))
print(Tj)

for j in range(1,20):
    adding=[]
    for i in range(1,2**(j-1)+1):
        adding_element=func_to_evaluate(x0+(2*i-1)*h/2)
        adding.append(adding_element)

    Tj1=0.5*Tj+0.5*h*sum(adding)
    print(f"Iteration {j}: Tj1 = {Tj1}, h = {h}")
    
    Sj=4/3*Tj1-1/3*Tj

    if abs((Tj1-Tj)/Tj)<0.0001:
        Integration=Tj1
        break
    Tj=Tj1
    h/=2
else:
    Integration = Tj1


real_integration=quad(func_to_evaluate,0,1)[0]
print('Numerical:',Integration)
print('Python build-in:',real_integration)