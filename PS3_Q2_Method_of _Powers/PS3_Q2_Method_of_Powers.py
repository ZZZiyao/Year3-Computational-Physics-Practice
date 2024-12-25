# Implement the method of powers to find the eigenvalue with the largest modulus of the 5x5 matrix G
# You will need to decide on a stopping criterion based on the change of the eigenvalue or the average
# change to the eigenvector. You should also catch non-convergence in case of problems.
# How does the eigenvalue vary with the size of the matrix, when keeping the pattern of the numbers the
# same?
# Try this with 1/3 rather than 1/2 along both o↵-diagonal lines.

import numpy as np
import matplotlib.pyplot as plt

def generate_G(N,frac):
    G=np.zeros((N,N))
    for i in range(0,N):
        if i>0:
            G[i][i-1]=-frac #this excludes the 1st row
        if i<N-1:
            G[i][i+1]=-frac #this excludes the last row
    return G


N_array=np.linspace(5,50,46)
print(N_array)
max_lambda_2=[]
for N in N_array:
    N=int(N)
    G=generate_G(N,0.5)+0.001*np.eye(N) #regularization
    v = np.ones(G.shape[0]) 

    max_lamj=0 #assume 0 for the first comparison
    for n in range(1,50000):
        wj=np.dot(G,v)
        wj_normalized=wj/np.linalg.norm(wj)
        #actually python knows it's a transpose when putting a 1d array at front
        lamj=np.dot(np.dot(wj_normalized,G),wj_normalized)-0.001
        if np.abs(lamj-max_lamj)<1e-9:
            print(f"Size {N} Converged after {n} iterations, maximum eigenvalue is {lamj}.")
            max_lambda_2.append(np.abs(lamj))
            break

        max_lamj=lamj
        v = wj_normalized
    else:
        print(f"Did not converge within the maximum iterations, current eigenvalue is {lamj}.")

N_array=np.linspace(5,50,46)
print(N_array)
max_lambda_3=[]
for N in N_array:
    N=int(N)
    G=generate_G(N,1/3)+0.001*np.eye(N) #regularization
    v = np.ones(G.shape[0]) 

    max_lamj=0 #assume 0 for the first comparison
    for n in range(1,50000):
        wj=np.dot(G,v)
        wj_normalized=wj/np.linalg.norm(wj)
        #actually python knows it's a transpose when putting a 1d array at front
        lamj=np.dot(np.dot(wj_normalized,G),wj_normalized)-0.001
        if np.abs(lamj-max_lamj)<1e-9:
            print(f"Size {N} Converged after {n} iterations, maximum eigenvalue is {lamj}.")
            max_lambda_3.append(np.abs(lamj))
            break

        max_lamj=lamj
        v = wj_normalized
    else:
        print(f"Did not converge within the maximum iterations, current eigenvalue is {lamj}.")

plt.plot(N_array,max_lambda_2,'.',label='1/2 elements')
plt.plot(N_array,max_lambda_3,'.', label='1/3 elements')
plt.legend()
plt.title('max eigenvalue against size for different off-diagonal lines')
plt.xlabel('Size of matrix')
plt.ylabel('Largest eigenvalue')
plt.grid()
plt.show()




