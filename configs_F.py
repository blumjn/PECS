#! /usr/bin/python3

##--------------------------------------------------------------------\
#   pso_python
#   '.src/lundquist_3_var/configs_F.py'
#   Constant values for objective function. Formatted for
#       automating objective function integration
#
#
#   Author(s): Lauren Linkous, Jonathan Lundquist
#   Last update: May 25, 2024
##--------------------------------------------------------------------\
import sys
import config as c
try: # for outside func calls
    sys.path.insert(0, './pso_python/src/')
    from swarm_feeder_v6 import PECS_feeder
    from constr_F import constr_F
except: # for local
    from swarm_feeder_v6 import PECS_feeder
    from constr_F import constr_F

OBJECTIVE_FUNC = PECS_feeder
CONSTR_FUNC = constr_F
OBJECTIVE_FUNC_NAME = "PECS_feeder"
CONSTR_FUNC_NAME = "constr_F"

# problem dependent variables
#    ["d0","x1","y1","x2","y2","x3","y3","x4","y4","x5","y5"]
# LB = [[0.675,  7.875,  0,   8.45,   8.925,  51.975,  25.35,  79.275,  42.075,  78.9,   0]]       # Lower boundaries for input 
# UB = [[1.125, 13.125,  0, 14.125,  14.875,  86.625,  42.25, 132.125,  70.125, 131.5,   0]]          # Upper boundaries for input
#    ["width","theta","gap","d0","x1","y1","r1","d1","x2","y2", "r2","d2"]
# LB = [[102.4,   46,   16,   .98,  8,   12,  2.3,   3.9,   103,  50,   3.4,   4.45]]       # Lower boundaries for input 
# UB = [[103.4,   48,   20,  1.18, 12,   16,  4.3,   4.1,   107,  54,   5.4,   4.65]]          # Upper boundaries for input

#    [   "d0",  "d1",    "d2",   "r1", "r2",     "x1",  "y1",   "x2",    "y2",  "x3",    "y3",     "x4",  "y4",     "x5", "y5"]
LB = [[0.8775, 2.535,  3.4125, 3.0225, 1.95,  12.1875,     0,  8.775,  4.3875, 67.08, 32.4675,  104.325, 48.75,   103.74,   0]]       # Lower boundaries for input 
UB = [[0.9225, 2.665,  3.5875, 3.1775, 2.05,  12.8125,     0,  9.225,  4.6125, 70.52, 34.1325,  109.675, 51.25,   109.06,   0]]          # Upper boundaries for input


IN_VARS = 15                # Number of input variables (x-values)
OUT_VARS = 1                # Number of output variables (y-values)
TARGETS = [0] # Target values for output
GLOBAL_MIN = None           # Global minima, if they exist