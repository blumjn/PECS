#! /usr/bin/python3

pattern_shape = []
exposure_shape = []
exposed_map = []
pattern_map = []
developed_map = []
perfect_map = []
overlap_map = []
pixels = []
pix_LB = []
pix_UB = []

#machine variables
dose = 480 #dose in uC/cm^2, gets adjusted based on beamstep at start of run
beamstep_px = [] #converts beamstep to be in terms of pixels instead of nm, set at start of run
width = 288 #set this as width in nm, becomes width in pixels as integer, set at start of run
height = 288 #set this as width in nm, becomes width in pixels as integer, set at start of run
alpha = 11.314 #forward beam size in nm (gaussian)
beta = 2291 #scattered beam size in nm (gaussian)
gamma = 195.7 #coulomb scattering size (exponential)
eta = 0.688 #effectiveness of scattered beam in %
v = 3.3 #effectiveness of coulomb scattering
threshold = 208.2 #dose threshold for full development
etch = 2 #side etch in nm
charge_rad = 56 #nm radius for charge to effect PSF

## Shape defining parameters
#[20,16,60,70,8,10,5,78,30,8,1,1,1]
gap_height = 20
gap_width = 16
antenna_height = 60
antenna_width = 70

ci = [8,10] #inner circle centers
ri = 5 #inner circle radii
co = [78,30] #outer circle centers
ro = 8 #outer circle radii

d1_w = 2 #top and bottom border width
d2_w = 5 #outside border width
d3_w = 4 #inside border width

d0 = 1 #main trapezoid dose factor
d1 = .5 #top and bottom border dose
d2 = .5 #outside border dose
d3 = .5 #inside border dose
di = .75 #inner circle dose factor
do = .75 #outer circle dose factor