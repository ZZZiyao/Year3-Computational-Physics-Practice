# Question: Finding the position between several point charges at which there is no electric field. 
# Use a generalised Newton-Raphson method for two variables, with either analytic or numerical estimates
# for the derivatives in the Jacobian matrix, to find the position at which E~0 = 0. You will need to pick
# a sensible starting guess for x and y; try to think of arguments using symmetries or slightly modified
# geometries which can help with this.

import numpy as np

r0=np.array([1,0])
r1=np.array([np.cos(np.radians(120)),np.sin(np.radians(120))])
r2=np.array([np.cos(np.radians(240)),np.sin(np.radians(240))])


def distance(r, r_i):
    return np.sqrt((r[0] - r_i[0])**2 + (r[1] - r_i[1])**2)

charges=[1,0.5,1]
positions=[r0,r1,r2]


def electric_field(r):
    Ex=((r[0]-r0[0])/((np.linalg.norm(r-r0))**3)) + (0.5*((r[0]-r1[0])/((np.linalg.norm(r-r1))**3))) + (r[0]-r2[0])/((np.linalg.norm(r-r2))**3)
    Ey=((r[1]-r0[1])/((np.linalg.norm(r-r0))**3)) + (0.5*((r[1]-r1[1])/((np.linalg.norm(r-r1))**3))) + (r[1]-r2[1])/((np.linalg.norm(r-r2))**3)
    return np.array([Ex,Ey])
    #returns x and y components of function


def jacobian(r):
    J = np.zeros((2, 2))
    for i in [0,1,2]:

        Q = charges[i]

        d = distance(r, positions[i])
        
        dx = r[0] - positions[i][0]
        dy = r[1] - positions[i][1]
        
        J[0, 0] += Q * (1 / d**3 - 3 * dx**2 / d**5)  # ∂E'_x / ∂x
        J[0, 1] += Q * (-3 * dx * dy / d**5)         # ∂E'_x / ∂y
        J[1, 0] += Q * (-3 * dx * dy / d**5)         # ∂E'_y / ∂x
        J[1, 1] += Q * (1 / d**3 - 3 * dy**2 / d**5)  # ∂E'_y / ∂y
    
    return J




ri=np.array([-0.5,0.5]) #initial guess

for i in range(1, 100):
    F = electric_field(ri)
    J = jacobian(ri)
    next_r=ri-np.dot(np.linalg.inv(J),F)
    if np.linalg.norm(F) < 1e-10:
        print(f"Zero-field solution found after {i} iterations: {next_r}")
        break
    ri=next_r
else:
    print("Newton-Raphson method did not converge.")

    








