import numpy as np
import matplotlib.pyplot as plt



# 1 

t = np.arange(0, 0.03 + 0.0005, 0.0005)

x = lambda t: np.cos(520 * np.pi * t + np.pi / 3)
y = lambda t: np.cos(280 * np.pi * t - np.pi / 3)
z = lambda t: np.cos(120 * np.pi * t + np.pi / 3)

T = 1.0 / 200.0
n = np.arange(0, 0.03 + T, T)

fig, axs = plt.subplots(3)
fig.suptitle("Exercitiul 1")

axs[0].plot(t, x(t))
axs[0].stem(n, x(n))
axs[1].plot(t, y(t))
axs[1].stem(n, y(n))
axs[2].plot(t, z(t))
axs[2].stem(n, z(n))

plt.show()

# 2

# a

f = 400
t = np.arange(1600) / 4000
sig = np.sin(2 * np.pi * f * t)

plt.figure()
plt.plot(t[:200], sig[:200])
plt.title('Exercitiul 2 a')
plt.show()

# b

f = 800
T = 1 / 8000
t = np.arange(0, 3 + T, T) 
sig = np.sin(2 * np.pi * f * t)

plt.figure()
plt.plot(t[:200], sig[:200])  
plt.xlim(0, 0.005)
plt.title('Exercitiul 2 b')
plt.show()

# c

f = 240
T = 1 / 2400
t = np.arange(0, 0.02, T)
sig = 2 * (np.mod(t * f, 1)) - 1

plt.figure()
plt.plot(t, sig)
plt.title('Exercitiul 2 c')
plt.show()

# d

f = 300
T = 1 / 3000
t = np.arange(0, 0.02, T)
sig = np.sign(np.sin(2 * np.pi * f * t))

plt.figure()
plt.plot(t, sig)
plt.title('Exercitiul 2 d')
plt.show()

# e

img = np.random.rand(128, 128)

plt.figure()
plt.imshow(img, cmap='gray') 
plt.title('Exercitiul 2 e')
plt.show()

# f

img = np.zeros((128, 128))

img[32:96, 32:96] = 1.0

plt.figure()
plt.imshow(img, cmap='gray') 
plt.title('Exercitiul 2 f')
plt.show()


# 3
# a: 1 / 2000
# b: 3600000