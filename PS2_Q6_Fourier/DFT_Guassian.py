# If this experiment had been performed with a probe laser with Gaussian pulses of 500 femtoseconds
# (1 fs = 10−3 ps), the data would be convolved with a 500 fs Gaussian function.
# i. Perform a DFT on a Gaussian with a standard deviation of 100 fs, sampled over the same range
# as the experimental data. What is the result? Hint: The formula for a Gaussian function with
# standard deviation of σ is g(t) = Ae−t^2/2σ^2. Hint: DFTs assume that the signal/function is
# periodically extended beyond T.

import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt(r"D:\CP\Practice\Year3-Computational-Physics-Practice\PS2_Q6_Fourier\data.txt")
std=0.5 #unit should be same as experimental data(ps)
def gaussian(t, mu):
    gt = np.exp(-(t-mu)**2 / (2*std**2))
    return gt

t_array=data[:,0]
N=len(t_array)
dt=t_array[1]-t_array[0]
T=N*dt
dw=2*np.pi/T
fn_array=gaussian(t_array,0)+gaussian(t_array,T)
fn_array=fn_array/fn_array.sum()

p_array=np.linspace(-N/2+1,N/2,N)
w_array=p_array*dw
fp_array=[]
for p in p_array:
    fp=sum([fn_array[n]*np.exp(1j*2*np.pi*p*n/N) for n in range(0,N)])
    fp_array.append(fp)

# Save DFT results to file
output_data = np.column_stack((w_array, np.abs(fp_array)))  # Combine frequencies and magnitudes
output_file = r"D:\CP\Practice\Year3-Computational-Physics-Practice\PS2_Q6_Fourier\dft_gauss.txt"
np.savetxt(output_file, output_data, header="Frequency (rad/s)  Magnitude", fmt="%.6e")
print(f"DFT results saved to {output_file}")



fig, axs = plt.subplots(2, 1, figsize=(12,8))
axs[0].plot(t_array, fn_array)
axs[1].plot(w_array, np.abs(fp_array))

axs[0].set_xlabel('t (ps)')
axs[0].set_ylabel('f(t)')
axs[1].set_xlabel(r'$\omega$ ($\times 10^{12} $ rad s$^{-1}$)') 
axs[1].set_ylabel(r'$\^f(\omega)$')
plt.show()