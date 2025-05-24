pattern_shape = []
exposure_shape = []
exposed_map = []
pattern_map = []
developed_map = []
perfect_map = []
overlap_map = []

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