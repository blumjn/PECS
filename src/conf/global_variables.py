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
x1 = 12.5
y1 = 0
x2 = 9
y2 = 5.7
x3 = 68.3
y3 = 33
x4 = 106.1
y4 = 49.6
x5 = 105.1
y5 = 0

gap_width = 18 #nm
antenna_width = 103.4 #nm, measured from center
antenna_angle = 47 #deg, full angle NOT from y=0
d0 = 0.9

r1 = 3.2
r2 = 2
d1 = 2.6
d2 = 3.2

outer_square = 200 #outer square in nm
donut_square = 150 #inner of outer in nm
inner_square = 100 # inner square in nm

# r1 = 20
# r2 = 17
# r3 = 19
# w1 = 104
# w2 = 71
#w3 = 38