#! /usr/bin/python3

##--------------------------------------------------------------------\
#   PECS
#   '.src/obj_func/PECS_v5.py'
#
#
#   Author(s):  Josh Blum, Lauren Linkous
#   Last update: December 11, 2025
##--------------------------------------------------------------------\

import time

from obj_func.swarm_feeder_v3 import PECS_feeder # instaed of * so we're explicitly pulling PECS_feeder from v3 
from obj_func.PECS_v5 import plot_shapes

start_time=time.time()
X = [20,16,60,70,8,10,5,78,30,8,2,5,4,1,.5,.5,.5,.75,.75]

F, noErrors = PECS_feeder(X, 1)

print(F)
print("Runtime: ",(time.time()-start_time)," s")

if 1:
  plot_shapes()