import numpy as np
import time

def explicit_euler(state):
    '''
    Explict Euler method
    '''
    new_state = state * 0.1 + added
    
    return new_state

npoints = 1000

state = np.zeros([npoints, npoints])
added = np.ones([npoints, npoints])
start = time.time()
for iter in range(2000):
  state = explicit_euler(state)
  #print(state[500,500])


end = time.time()
print(f"JAX solver took {end - start} second")