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
import pandas as pd
master_data = pd.read_csv('dataset.csv')
use_data = master_data.drop("Date", axis=1).drop("Diary", axis=1)
use_data.head()


#%%
data = np.array(use_data)
for i in range(len(data[0])):
  data.T[i] = min_max(data.T[i])
data

#%%
import matplotlib.pyplot as plt
swap(data, 1, 2)
for d in data:
  plt.plot(d)
plt.savefig('figure.png')

#%%
# とりあえず散布図行列を作ってみる
import seaborn as sns
import pandas as pd

# kind="reg" でliner regression
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
g = sns.pairplot(use_data, kind="reg")
plt.savefig('pairplot.png')
