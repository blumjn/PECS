def area_setup(x,y):
    import numpy as np
#This function sets up the empty arrays for both the pattern and the resulting exposure
#x,y in terms of pixels, not nm

#pattern is most likely a lower resolution than the exposure and is based on the Raith stepsize
    pattern_row, pattern_col = (x, y)
    exposure_row, exposure_col = (x, y)

#creates the 2D arrays
    pattern_shape = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)])
    exposure_shape = np.array([[0 for j in range(exposure_row)] for i in range(exposure_col)])

    return pattern_shape, exposure_shape