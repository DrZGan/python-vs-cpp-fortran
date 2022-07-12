import numpy as np
import time
from scipy import signal

npoints = 1000 - 2

u_xy = np.ones([npoints, npoints])
kernal = np.array([[0, 1, 0], [1, -4, 1],[0, 1, 0]])

start = time.time()
for iter in range(2000):
    u_xy_laplace = signal.convolve2d(u_xy, kernal, boundary='symm', mode='same')

end = time.time()
print(f"Python convolution solver took {end - start} second")
