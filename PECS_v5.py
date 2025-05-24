import time

from swarm_feeder_v3 import *

start_time=time.time()
X = [20,16,60,70,8,10,5,78,30,8,2,5,4,1,.5,.5,.5,.75,.75]

F, noErrors = PECS_feeder(X, 1)

print(F)
print("Runtime: ",(time.time()-start_time)," s")

if 1:
  plot_shapes()