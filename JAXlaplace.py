import jax
import jax.numpy as np
import time

@jax.jit
def laplace():
    u_ij = u_xy[1:-1,1:-1]
    u_ip1j = u_xy[2:,1:-1]
    u_im1j = u_xy[0:-2,1:-1]
    u_ijp1 = u_xy[1:-1,2:]
    u_ijm1 = u_xy[1:-1,0:-2]

    u_xy_laplace = u_ip1j - 2*u_ij + u_im1j + u_ijp1 - 2*u_ij + u_ijm1 

npoints = 1000

u_xy = np.zeros([npoints, npoints])

start = time.time()
for iter in range(2000):
  laplace()


end = time.time()
print(f"JAX solver took {end - start} second")