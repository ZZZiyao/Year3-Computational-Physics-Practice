import numpy as np
import matplotlib.pyplot as plt

data_exp=np.loadtxt(r"D:\CP\Practice\Year3-Computational-Physics-Practice\PS2_Q6_Fourier\dft_file.txt",skiprows=1,unpack=True)
data_gauss=np.loadtxt(r"D:\CP\Practice\Year3-Computational-Physics-Practice\PS2_Q6_Fourier\dft_gauss.txt",skiprows=1,unpack=True)
data=np.loadtxt(r"D:\CP\Practice\Year3-Computational-Physics-Practice\PS2_Q6_Fourier\data.txt")
t_arrayf=data[:,0]
fn_arrayf=data[:,1]

w_array=data_exp[0]
fp_array=data_exp[1]*data_gauss[1]
N=len(w_array)
dw=w_array[1]-w_array[0]
n_array=np.linspace(0,N-1,N)
dt=2*np.pi/(N*dw)
t_array=np.array([dt*i for i in n_array])
fn_array=[]
for n in n_array:
    fn=sum([fp_array[p]*np.exp(-1j*2*np.pi*p*n/N) for p in range(0,N-1)])
    fn_array.append((1/N)*fn)


fig, axs = plt.subplots(2, 1, figsize=(12,8))
axs[0].plot(t_array, np.abs(fn_array),label='convoluted')
axs[0].plot(t_arrayf,fn_arrayf,label='original')
axs[1].plot(w_array, fp_array,label='convoluted signal')
axs[1].plot(w_array,data_exp[1],label='experimentle signal')
axs[1].plot(w_array,data_gauss[1],label='gaussian signal')

axs[0].set_xlabel('t (ps)')
axs[0].set_ylabel('f(t)')
axs[1].set_xlabel(r'$\omega$ ($\times 10^{12} $ rad s$^{-1}$)') 
axs[1].set_ylabel(r'$\^f(\omega)$')
axs[0].legend()
axs[1].legend()

plt.show()