def exposure_t0(pattern,exposure_shape,col,row,a,b,n,pixel_size,beamstep,dose,exposure,threshold):
    import numpy as np
    import math as m
    import config


#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,col*pixel_size,col, dtype='float32')
    y = np.linspace(0,row*pixel_size,row, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(0,row,8):
        for j in range(col):
            if pattern[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+pattern[i][j]*(dose/(m.pi*(1+n)))*((1/(a**2))*np.exp(-0.5*(r**2)/(a**2))+(n/(b**2))*np.exp(-0.5*(r**2)/(b**2)))
    config.exposed_map_0 = exposure_shape
    return 
def exposure_t1(pattern,exposure_shape,col,row,a,b,n,pixel_size,beamstep,dose,exposure,threshold):
    import numpy as np
    import math as m
    import config


#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,col*pixel_size,col, dtype='float32')
    y = np.linspace(0,row*pixel_size,row, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(1,row,8):
        for j in range(col):
            if pattern[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+pattern[i][j]*(dose/(m.pi*(1+n)))*((1/(a**2))*np.exp(-0.5*(r**2)/(a**2))+(n/(b**2))*np.exp(-0.5*(r**2)/(b**2)))
    config.exposed_map_1 = exposure_shape
    return 

def exposure_t2(pattern,exposure_shape,col,row,a,b,n,pixel_size,beamstep,dose,exposure,threshold):
    import numpy as np
    import math as m
    import config


#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,col*pixel_size,col, dtype='float32')
    y = np.linspace(0,row*pixel_size,row, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(2,row,8):
        for j in range(col):
            if pattern[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+pattern[i][j]*(dose/(m.pi*(1+n)))*((1/(a**2))*np.exp(-0.5*(r**2)/(a**2))+(n/(b**2))*np.exp(-0.5*(r**2)/(b**2)))
    config.exposed_map_2 = exposure_shape
    return 

def exposure_t3(pattern,exposure_shape,col,row,a,b,n,pixel_size,beamstep,dose,exposure,threshold):
    import numpy as np
    import math as m
    import config


#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,col*pixel_size,col, dtype='float32')
    y = np.linspace(0,row*pixel_size,row, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(3,row,8):
        for j in range(col):
            if pattern[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+pattern[i][j]*(dose/(m.pi*(1+n)))*((1/(a**2))*np.exp(-0.5*(r**2)/(a**2))+(n/(b**2))*np.exp(-0.5*(r**2)/(b**2)))
    config.exposed_map_3 = exposure_shape
    return 

def exposure_t4(pattern,exposure_shape,col,row,a,b,n,pixel_size,beamstep,dose,exposure,threshold):
    import numpy as np
    import math as m
    import config


#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,col*pixel_size,col, dtype='float32')
    y = np.linspace(0,row*pixel_size,row, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(4,row,8):
        for j in range(col):
            if pattern[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+pattern[i][j]*(dose/(m.pi*(1+n)))*((1/(a**2))*np.exp(-0.5*(r**2)/(a**2))+(n/(b**2))*np.exp(-0.5*(r**2)/(b**2)))
    config.exposed_map_4 = exposure_shape
    return 

def exposure_t5(pattern,exposure_shape,col,row,a,b,n,pixel_size,beamstep,dose,exposure,threshold):
    import numpy as np
    import math as m
    import config


#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,col*pixel_size,col, dtype='float32')
    y = np.linspace(0,row*pixel_size,row, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(5,row,8):
        for j in range(col):
            if pattern[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+pattern[i][j]*(dose/(m.pi*(1+n)))*((1/(a**2))*np.exp(-0.5*(r**2)/(a**2))+(n/(b**2))*np.exp(-0.5*(r**2)/(b**2)))
    config.exposed_map_5 = exposure_shape
    return 

def exposure_t6(pattern,exposure_shape,col,row,a,b,n,pixel_size,beamstep,dose,exposure,threshold):
    import numpy as np
    import math as m
    import config


#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,col*pixel_size,col, dtype='float32')
    y = np.linspace(0,row*pixel_size,row, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(6,row,8):
        for j in range(col):
            if pattern[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+pattern[i][j]*(dose/(m.pi*(1+n)))*((1/(a**2))*np.exp(-0.5*(r**2)/(a**2))+(n/(b**2))*np.exp(-0.5*(r**2)/(b**2)))
    config.exposed_map_6 = exposure_shape
    return 

def exposure_t7(pattern,exposure_shape,col,row,a,b,n,pixel_size,beamstep,dose,exposure,threshold):
    import numpy as np
    import math as m
    import config


#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,col*pixel_size,col, dtype='float32')
    y = np.linspace(0,row*pixel_size,row, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(7,row,8):
        for j in range(col):
            if pattern[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+pattern[i][j]*(dose/(m.pi*(1+n)))*((1/(a**2))*np.exp(-0.5*(r**2)/(a**2))+(n/(b**2))*np.exp(-0.5*(r**2)/(b**2)))
    config.exposed_map_7 = exposure_shape
    return 