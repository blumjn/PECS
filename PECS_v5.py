import time
import threading
import config

from raith_setup_file import *
from area_setup_file import *
from pattern_creation_file import *
from exposure_t_file import *
from FoM_file import *
from plots_file import *

start_time=time.time()

#inputs:  (0) alpha [nm], (1) beta[nm], (2) eta [%]
#outputs: (0) alpha [nm], (1) beta [nm], (2) eta [%], (3) pixel_size [nm],
#         (4) beamstep [px], (5) dose [uC/cm2], (6) exposure [uC/cm2], (7) threshold[%]
raith = raith_setup(10,100,1.25)
print("Raith")
width = int(360/raith[3]) #width in nm/pixel size in nm = width in pixels as integer
height = int(2*raith[1]/raith[3]) #2*beta[nm]/pixel size in nm = height in pixels as integer
#inputs:  (0) width [px], (1) height[px]
#outputs: two 2D arrays, 1st for the pattern, 2nd for the exposure
#         both arrays have pixel size determined by raith[3]
pattern_shape, exposure_shape = area_setup(width,height)
print("Area Setup")
#inputs:  (0) 2D array, (1) its width [px], (2) its height [px], (3) nm/pixel [nm], (4) beamstep [px]
#outputs: 2D array of exposure shape
pattern = pattern_creation(pattern_shape,width,height,raith[3],raith[4])
print("Pattern Setup")
#inputs:  (0) 2D array with the pattern to be exposed, (1) 2D array for the exposure, (2) its width [px],
#         (3) its height [px], (4-11) the machine parameters)
#outputs: 2D array of exposure shape and amount
print("Starting Exposure Calculation")

t0 = threading.Thread(target=exposure_t0, args=(pattern,exposure_shape,width,height,*raith))
t1 = threading.Thread(target=exposure_t1, args=(pattern,exposure_shape,width,height,*raith))
t2 = threading.Thread(target=exposure_t2, args=(pattern,exposure_shape,width,height,*raith))
t3 = threading.Thread(target=exposure_t3, args=(pattern,exposure_shape,width,height,*raith))
t4 = threading.Thread(target=exposure_t4, args=(pattern,exposure_shape,width,height,*raith))
t5 = threading.Thread(target=exposure_t5, args=(pattern,exposure_shape,width,height,*raith))
t6 = threading.Thread(target=exposure_t6, args=(pattern,exposure_shape,width,height,*raith))
t7 = threading.Thread(target=exposure_t7, args=(pattern,exposure_shape,width,height,*raith))

t0.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()

t0.join()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()

exposed_map = config.exposed_map_0+config.exposed_map_1+config.exposed_map_2+config.exposed_map_3+config.exposed_map_4+config.exposed_map_5+config.exposed_map_6+config.exposed_map_7
print("Exposure Calculation")

#Finds which regions will fully develop and sets them equal to 1
#multiplication by the resolution is a temporary fix to make changing the resolution not significantly change the results
developed_map = (exposed_map/raith[6]>raith[7])

#inputs: (0) thresholded exposure map, (1) width [px], (2) height [px], (3) pixel size [nm/pixel]
#outputs: (0-n) figures of merit (n+1) a crosscut at x=0
lw, gap, crosscut = FoM(developed_map,width,height,raith[3])
print("Linewidth = ", lw, "; Gap = ", gap)

print("Runtime: ",(time.time()-start_time)," s")

#output plots
#tickspacing = 50
#xrange = int(width*raith[3])
#yrange = int(height*raith[3])

#inputs: (0) tickspacing [nm] (1) plots xrange [nm] (2) plots yrange [nm], (3) pixel size [nm/pixel]
#        (4) 2D pattern array, (5) 2D exposure map array (scaled to exposure) (6) 2D developed map (thresholded)
#        (7) crosscut at x=0 (thresholded)
#plots(tickspacing, xrange, yrange, raith[3], pattern, exposed_map/raith[6], developed_map, crosscut)




