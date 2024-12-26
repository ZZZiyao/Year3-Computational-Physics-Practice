import numpy as np
import matplotlib.pyplot as plt


g_array=[-0.9,-0.5,-0.1,-0.001,0.001,0.1,0.5,0.9]
error=[]
iterations=[]

for g in g_array:
    exact_value=1/(1+g)
    fi=1
    for i in range(1,1000):
        next_f=1-g*fi
        if np.abs((next_f-fi)/fi)<1e-6:
            print(f'converges to {next_f} after {i} iterations')
            print(f'difference with exact value is {next_f-exact_value}')
            relative_error=np.abs((next_f-exact_value)/exact_value)
            error.append(relative_error)
            iterations.append(i)
            break
    
        fi=next_f

    else:
            print('cannot converge')

plt.plot(g_array,error,'.')
plt.xlabel('value of g')
plt.ylabel('difference with exact value')
plt.show()

plt.plot(g_array,iterations,'.')
plt.xlabel('value of g')
plt.ylabel('number of iterations to converge')
plt.show()

