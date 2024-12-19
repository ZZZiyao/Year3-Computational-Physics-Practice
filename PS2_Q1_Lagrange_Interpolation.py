# Question:Produce a simple dataset with n points (xi, fi), which follow a simple non-polynomial function of your
# choice. The built-in functions for sin and cos, or the Gaussian function, or anything along those lines can
# be used for this. Initially, choose n to be small; say 4 or 5. Plot the points to validate visually that they
# follow your chosen function.
# Implement a function that calculates the Lagrange polynomial formula in code directly. The code should
# be written so n can be changed easily (or figures out the value of n itself). Validate the result by
# checking that the function passes through the data points, and then plot the result across a reasonably
# finely-spaced set of x values. Observe the behaviour when x is outside of the range of xi points.
# Repeat for larger values of n, for the same original choice of function, and observe the behaviour of the
# interpolated function. What can you conclude about the use of Lagrange polynomials for interpolation?
# Try this for a few different functions (it should be easy to change the initial code at this point to allow
# you to test a few different forms).

import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    return (1.0 / (np.sqrt(2.0 * np.pi) * sig) * np.exp(-np.power((x - mu) / sig, 2.0) / 2))

xi=np.linspace(0,10,10)
fi=gaussian(xi,5,5)

def lagrange(x,xi,fi,num):
    adding_element=[]
    for i in range(0,num):
      basis_element=[]
      for j in range(0,num):
         if j!=i:
            basis_element.append((x-xi[j])/(xi[i]-xi[j]))
      basis=np.prod(basis_element)      
      adding_element.append(basis*fi[i])
    return np.sum(adding_element)

x=np.linspace(0,15,30)
num=len(xi)
lagrange_fit_func = [lagrange(x_val, xi, fi, num) for x_val in x] 

plt.plot(x,lagrange_fit_func,label='lagrange fitted function')
plt.plot(xi,fi,label='initial points')
plt.plot(x,gaussian(x,5,5),label='correct function')
plt.legend()
plt.title('Lagrange Polynomials')
plt.grid()
plt.show()
      
