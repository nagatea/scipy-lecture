#%%
%matplotlib inline
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.xticks()
plt.yticks()
plt.subplot(1, 2, 1)
plt.text(0.5, 0.5, 'subplot(1,2,1)', ha='center', va='center', size=20, alpha=.5)
plt.subplot(1, 2, 2)
plt.text(0.5, 0.5, 'subplot(1,2,2)', ha='center', va='center', size=20, alpha=.5)

#%%
plt.figure(figsize=(6, 4))
plt.xticks()
plt.yticks()
plt.subplot(2, 2, 1)
plt.text(0.5, 0.5, 'subplot(2,2,1)', ha='center', va='center', size=20, alpha=.5)
plt.subplot(2, 2, 2)
plt.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center', size=20, alpha=.5)
plt.subplot(2, 2, 3)
plt.text(0.5, 0.5, 'subplot(2,2,3)', ha='center', va='center', size=20, alpha=.5)
plt.subplot(2, 2, 4)
plt.text(0.5, 0.5, 'subplot(2,2,4)', ha='center', va='center', size=20, alpha=.5)

#%%
plt.figure(figsize=(6, 4))
plt.xticks()
plt.yticks()
plt.subplot(3, 3, 1)
plt.text(0.5, 0.5, 'subplot(3,3,1)', ha='center', va='center', size=10, alpha=.5)
plt.subplot(3, 3, 5)
plt.text(0.5, 0.5, 'subplot(3,3,5)', ha='center', va='center', size=10, alpha=.5)
plt.subplot(3, 3, 9)
plt.text(0.5, 0.5, 'subplot(3,3,9)', ha='center', va='center', size=10, alpha=.5)

#%%
plt.figure(figsize=(6, 4))
plt.xticks()
plt.yticks()
plt.axes([0.5, 0.5, 0.8, 0.8])
plt.axes([0.2, 0.2, 0.3, 0.3])

#%%
import numpy as np
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = (np.cos(x), np.sin(x))

plt.figure(figsize=(6, 4))
plt.xticks(np.linspace(-3, 3, 7))
plt.yticks(np.linspace(-1, 1, 9))

plt.subplot(2, 1, 1)
plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-")

plt.subplot(2, 1, 2)
plt.plot(x, s, color="red", linewidth=1.0, linestyle="-")

plt.axes([1, 0.125, 0.5, 0.75]) # なんとなく横に円を描いてみたかった
plt.xticks(np.linspace(-1, 1, 5))
plt.yticks(np.linspace(-1, 1, 5))
x = np.linspace(-np.pi, np.pi, 256)
y = np.linspace(-np.pi, np.pi, 256)
plt.plot(np.cos(x), np.sin(y))