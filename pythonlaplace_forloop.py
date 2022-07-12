import numpy as np
import time

npoints = 1000

u_xy = np.ones([npoints, npoints])
u_xy_laplace = np.ones([npoints, npoints])
start = time.time()
for iter in range(2000):

    for i in range(1,npoints-1):
        for j in range(1,npoints-1):
            u_xy_laplace[i,j] = u_xy[i+1,j] - 2*u_xy[i,j] + u_xy[i-1,j] + u_xy[i,j+1] - 2*u_xy[i,j] + u_xy[i,j-1]

end = time.time()
print(f"Python for-loop solver took {end - start} second")
