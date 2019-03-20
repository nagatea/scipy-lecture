#%% [markdown]
# ## Numerical operations on arrays


#%%
import numpy as np
a = np.arange(0, 6)
a

#%%
a * 2

#%%
a ** 2

#%%
b = np.arange(0, 6)
b

#%%
a == b

#%%
np.array_equal(a, b)

#%%
np.sin(a)

#%%
np.exp(a)

#%%
a = np.triu(np.ones((3, 3)))
a

#%%
a.T # 転置行列

#%%
a = np.arange(1, 6) + np.arange(10, 51, 10)[:, np.newaxis]
a

#%%
a.sum()

#%%
a.sum(0) # columnの足し算

#%%
a.sum(1) # rowの足し算

#%%
a.min()

#%%
a.max()

#%%
a.mean()

#%%
a.mean(1)

#%%
a = np.tile(np.arange(10, 50, 10), (4, 1))
a

#%%
b = a.T
b

#%%
b + np.arange(1, 5)

#%%
x, y = np.arange(5), np.arange(5)[:, np.newaxis]
distance = np.sqrt(x**2 + y**2)
distance

#%%
%matplotlib inline
import matplotlib.pyplot as plt
plt.pcolor(distance)
plt.colorbar()

#%%
x, y = np.ogrid[0:5, 0:5]
x

#%%
x * y

#%%
a = np.array([[1, 2, 3], [4, 5, 6]])
a

#%%
a.reshape((3, 2))

#%%
a.reshape((6, 1))
