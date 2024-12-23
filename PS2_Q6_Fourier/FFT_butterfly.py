import numpy as np
import matplotlib.pyplot as plt

def bit_reversal(n, num_bits):
    binary = f'{n:0{num_bits}b}'  # Convert n to a binary string with num_bits digits
    reversed_binary = binary[::-1]  # Reverse the binary string
    return int(reversed_binary, 2)  # Convert the reversed binary string back to an integer

def generate_bit_reversed_indices(N):
    num_bits = int(np.log2(N))  # Number of bits needed to represent indices
    return [bit_reversal(i, num_bits) for i in range(N)]

def bit_reverse_reorder(arr):
    N = len(arr)
    indices = generate_bit_reversed_indices(N)  # Get the bit-reversed indices
    reordered = np.zeros(N, dtype=arr.dtype)  # Create a new array with the same type as input
    for index, value in enumerate(indices):
        reordered[index] = arr[value]  # Place the value at the bit-reversed position
    return reordered


def iterative_fft(x):
    N = len(x)
    if np.log2(N) % 1 > 0:
        raise ValueError("Input length must be a power of 2")

    # Step 1: Bit-reversal reordering
    x = bit_reverse_reorder(x)

    # Step 2: Iterative FFT computation
    num_stages = int(np.log2(N))
    for stage in range(1, num_stages + 1):
        m = 2**stage  # Current block size
        half_block = m // 2  # Half block size

        for start in range(0, N, m):  # Start index of the current block
            for p in range(half_block):
                twiddle_factor = np.exp(-2j * np.pi * p / m)
                even_value = x[start + p]
                odd_value = x[start + p + half_block]
                x[start + p] = even_value + twiddle_factor * odd_value
                x[start + p + half_block] = even_value - twiddle_factor * odd_value

    return x


def func_to_fft(t):
    return np.sin(t) + np.cos(10 * t)  


T = 2 * np.pi  # Period
N = 2**8  # sample size
dt = T / N  
dw = 2 * np.pi / T  


t_array = np.array([i * dt for i in range(N)])  
p_array = np.arange(-N // 2, N // 2)  
w_array = p_array * dw  


fn_array = func_to_fft(t_array)


fft_result = iterative_fft(fn_array.astype(complex))

# 手动平移 FFT 结果
fft_shifted = np.zeros_like(fft_result, dtype=complex)
fft_shifted[:N // 2] = fft_result[N // 2:]  # move high frequencies to the front
fft_shifted[N // 2:] = fft_result[:N // 2]  # move low frequencies to behind


amplitude = np.abs(fft_shifted) / N  # normalization


plt.figure(figsize=(10, 12))


plt.subplot(2, 1, 1)
plt.plot(t_array, fn_array)
plt.title("Time-Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()


plt.subplot(2, 1, 2)
plt.plot(w_array, amplitude)
plt.title("Frequency Spectrum (Manual Shift)")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()


