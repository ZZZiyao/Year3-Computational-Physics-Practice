import numpy as np
import matplotlib.pyplot as plt

# Define the target function
def func_2D(x, y, r=0.5):
    condition=(x - r)**2 + (y - r)**2
    if condition <1/4:
        return 1
    else:
        return 0

# Define the Gaussian distribution for P(x)
def gaussian_2D(x, y, sig=1, mu=0.5):
    power = -((x - mu)**2 + (y - mu)**2) / (2 * sig**2)
    A = 1 / (2 * np.pi * sig**2)
    return A * np.exp(power)


#propose another point
def gaussian_proposal(x, sigma=1):
    return x + np.random.normal(0, sigma)

# Metropolis parameters
N = int(1e6)  # Number of iterations
N_array=[1e2,1e3,1e4,1e5,1e6,1e7]
errors=[]
for N in N_array:
    N=int(N)
    x, y = 0.5, 0.5  # Initial point
    step_size = 0.1  # Step size for proposal distribution

    # Storage for accepted Q values
    Q_acc = []

    for i in range(N):
        # Propose new points
        new_x = gaussian_proposal(x)
        new_y = gaussian_proposal(y)

        # Calculate probabilities
        Pcurrent = gaussian_2D(x, y)
        Pnew = gaussian_2D(new_x, new_y)

        # Calculate Q
        Q = func_2D(new_x, new_y) / Pnew

        # Metropolis acceptance step
        if Pcurrent <= Pnew:  # Accept new value
            Q_acc.append(Q)
            x, y = new_x, new_y  # Update values
        else:
            Pacc = Pnew / Pcurrent  # Acceptance probability
            some_rand = np.random.uniform(0, 1)
            if some_rand < Pacc:  # Random number falls within acceptance range
                Q_acc.append(Q)
                x, y = new_x, new_y


    Q_mean = np.mean(Q_acc)
    Q_std = np.std(Q_acc) / np.sqrt(len(Q_acc))  # Standard error
    errors.append(Q_std)

    print(f"Estimated integral: {Q_mean} ± {Q_std}")
    print(f'theoretical: {np.pi*0.5**2}')

plt.plot(N_array,errors)
plt.show()
        


