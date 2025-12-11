

import csv
import os
import numpy as np

import conf.config as c
import conf.global_variables as g

from obj_func.PECS_functions import *


def PECS_feeder(X, NO_OF_OUTS):

    F = np.zeros((NO_OF_OUTS))
    noErrors = True
    try:
        #these are vestigial. I want to make the pixel scaling work but right now things break if the pixels are not in 1 nm increments
        g.width = int(g.width/c.pixel_size)
        g.height = int(g.height/c.pixel_size)
        g.dose = c.dose*(c.beamstep_nm**2)
        g.beamstep_px = int(c.beamstep_nm/c.pixel_size) 
        #"width","theta","gap","d0","x1","y1","r1","d1","x2","y2", "r2","d2"
        g.d0 = X[0]
        g.d1 = X[1]
        g.d2 = X[2]
        g.r1 = X[3]
        g.r2 = X[4]
        g.x1 = X[5]
        g.y1 = X[6]
        g.x2 = X[7]
        g.y2 = X[8]
        g.x3 = X[9]
        g.y3 = X[10]
        g.x4 = X[11]
        g.y4 = X[12]
        g.x5 = X[13]
        g.y5 = X[14]
 
        area_setup() #creates a bunch of empty arrays of the correct sizes for the whole process

        #change this out for whichever shape you are testing. Note that each function requires a different input setup for the PSO
        pattern_creation_antenna_combined() #creates the pattern that will be exposed and the ideal map for comparison
     
        split_exposure() #steps through the actual exposure

        g.developed_map = (g.exposed_map>c.threshold) #develops the exposure

        side_etch() #expands the exposed area slightly to match the plasma descum 
     
        F[0] = FoM() #counts the number of incorrect pixels

        dataline = [X[0], X[1], X[2], X[3],X[4], X[5], X[6], X[7], X[8], X[9],X[10],X[11],X[12],X[13],X[14], F[0]]
        with open(os.path.join(c.folder, c.filename), 'a', newline = "") as logfile:
            logwriter = csv.writer(logfile, delimiter = ",")
            logwriter.writerow(dataline)

    except:
        noErrors = False

    return F, noErrors