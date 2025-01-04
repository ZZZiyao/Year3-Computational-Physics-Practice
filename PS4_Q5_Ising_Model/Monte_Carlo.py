import numpy as np
import matplotlib.pyplot as plt

def Create_lattice(N):
    atoms=-np.ones((N,N))
    return atoms

L=50
atoms=Create_lattice(L)

def Calculate_single_E(x, y):
    return -0.5*atoms[x,y]*(atoms[x,(y-1)%L] + atoms[x, (y+1)%L] + atoms[(x-1)%L, y] + atoms[(x+1)%L, y])

def Calculate_dE(x, y):
    # Flipping one atom changes the energy of the system by 4 units of the change in energy of the neighbouring atoms
    deltaE = -4.0*Calculate_single_E(x, y)
    return deltaE

def Flip_spin(x, y, T):
    deltaE = Calculate_dE(x,y)
    if deltaE < 0.0:
        atoms[x,y] *= -1
    elif np.random.uniform() < np.exp(-1.0*deltaE/T):
        atoms[x, y] *= -1



mean_s = []
iterations = range(20)
burnin = 0
for step in iterations:
    for i in range(L):
        for j in range(L):
            Flip_spin(i, j, T=3)
    
    if step >= burnin:  
        mean_spin = np.sum(atoms) / L**2
        mean_s.append(mean_spin)


plt.plot(range(burnin, 20), mean_s)
plt.show()

