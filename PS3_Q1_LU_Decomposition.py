# Write a program to perform LU decomposition followed by forward and backward substitution to solve
# A · x = b for x. Use this to also invert the matrix A.

import numpy as np
import matplotlib.pyplot as plt

A = (1 / 6) * np.array([
    [5, 4, 3, 2, 1],
    [4, 8, 6, 4, 2],
    [3, 6, 9, 6, 3],
    [2, 4, 6, 8, 4],
    [1, 2, 3, 4, 5]
])
b=np.array([0,1,2,3,4])
N=5

U=np.zeros((N,N))
L=np.zeros((N,N))



#initialize L
for j in range(0,N): 
    for i in range(0,N): 
        if i==j:
            L[i][j]=1

#LU decomposition            
for j in range(0,N): #this is column
    for i in range(0,N): #this is row
        if i<=j:
            U[i][j]=A[i][j]-np.sum([L[i][k]*U[k][j] for k in range(0,i)])

        if i>j:
            L[i][j]=(1/U[j][j])*(A[i][j]-np.sum([L[i][k]*U[k][j] for k in range(0,j)]))


#solving for y (Ux): L.y=b  can be solved by forward substitution
def solve_for_x(b):
    y=np.zeros(N)
    y[0]=b[0]/L[0][0]
    for i in range(1,N):
        y[i]=(b[i]-np.sum([L[i][j]*y[j] for j in range(0,i)]))/L[i][i]

    #solving for x: U.x=y  can be solved by backward substitution
    x=np.zeros(N)
    x[N-1]=y[N-1]/U[N-1][N-1]
    for i in range(N-2,-1,-1): #generate N-1 numbers from N-2 to 0
        x[i]=(y[i]-np.sum([U[i][j]*x[j] for j in range(i+1,N)]))/U[i][i]

    return x

I=np.eye(N)
Inverse_A=np.zeros((N,N))

for i in range (0,N):
    Inverse_A[:,i]=solve_for_x(I[:,i])

x=solve_for_x(b)

#error magnitude 
#first evaluate r=Ax-b, should be 0 in ideal case
#error is sum of every r element /N

r=np.dot(A,x)-b
r_error=np.sum(np.abs(r))/N

R=np.abs(np.dot(A,Inverse_A)-I)
R_error=np.sum(np.sum(R[i] for i in range(0,N-1)))/N**2

print(r_error)
print(R_error)
