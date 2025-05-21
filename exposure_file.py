def exposure(pattern,exposure_shape,col,row,a,b,n,pixel_size,beamstep,dose,exposure,threshold):
    import numpy as np
    import math as m

#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,col*pixel_size,col, dtype='float32')
    y = np.linspace(0,row*pixel_size,row, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(row):
        for j in range(col):
            if pattern[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+pattern[i][j]*(dose/(m.pi*(1+n)))*((1/(a**2))*np.exp(-0.5*(r**2)/(a**2))+(n/(b**2))*np.exp(-0.5*(r**2)/(b**2)))
    
    return exposure_shape