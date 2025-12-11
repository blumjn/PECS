#! /usr/bin/python3

##--------------------------------------------------------------------\
#   PECS
#   '.src/obj_func/swarm_feeder_v3.py'
#
#
#   Author(s):  Josh Blum
#   Last update: December 11, 2025
##--------------------------------------------------------------------\


import config as c
import global_variables as g
import numpy as np
from PECS_functions import *

def PECS_feeder(X, NO_OF_OUTS):
    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
      
        c.dose = c.dose*(c.beamstep_nm**2)
        c.beamstep_px = int(c.beamstep_nm/c.pixel_size)
        c.width = int(c.width/c.pixel_size)
        c.height = int(c.height/c.pixel_size) 

        g.gap_height = X[0]
        g.gap_width = X[1]
        g.antenna_height = X[2]
        g.antenna_width = X[3]

        g.ci = [X[4],X[5]]
        g.ri = X[6]
        g.co = [X[7],X[8]]
        g.ro = X[9]

        g.d1_w = X[10] #top and bottom border width
        g.d2_w = X[11] #outside border width
        g.d3_w = X[12] #inside border width

        g.d0 = X[13] #main trapezoid dose factor
        g.d1 = X[14] #top and bottom border dose
        g.d2 = X[15] #outside border dose
        g.d3 = X[16] #inside border dose
        g.di = X[17] #inner circle dose factor
        g.do = X[18] #outer circle dose factor

        #inputs:  (0) width [px], (1) height[px]
        #outputs: two 2D arrays, 1st for the pattern, 2nd for the exposure
        #         both arrays have pixel size determined by raith[3]
        area_setup()
  
        #inputs:  (0) 2D array, (1) its width [px], (2) its height [px], (3) nm/pixel [nm], (4) beamstep [px]
        #outputs: 2D array of exposure shape

        pattern_creation_antennas()

        #inputs:  (0) 2D array with the pattern to be exposed, (1) 2D array for the exposure, (2) its width [px],
        #         (3) its height [px], (4-11) the machine parameters)
        #outputs: none, but it updates config.exposed_map with the... exposed map

        split_exposure()

        #Finds which regions will fully develop and sets them equal to 1
        g.developed_map = (g.exposed_map>c.threshold)
   
        #inputs: (0) thresholded exposure map, (1) width [px], (2) height [px], (3) pixel size [nm/pixel]
        #outputs: (0-n) figures of merit (n+1) a crosscut at x=0
        F = FoM()   
    except:
        noErrors = False

    return F, noErrors