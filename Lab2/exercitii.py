import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.io.wavfile

# 1

f = 4
phi_s = np.pi / 4
phi_c = phi_s - np.pi / 2
fs = 1000
t = np.linspace(0, 1, fs)

sig_s = np.sin(2 * np.pi * f * t + phi_s)
sig_c = np.cos(2 * np.pi * f * t + phi_c)

fig, axs = plt.subplots(2)
fig.suptitle("Exercitiul 1")

axs[0].plot(t, sig_s)
axs[1].plot(t, sig_c)
plt.tight_layout()
plt.show()

# 2

# partea 1

f = 4
fs = 1000
t = np.linspace(0, 1, fs)
phases = [0, np.pi / 4, np.pi / 2, np.pi]

fig, axs = plt.subplots(4)
fig.suptitle("Exercitiul 2 - Partea 1")

for i, phi in enumerate(phases):
    sig = np.sin(2 * np.pi * f * t + phi)
    axs[i].plot(t, sig)

plt.tight_layout()
plt.show()

# partea 2

sig = np.sin(2 * np.pi * f * t)
n = np.random.normal(0, 1 , len(t))
norm_sig = np.linalg.norm(sig)
norm_n = np.linalg.norm(n)
snr_values = [0.1, 1, 10, 100]

fig, axs = plt.subplots(4)
fig.suptitle("Exercitiul 2 - Partea 2")

for i, snr in enumerate(snr_values):
    gamma = np.sqrt((norm_sig ** 2) / (snr * (norm_n ** 2)))

    sig_noisy = sig + gamma * n

    axs[i].plot(t, sig_noisy)

plt.tight_layout()
plt.show()

# 3

fs = 8000
t = np.arange(fs * 2) / fs

sig = np.sin(2 * np.pi * 400 * t)

sd.play(sig, fs)
sd.wait()

scipy.io.wavfile.write('semnal_ex3.wav', fs, np.double(sig))

fs_r, sig_r = scipy.io.wavfile.read('semnal_ex3.wav')

# 4

f = 4
fs = 1000
t = np.linspace(0, 1, fs)

sig_s = np.sin(2 * np.pi * f * t)
sig_saw = 2 * (np.mod(t * f, 1)) - 1
sig_sum = sig_s + sig_saw

fig, axs = plt.subplots(3)
fig.suptitle("Exercitiul 4")

axs[0].plot(t, sig_s)
axs[1].plot(t, sig_saw)
axs[2].plot(t, sig_sum)
plt.tight_layout()
plt.show()

# 5

fs = 8000               
t = np.linspace(0, 1, fs)

f1 = 400
sig1 = np.sin(2 * np.pi * f1 * t)

f2 = 800
sig2 = np.sin(2 * np.pi * f2 * t)

sig_concat = np.concatenate((sig1, sig2))

sd.play(sig_concat, fs)
sd.wait()

# se observa o tranzitie brusca 

# 6

fs = 1000
t = np.arange(0, 1, 1/fs) 

sig_a = np.sin(2 * np.pi * (fs / 2) * t)
sig_b = np.sin(2 * np.pi * (fs / 4) * t)
sig_c = np.sin(2 * np.pi * 0 * t)

# la a, este doar 0; la b, se repeta secventa 0, 1, 0, -1; la c, este doar 0

# 7

fs = 1000
f = 40
t = np.linspace(0, 1, fs)

sig = np.sin(2 * np.pi * f * t)

sig_a = sig[::4]
fs_ab = fs / 4
t_a = np.arange(len(sig_a)) / fs_ab

sig_b = sig[1::4]
t_b = np.arange(len(sig_b)) / fs_ab


fig, axs = plt.subplots(3)
fig.suptitle("Exercitiul 7")
axs[0].plot(t, sig)
axs[1].plot(t_a, sig_a)
axs[2].plot(t_b, sig_b)
plt.tight_layout()
plt.show()

# a: daca fs / 8 >= f, atunci semnalul tot este bine reprezentat

# b: semnalul este decalat cu 1

# 8

alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000)

sin = np.sin(alpha)
approx_taylor = alpha
approx_pade = (alpha - (7 * alpha**3) / 60) / (1 + (alpha**2) / 20)

err_taylor = np.abs(sin - approx_taylor)
err_pade = np.abs(sin - approx_pade)

fig, axs = plt.subplots(3)
fig.suptitle("Exercitiul 8 - Taylor")

axs[0].plot(alpha, sin)
axs[1].plot(alpha, approx_taylor)
axs[2].plot(alpha, err_taylor)
plt.tight_layout()
plt.show()

# este foarte precis in jurul lui 0, dar cu cat se apropie de capetele intervalului cu atat creste eroarea

fig, axs = plt.subplots(3)
fig.suptitle("Exercitiul 8 - Pade")

axs[0].plot(alpha, sin)
axs[1].plot(alpha, approx_pade)
axs[2].plot(alpha, err_pade)
plt.tight_layout()
plt.show()

# este extrem de precis pe tot intervalul

fig, axs = plt.subplots(2)
fig.suptitle("Exercitiul 8 - Axa logaritmica")

axs[0].semilogy(alpha, err_taylor)
axs[1].semilogy(alpha, err_pade)
plt.tight_layout()
plt.show()

# Taylor: ajunge pana la aprox 10**-1 la capetele intervalului; Pade: ajunge pana la aprox 10**-3 la capetele intervalului  