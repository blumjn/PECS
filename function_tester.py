import time

from swarm_feeder_v1 import *

start_time=time.time()
lw, gap = PECS_feeder(10,100,1.25)

print("Linewidth = ", lw, "; Gap = ", gap)
print("Runtime: ",(time.time()-start_time)," s")