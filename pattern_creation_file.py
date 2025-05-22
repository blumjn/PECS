def pattern_creation(map,col,row,pixel_size,beamstep):
    import numpy as np
    import math as m
#creates arrays with values for x and y in terms of nm with 0 at center (offset by 1)
    x = np.linspace(-col*pixel_size/2,-beamstep+col*pixel_size/2,col, dtype='float64')
    y = np.linspace(-row*pixel_size/2,-beamstep+row*pixel_size/2,row, dtype='float64')
#steps through map and assigns a value of 1 if the position is within bounds
    for i in range(0, row, beamstep):
        for j in range(0, col, beamstep):
            if abs(x[j])>100 and abs(x[j])<140:
                map[i][j] = 1
                    
    return map
