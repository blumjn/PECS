#! /usr/bin/python3

##--------------------------------------------------------------------\
#   PECS
#   '.src/obj_func/configs_F.py'
#   Constant values for objective function. Formatted for
#       automating objective function integration
#
#
#   Author(s): Lauren Linkous, Jonathan Lundquist, Josh Blum
#   Last update: December 11, 2025
##--------------------------------------------------------------------\
import sys
import conf.config as c
try: # for outside func calls

    sys.path.insert(0, './PECS/src/')
    from obj_func.swarm_feeder_v3 import PECS_feeder
    from obj_func.constr_F import constr_F
except: # for local
    from obj_func.swarm_feeder_v3 import PECS_feeder
    from obj_func.constr_F import constr_F


OBJECTIVE_FUNC = PECS_feeder
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "PECS_feeder"
CONSTR_FUNC_NAME = "constr_F"

# problem dependent variables
LB = [[15,10,50,60,2,4,1,70,22,2,0,0,0,.5,.25,.25,.25,.25,.25]]       # Lower boundaries for input
UB = [[25,22,70,80,14,16,10,86,38,16,8,10,10,2,1,1,1,2,2]]          # Upper boundaries for input
IN_VARS = 19                 # Number of input variables (x-values)
OUT_VARS = 2                # Number of output variables (y-values)
TARGETS = [16, 0]            # Target values for output
GLOBAL_MIN = None           # Global minima, if they exist