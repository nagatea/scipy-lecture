#%% [markdown]
# ## Advanced operations

#%%
import numpy as np
p = np.poly1d([3, 2, -1]) # 3x^2 + 2x - 1
p(0)

#%%
p.roots

#%%
p(-1)

#%%
%matplotlib inline
import matplotlib.pyplot as plt
x = np.linspace(0, 1, 20)
x

#%%
y = np.cos(x) + 0.3*np.random.rand(20)
y

#%%
p = np.poly1d(np.polyfit(x, y, 3))
p

#%%
t = np.linspace(0, 1, 200)
plt.plot(x, y, 'o', t, p(t), '-')

#%%
x = np.linspace(-1, 1, 2000)
y = np.cos(x) + 0.3*np.random.rand(2000)
p = np.polynomial.Chebyshev.fit(x, y, 90) # いろいろな多項式の例としてチェビシェフ基底関数
t = np.linspace(-1, 1, 200)
plt.plot(x, y, 'r.')
plt.plot(t, p(t), 'k-', lw=3)

#%% 
data = np.loadtxt('example.txt')
data

#%%
img = plt.imread('example.jpeg')
img.shape

#%%
plt.imshow(img)

#%%
plt.imshow(img[::10, ::10])
