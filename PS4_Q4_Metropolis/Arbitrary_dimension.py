import numpy as np
import matplotlib.pyplot as plt

# Define the target function
def func_nD(pos,r=0.5):
    condition=np.sum([(pos[i] - r)**2 for i in range(0,len(pos))])
    if condition <r**2:
        return 1
    else:
        return 0

# Define the Gaussian distribution for P(x)
def gaussian_nD(pos, n, sig=1, mu=0.5):
    power_numerator =np.sum( [((pos[i] - mu)**2) for i in range(0,len(pos))])
    power=power_numerator/(2 * sig**2)
    A = 1 / (((2 * np.pi)**(n/2)) * sig**n)
    return A * np.exp(-power)


#propose another point
def gaussian_proposal(pos, sigma=1):
    return pos + np.random.normal(0, sigma,size=len(pos))

# Metropolis parameters
N = int(1e6)  # Number of iterations
n=3
pos=np.random.rand(n)  # Initial point
# Storage for accepted Q values
Q_acc = []

for i in range(N):
    # Propose new points
    new_pos = gaussian_proposal(pos)

    # Calculate probabilities
    Pcurrent = gaussian_nD(pos, n)
    Pnew = gaussian_nD(new_pos, n)

    # Calculate Q
    Q = func_nD(new_pos) / Pnew

    # Metropolis acceptance step
    if Pcurrent <= Pnew:  # Accept new value
        Q_acc.append(Q)
        pos=new_pos  # Update values
    else:
        Pacc = Pnew / Pcurrent  # Acceptance probability
        some_rand = np.random.uniform(0, 1)
        if some_rand < Pacc:  # Random number falls within acceptance range
            Q_acc.append(Q)
            pos=new_pos


Q_mean = np.mean(Q_acc)
Q_std = np.std(Q_acc) / np.sqrt(len(Q_acc))  # Standard error

print(f"Estimated integral: {Q_mean} ± {Q_std}")
print(f'theoretical: {4/3*np.pi*0.5**3}')


        