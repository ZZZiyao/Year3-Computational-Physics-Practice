# Verify that you can perform a discrete Fourier transform (DFT) using the formulae in Chapter 3 of
# the lecture notes. Your DFT should take, as inputs, N samples from a function f(t). t should span a
# time domain between 0 ≤ t < T, such that your samples are spaced by ∆t = T/N.
# Plot the angular frequency spectrum of a sinusoidal function. Is the result as you expect?
# Tip: Use an even number of samples; or even better, make N a power of 2.
import numpy as np
import matplotlib.pyplot as plt


def func_to_dft(x):
    return np.sin(2*x)+np.sin(x)+np.cos(100*x)

T=2*np.pi
N=2**8
dt=T/N
dw=2*np.pi/T
t_array=np.array([i*dt for i in range(0,N)]) #this excludes N, which is sensible since we only have N-1 intervals
fn_array=func_to_dft(t_array)
p_array=np.linspace(-N/2+1,N/2,N)
w_array=p_array*dw
fp_array=[]
for p in p_array:
    fp=sum([fn_array[n]*np.exp(1j*2*np.pi*p*n/N) for n in range(0,N)])
    fp_array.append(fp)

fig, axs = plt.subplots(2, 1, figsize=(12,8))
axs[0].plot(t_array, fn_array)
axs[1].plot(w_array, np.abs(fp_array))

axs[0].set_xlabel(r'$t$ (s)')
axs[0].set_ylabel(r'$f(t)$')
axs[1].set_xlabel(r'$\omega$ (rad s$^{-1}$)')
axs[1].set_ylabel(r'$\^f(\omega)$')
plt.show()
