
#This file sets up the raith and is where the parameters such as pixel size and beamstep get set

alpha = 16 #forward beam size in nm
beta = 1500 #scattered beam size in nm
eta = 0.5 #effectiveness of scattered beam in %

pixel_size = 1 #length of 1 pixel in nm, must be <= beamstep
beamstep_nm = 1 #beam step in nm, must be >= and divisible by pixel_size
dose = 400 #dose in uC/cm^2, gets adjusted based on beamstep at start of run
threshold = 175 #dose threshold for full development
beamstep_px = [] #converts beamstep to be in terms of pixels instead of nm, set at start of run

width = 200 #set this as width in nm, becomes width in pixels as integer, set at start of run
height = 200 #set this as width in nm, becomes width in pixels as integer, set at start of run

nt = 16 #number of threads allowed for multithreading of exposure

## Shape defining parameters
gap_height = 20
gap_width = 16
antenna_height = 60
antenna_width = 70

## plotting constants
tickspacing = 25