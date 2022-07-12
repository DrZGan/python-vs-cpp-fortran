import numpy as np
import time

npoints = 1000

u_xy = np.zeros([npoints, npoints])
added = np.ones([npoints, npoints])

start = time.time()
for iter in range(2000):

    for i in range(1,npoints-1):
        for j in range(1,npoints-1):
            u_xy[i,j] = u_xy[i,j]*0.1 + added[i,j]

end = time.time()
print(f"Python for-loop solver took {end - start} second")
