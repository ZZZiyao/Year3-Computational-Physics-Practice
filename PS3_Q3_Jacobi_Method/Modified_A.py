# You will also need to prevent the program getting stuck in an infinite loop if the iteration does not
# converge. Can you modify A to purposefully make the method not converge so as to check this?
import numpy as np

def generate_A(N,diag):
    A=np.zeros((N,N))
    for i in range(0,N):
        A[i][i]=diag
        if i>0:
            A[i][i-1]=-1 #this excludes the 1st row
        if i<N-1:
            A[i][i+1]=-1 #this excludes the last row
    return A

def generate_SB(N,A):
    TL=np.zeros((N,N))
    TU=np.zeros((N,N))
    D=np.zeros((N,N))
    for i in range(0,N):
        for j in range(0,N):
            if i>j:
                TL[i][j]=A[i][j]
            if i<j:
                TU[i][j]=A[i][j]
            if i==j:
                D[i][j]=A[i][j]
    return TL, TU, D

def generate_inverse_D(D):
    inverse_D=D
    N=D.shape[0]
    for i in range(0,N):
        for j in range(0,N):
            if i==j:
                inverse_D[i][j]=1/D[i][j]
    return inverse_D


b=[-1,0,0,0,5]
A=generate_A(5,1) #change diagonal element to 1
TL=generate_SB(5,A)[0]
TU=generate_SB(5,A)[1]
D=generate_SB(5,A)[2]
inverse_D=generate_inverse_D(D)
G=np.dot(inverse_D,TL+TU)

inverse_Ai=inverse_D
total_sum_Ai = 0
for row in inverse_Ai:
    for element in row:
        total_sum_Ai += element
residual=[]
for i in range(0,1000):
    next_A=inverse_D-np.dot(G,inverse_Ai)
    total_sum_next = 0
    for row in next_A:
        for element in row:
            total_sum_next += element

    error=np.abs((total_sum_next-total_sum_Ai)/total_sum_Ai)
    residual.append(error)
    if residual[i]>residual[i-1]:
        print(f'At {i} iteration, residual increase, do not converge')
        break
    if error<1e-13:
        print(f'found solution after {i} iterations:{next_A}')
        break
    inverse_Ai=next_A
    total_sum_Ai=total_sum_next
else:
        print('cannot find solution')