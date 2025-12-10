#! /usr/bin/python3

##--------------------------------------------------------------------\
#   pso_python
#   './pso_python/src/main_test.py'
#   Test function/example for using the 'swarm' class in particle_swarm.py.
#       This has been modified from the original to include message 
#       passing back to the parent class or testbench, rather than printing
#       error messages directly from the 'swarm' class. Format updates are 
#       for integration in the AntennaCAT GUI.
#
#   Author(s): Jonathan Lundquist, Lauren Linkous
#   Last update: March 12, 2025
##--------------------------------------------------------------------\

import pandas as pd
import numpy as np
import os
from particle_swarm import swarm
import time
from swarm_feeder_v6 import *

# OBJECTIVE FUNCTION SELECTION
#import one_dim_x_test.configs_F as func_configs     # single objective, 1D input
#import himmelblau.configs_F as func_configs         # single objective, 2D input
import configs_F as func_configs     # multi objective function

start_time=time.time()
if __name__ == "__main__":
    # Constant variables
    NO_OF_PARTICLES = 11        # Number of particles in swarm
    #T_MOD = 1                 # Variable time-step extinction coefficient
    TOL = 10 ** -10              # Convergence Tolerance
    MAXIT = 11000             # Maximum allowed iterations
    BOUNDARY = 1                 # int boundary 1 = random,      2 = reflecting
                                    #              3 = absorbing,   4 = invisible

    # Objective function dependent variables
    func_F = func_configs.OBJECTIVE_FUNC  # objective function
    constr_F = func_configs.CONSTR_FUNC   # constraint function

    LB = func_configs.LB              # Lower boundaries, [[0.21, 0, 0.1]]
    UB = func_configs.UB              # Upper boundaries, [[1, 1, 0.5]]   
    OUT_VARS = func_configs.OUT_VARS  # Number of output variables (y-values)
    TARGETS = func_configs.TARGETS    # Target values for output

    # target format. TARGETS = [0, ...] 

    # threshold is same dims as TARGETS
    # 0 = use target value as actual target. value should EQUAL target
    # 1 = use as threshold. value should be LESS THAN OR EQUAL to target
    # 2 = use as threshold. value should be GREATER THAN OR EQUAL to target
    #DEFAULT THRESHOLD
    THRESHOLD = np.zeros_like(TARGETS) 
    #THRESHOLD = np.ones_like(TARGETS)
    #THRESHOLD = [0,0,0,0,0]


    # optimizer constants
    #WEIGHTS = [[0.5, 0.7, 0.78]]       # original vector weights
    WEIGHTS = [[0.5, 0.7, 0.78]]        # Actual vector weights
    VLIM = .25                       # Initial velocity limit as a fraction of the variation in each input


    best_eval = 1e22
    parent = None             # for the optimizer test ONLY
    evaluate_threshold = True # use target or threshold. True = THRESHOLD, False = EXACT TARGET
    suppress_output = True    # Suppress the console output of particle swarm
    allow_update = True       # Allow objective call to update state 


    # Constant variables in a list format
    opt_params = {'NO_OF_PARTICLES': [NO_OF_PARTICLES], # Number of particles in swarm
                #'T_MOD': [T_MOD],                       # Variable time-step extinction coefficient
                'BOUNDARY': [BOUNDARY],                 # int boundary 1 = random,      2 = reflecting
                                                        #              3 = absorbing,   4 = invisible
                'WEIGHTS': [WEIGHTS],                   # Update vector weights
                'VLIM':  [VLIM] }     
    # dataframe conversion
    opt_df = pd.DataFrame(opt_params)

    # optimizer initialization
    myOptimizer = swarm(LB, UB, TARGETS, TOL, MAXIT,
                            func_F, constr_F,
                            opt_df,
                            parent=parent, 
                            evaluate_threshold=evaluate_threshold, obj_threshold=THRESHOLD)  
    #creates the log files
    with open(os.path.join(c.folder, c.filename), 'w', newline = "") as logfile:
            logwriter = csv.writer(logfile, delimiter = ",")
            logwriter.writerow(["d0","d1","d2","r1","r2", "x1","y1","x2", "y2", "x3", "y3",  "x4",  "y4",  "x5", "y5","WrongPixels"])
    
    oldfilename=c.filename
    c.filename="best_results_"+c.filename
    with open(os.path.join(c.folder, c.filename), 'w', newline = "") as logfile:
            logwriter = csv.writer(logfile, delimiter = ",")
            logwriter.writerow(["d0","d1","d2","r1","r2", "x1","y1","x2", "y2", "x3", "y3",  "x4",  "y4",  "x5", "y5","WrongPixels"])
    c.filename = oldfilename


    while not myOptimizer.complete():
  
        # step through optimizer processing
        # this will update particle or agent locations

        myOptimizer.step(suppress_output)

        # call the objective function, control 
        # when it is allowed to update and return 
        # control to optimizer
        myOptimizer.call_objective(allow_update)

        # check the current progress of the optimizer
        # iter: the number of objective function calls
        # eval: current 'best' evaluation of the optimizer
        iter, eval = myOptimizer.get_convergence_data()

        if (eval <= best_eval) and (eval != 0):
            best_eval = eval

        # optional. if the optimizer is not printing out detailed 
        # reports, preview by checking the iteration and best evaluation

        if suppress_output:
       
            if iter%NO_OF_PARTICLES == 0 and iter > 1 and iter<= 500:
                print("Current Runtime")
                print(time.time()-start_time)
                print("Iteration")
                print(iter)
                print("Best Eval")
                print(best_eval)
                #print(myOptimizer.get_optimized_soln())
                print(myOptimizer.get_optimized_outs())
                oldfilename=c.filename
                c.filename="best_results_"+c.filename
                X = myOptimizer.get_optimized_soln()
                #look. I don't like dealing with data structures. This works. It's fine.
                X = np.array([float(X[0][0]),float(X[1][0]),float(X[2][0]),float(X[3][0]),float(X[4][0]),float(X[5][0]),float(X[6][0]),float(X[7][0]),\
                              float(X[8][0]),float(X[9][0]),float(X[10][0]),float(X[11][0]),float(X[12][0]),float(X[13][0]),float(X[14][0])])
                PECS_feeder(X, 1)
                plot_shapes(iter)
                c.filename=oldfilename
            if iter%(10*NO_OF_PARTICLES) ==0 and iter > 500 and iter<= 5000: #print out every 250th iteration update
                print("Current Runtime")
                print(time.time()-start_time)
                print("Iteration")
                print(iter)
                print("Best Eval")
                print(best_eval)
                #print(myOptimizer.get_optimized_soln())
                print(myOptimizer.get_optimized_outs())
                oldfilename=c.filename
                c.filename="best_results_"+c.filename
                X = myOptimizer.get_optimized_soln()
                X = np.array([float(X[0][0]),float(X[1][0]),float(X[2][0]),float(X[3][0]),float(X[4][0]),float(X[5][0]),float(X[6][0]),float(X[7][0]),\
                              float(X[8][0]),float(X[9][0]),float(X[10][0]),float(X[11][0]),float(X[12][0]),float(X[13][0]),float(X[14][0])])                
                PECS_feeder(X, 1)
                plot_shapes(iter)
                c.filename=oldfilename
            if iter%(100*NO_OF_PARTICLES) ==0 and iter > 5000: #print out every 2500th iteration update
                print("Current Runtime")
                print(time.time()-start_time)
                print("Iteration")
                print(iter)
                print("Best Eval")
                print(best_eval)
                #print(myOptimizer.get_optimized_soln())
                print(myOptimizer.get_optimized_outs())
                oldfilename=c.filename
                c.filename="best_results_"+c.filename
                X = myOptimizer.get_optimized_soln()
                X = np.array([float(X[0][0]),float(X[1][0]),float(X[2][0]),float(X[3][0]),float(X[4][0]),float(X[5][0]),float(X[6][0]),float(X[7][0]),\
                              float(X[8][0]),float(X[9][0]),float(X[10][0]),float(X[11][0]),float(X[12][0]),float(X[13][0]),float(X[14][0])])                
                PECS_feeder(X, 1)
                plot_shapes(iter)
                c.filename=oldfilename

            # print(myOptimizer.weights)
            # print(type(myOptimizer.weights))
            #myOptimizer.weights=[] #self.weights = np.array(weights)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Optimized Solution")
    print(myOptimizer.get_optimized_soln())
    print("Optimized Outputs")
    print(myOptimizer.get_optimized_outs())

    X = myOptimizer.get_optimized_soln()

    X = np.array([float(X[0][0]),float(X[1][0]),float(X[2][0]),float(X[3][0]),float(X[4][0]),float(X[5][0]),float(X[6][0]),float(X[7][0]),\
                          float(X[8][0]),float(X[9][0]),float(X[10][0]),float(X[11][0]),float(X[12][0]),float(X[13][0]),float(X[14][0])])
    print(X)

    PECS_feeder(X, 1)
    # I run this again just to make sure the best final info is logged
