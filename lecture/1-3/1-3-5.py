#%%
import numpy as np
a = np.arange(1, 16).reshape((3, 5)).T
a

#%%
b = a[1:4:2]
b

#%%
from scipy import misc
face = misc.face()
face

#%%
import matplotlib.pyplot as plt
%matplotlib inline
plt.imshow(face) 

#%%
crop_face = face[100:-100, 100:-100]
plt.imshow(crop_face)

#%%
sy, sx, sz = face.shape
y, x = np.ogrid[0:sy, 0:sx]
y.shape, x.shape


#%%
centerx, centery = (660, 300)
mask = ((y- centery)**2 + (x - centerx)**2) > 230**2
face = face.copy()
face[mask] = 0
plt.imshow(face)

#%%
data = np.loadtxt('population.txt')
data

#%%
year, hares, lynxes, carrots = data.T
year

#%%
plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, hares, year, lynxes, year, carrots)
plt.legend(('Hare', 'Lynx', 'Carrot'))

#%%
def compute_mandelbrot(N_max, some_threshold, nx, ny):
  x = np.linspace(-2, 1, nx)
  y = np.linspace(-1.5, 1.5, ny)
  c = x[:, np.newaxis]+ 1j*y[np.newaxis, :]
  z = 0
  for j in range(N_max):
    z = z**2 + c
  mandelbrot_set = (np.abs(z) < some_threshold)
  return mandelbrot_set

mandelbrot_set = compute_mandelbrot(50, 50, 1000, 1000)
plt.gray()
plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])

