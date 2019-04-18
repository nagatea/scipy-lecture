#%%
import numpy as np
def min_max(x, axis=None):
  min = x.min(axis=axis, keepdims=True)
  max = x.max(axis=axis, keepdims=True)
  res = (x-min)/(max-min)
  return res

#%%
def swap(data, i, j):
  for d in data:
    tmp = d[i]
    d[i] = d[j]
    d[j] = tmp

#%%
data = np.loadtxt('dataset.csv', delimiter=",", skiprows=1, usecols=(1,2,3,4,5,6,7,8))
for i in range(len(data[0])):
  data.T[i] = min_max(data.T[i])
data

#%%
import matplotlib.pyplot as plt
swap(data, 1, 2)
for d in data:
  plt.plot(d)

#%%
plt.savefig('figure.png')
