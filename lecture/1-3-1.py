#%% [markdown]
# ## The NumPy array object
#%%
import numpy as np
a = np.array([0, 1, 2, 3])
a

#%%
a.ndim

#%%
a.shape

#%%
type(a.shape)

#%%
len(a)

#%%
b = np.array([[0, 1, 2], [3, 4, 5]])
b

#%%
b.ndim

#%%
b.shape

#%%
len(b)

#%%
c = np.arange(0, 100, 10) # array_rangeの略？
c

#%%
d = np.linspace(0, 1, 5)
d

#%%
a = np.ones((3, 3)) # shapeとなるtupleを渡している
a

#%%
b = np.zeros((2, 5))
b

#%%
c = np.eye(5)
c

#%%
d = np.diag(np.array([1, 2, 3, 4, 5]))
d

#%%
a = np.random.rand(4)
a

#%%
b = np.random.randn(4) # 正規分布
b

#%%
%matplotlib inline
import matplotlib.pyplot as plt

#%%
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)
plt.plot(x, y, 'o') # 点が重ねて表示される

#%%
a = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
a

#%%
a[1, :]

#%%
a[:, 1]

#%%
a[1:, 1:] # PythonのArrayの":"はstart:stop:stepの関係がある

#%%
b = np.arange(10, 51, 10)[:, np.newaxis]
b

#%%
c = np.arange(1, 6)
c

#%%
b + c

#%%
a = np.arange(0, 100, 10)
a

#%%
a[[1, 1, 4, 5, 1, 4]]
