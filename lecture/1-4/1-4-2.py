#%%
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = (np.cos(x), np.sin(x))
plt.plot(x, c, x, s)

#%%
plt.figure(figsize=(8, 6), dpi=80)

#%%
plt.subplot(1, 1, 1)

#%%
plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-")
plt.plot(x, s, color="red", linewidth=1.0, linestyle="-")

#%%
plt.xlim(-4.0, 4.0)
plt.ylim(-1.0, 1.0)
plt.xticks(np.linspace(-4, 4, 17, endpoint=True))
plt.yticks(np.linspace(-1, 1, 9, endpoint=True))
plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-")
plt.plot(x, s, color="red", linewidth=1.0, linestyle="-")
plt.show()

#%%
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ['a', 'b', 'c', 'd', 'e'])
plt.yticks([-1, 0, +1])
plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-")
plt.plot(x, s, color="red", linewidth=1.0, linestyle="-")
plt.show()

#%%
plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="cos(x)")
plt.plot(x, s, color="red", linewidth=1.0, linestyle="-", label="sin(x)")
plt.legend(loc='upper left')
plt.show()


#%%
plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="cos(x)")
plt.plot(x, s, color="red", linewidth=1.0, linestyle="-", label="sin(x)")
t = 2 * np.pi / 3
plt.scatter(t, np.cos(t), 50, color="blue")
plt.scatter(t, np.sin(t), 50, color="red")
plt.plot([t, t], [0, np.cos(t)], color="blue", linewidth=2.5, linestyle="--")
plt.plot([t, t], [0, np.sin(t)], color="red", linewidth=2.5, linestyle="--")
plt.annotate(r'$\sin(\frac{2\pi}{3})$', xy=(t, np.sin(t)))
plt.annotate(r'$\cos(\frac{2\pi}{3})$', xy=(t, np.cos(t)))
plt.show()
