
#This file sets up the raith and is where the parameters such as pixel size and beamstep get set

pixel_size = 1 #length of 1 pixel in nm, must be <= beamstep
beamstep_nm = 1 #beam step in nm, must be >= and divisible by pixel_size
dose = 480 #dose in uC/cm^2, gets adjusted based on beamstep at start of run
threshold = 200 #dose threshold for full development
beamstep_px = [] #converts beamstep to be in terms of pixels instead of nm, set at start of run

nt = 8 #number of threads allowed for multithreading of exposure

## Shape defining parameters
gap_width = 25 #nm
antenna_width = 102 #nm, measured from center
antenna_angle = 45.7 #deg, full angle NOT from y=0

## plotting constants
tickspacing = 50
folder = "plots_11_30_25_run1"
filename = "log.csv"