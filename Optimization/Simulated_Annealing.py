import numpy as np
import matplotlib.pyplot as plt

kb=1.38e-23
bound=2


def func(x,y):
    return np.sin(3 * x) * np.sin(3 * y) + 0.5 * (x**2 + y**2)

def bolz(dE,T):
    return np.exp(-dE/(kb*T))

def annealing(T,cooling_rate=0.99,bound=bound):


    x0=np.random.uniform(-bound,bound)
    y0=np.random.uniform(-bound,bound)

    best_x=x0
    best_y=y0
    best_E=func(x0,y0)


    for _ in range(int(1e5)):
        

        current_E=func(x0,y0)

        if current_E<best_E:
            best_E=current_E
            best_x=x0
            best_y=y0

        hx=np.random.uniform(-0.1,0.1)
        hy=np.random.uniform(-0.1,0.1)

        new_x=x0+hx
        new_y=y0+hy
        new_x = np.clip(new_x, -bound, bound)
        new_y = np.clip(new_y, -bound, bound)

        new_E=func(new_x,new_y)

        dE=new_E-current_E

        if dE<=0:
            x0=new_x
            y0=new_y
        
        
        else:
            pacc=bolz(dE,T)
            if np.random.rand()<pacc:
                x0=new_x
                y0=new_y
        
    
        

        T*=cooling_rate

    return best_x,best_y,best_E

result=annealing(200)

x = np.linspace(-bound, bound, 200)
y = np.linspace(-bound, bound, 200)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=50, cmap="viridis")
plt.colorbar(label="f(x, y)")
plt.scatter(result[0], result[1], color='red', label=f'Optimal solution at x={result[0]:2f}, y={result[1]:2f}, with value {result[2]:2f}', zorder=10)
plt.title("Simulated Annealing Optimization")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()





    