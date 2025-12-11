import config as c
import global_variables as g
import numpy as np
from PECS_functions import *
import csv
import os

g.width = int(g.width/c.pixel_size)
g.height = int(g.height/c.pixel_size)
g.dose = c.dose*(c.beamstep_nm**2)
g.beamstep_px = int(c.beamstep_nm/c.pixel_size) 

#         both arrays have pixel size determined by raith[3]
area_setup()

#inputs:  (0) 2D array, (1) its width [px], (2) its height [px], (3) nm/pixel [nm], (4) beamstep [px]
#outputs: 2D array of exposure shape
pattern_creation_antenna_combined()

#inputs:  (0) 2D array with the pattern to be exposed, (1) 2D array for the exposure, (2) its width [px],
#         (3) its height [px], (4-11) the machine parameters)
#outputs: none, but it updates config.exposed_map with the... exposed map
split_exposure()

#Finds which regions will fully develop and sets them equal to 1
g.developed_map = (g.exposed_map>c.threshold)
#inputs: (0) thresholded exposure map, (1) width [px], (2) height [px], (3) pixel size [nm/pixel]
#outputs: (0-n) figures of merit (n+1) a crosscut at x=0
side_etch()
# with open(os.path.join(c.folder, c.filename), 'w', newline = "") as logfile:
#     logwriter = csv.writer(logfile, delimiter = ",")
#     logwriter.writerow(["alpha","beta","gamma","eta","v","threshold","etch","charge_rad","Wrong_Pixels", "Width1", "Gap1", "Width2"])
# dataline = [g.alpha,g.beta,g.gamma,g.eta,g.v,g.threshold,g.etch,g.charge_rad,F[0], F[1], F[2], F[3]]
# with open(os.path.join(c.folder, c.filename), 'a', newline = "") as logfile:
#     logwriter = csv.writer(logfile, delimiter = ",")
#     logwriter.writerow(dataline)
print(FoM())
plot_shapes(0)