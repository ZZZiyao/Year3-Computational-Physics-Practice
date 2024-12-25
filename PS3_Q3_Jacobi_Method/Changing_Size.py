# Question: This matrix is not strictly diagonally dominant but the Jacobi method does actually converge. However,
# it can take many iterations to do so and the number of iterations required gets very large as the matrix
# gets bigger. See how the number of iterations grows with the matrix size. Compare with the same size
# matrix but with 3’s along the diagonal rather than 2’s. The 3’s make the Jacobi approximation better and
# it should converge much faster.

import numpy as np
import matplotlib.pyplot as plt

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


N_array=np.linspace(3,50,48)
iterations_2=[]
for N in N_array:
    N=int(N)
    A=generate_A(N,2) #change diagonal element to 1
    TL=generate_SB(N,A)[0]
    TU=generate_SB(N,A)[1]
    D=generate_SB(N,A)[2]
    inverse_D=generate_inverse_D(D)
    G=np.dot(inverse_D,TL+TU)

    inverse_Ai=inverse_D
    total_sum_Ai = 0
    for row in inverse_Ai:
        for element in row:
            total_sum_Ai += element
    residual=[]
    for i in range(0,int(1e5)):
        next_A=inverse_D-np.dot(G,inverse_Ai)
        total_sum_next = 0
        for row in next_A:
            for element in row:
                total_sum_next += element

        error=np.abs((total_sum_next-total_sum_Ai)/total_sum_Ai)
 
        if error<1e-13:
            print(f'found solution after {i}')
            iterations_2.append(i)
            break
        inverse_Ai=next_A
        total_sum_Ai=total_sum_next
    else:
            print('cannot find solution')


iterations_3=[]
for N in N_array:
    N=int(N)
    A=generate_A(N,3) #change diagonal element to 1
    TL=generate_SB(N,A)[0]
    TU=generate_SB(N,A)[1]
    D=generate_SB(N,A)[2]
    inverse_D=generate_inverse_D(D)
    G=np.dot(inverse_D,TL+TU)

    inverse_Ai=inverse_D
    total_sum_Ai = 0
    for row in inverse_Ai:
        for element in row:
            total_sum_Ai += element
    residual=[]
    for i in range(0,int(1e4)):
        next_A=inverse_D-np.dot(G,inverse_Ai)
        total_sum_next = 0
        for row in next_A:
            for element in row:
                total_sum_next += element

        error=np.abs((total_sum_next-total_sum_Ai)/total_sum_Ai)
 
        if error<1e-13:
            print(f'found solution after {i} iterations')
            iterations_3.append(i)
            break
        inverse_Ai=next_A
        total_sum_Ai=total_sum_next
    else:
            print('cannot find solution')

plt.plot(N_array,iterations_2,label='diagonal element=2')
plt.plot(N_array,iterations_3,label='diagonal element=3')
plt.legend()
plt.title('num of iterations to converge against size for different diagonal elements')
plt.xlabel('Size of matrix')
plt.ylabel('num of iterations')
plt.grid()
plt.show()
