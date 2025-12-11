#! /usr/bin/python3

##--------------------------------------------------------------------\
#   PECS
#   '.src/obj_func/PECS_functions.py'
#
#
#   Author(s):  Josh Blum, Lauren Linkous
#   Last update: December 11, 2025
##--------------------------------------------------------------------\


import threading
import numpy as np
import math as m
import matplotlib.pyplot as plt

import conf.global_variables as g
import conf.config as c


def area_setup():

#This function sets up the empty arrays for both the pattern and the resulting exposure
#x,y in terms of pixels, not nm

#pattern is most likely a lower resolution than the exposure and is based on the Raith stepsize
    pattern_row, pattern_col = (c.width, c.height)

#creates the 2D arrays
    g.pattern_shape = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    g.exposure_shape = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    g.exposed_map = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    g.pattern_map = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    g.perfect_map = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    return

def FoM():

    g.overlap_map = np.logical_xor(g.developed_map,g.perfect_map)

#Takes a crosscut of the map at x=0 (actually offset by +-1)    
    crosscut = g.developed_map[int(c.height/2),:]

#If there are at least 4 exposed pixels, then there are two developed lines of non-unity width
#If the exposed pixels take up the whole space, then there is no gap 
    if sum(crosscut)>3 and sum(crosscut)<(c.width-4):
#turnpoints stores the indices where the step changes
        turnpoints = []

        for i in range(1,c.width,1):
#checks if the step has changed, stores the index if yes
            if (crosscut[i]^crosscut[i-1])==1:
                turnpoints.append(i)
 
#the first line width is the right hand pixel - the left hand pixel times the pixel size
#the gap is the left hand pixel of the second line minus the right hand pixel of the first times the pixel size
        lw = (turnpoints[1]-turnpoints[0])*c.pixel_size
        gap = (turnpoints[2]-turnpoints[1])*c.pixel_size
#If the number of exposed pixels is too great, assume that the lines take up the whole space and the gap is 0        
    elif sum(crosscut)>=(c.width-4):
        lw = c.width*c.pixel_size
        gap = 0
#If all else fails, assume that the lines did not develop at all
    else:
        lw = 0
        gap = c.width*c.pixel_size
    overlap = np.count_nonzero(g.overlap_map)
        
    return np.count_nonzero(g.overlap_map)

def FoM_lines():

#Takes a crosscut of the map at x=0 (actually offset by +-1)    
    crosscut = g.developed_map[int(c.height/2),:]

#If there are at least 4 exposed pixels, then there are two developed lines of non-unity width
#If the exposed pixels take up the whole space, then there is no gap 
    if sum(crosscut)>3 and sum(crosscut)<(c.width-4):
#turnpoints stores the indices where the step changes
        turnpoints = []

        for i in range(1,c.width,1):
#checks if the step has changed, stores the index if yes
            if (crosscut[i]^crosscut[i-1])==1:
                turnpoints.append(i)
 
#the first line width is the right hand pixel - the left hand pixel times the pixel size
#the gap is the left hand pixel of the second line minus the right hand pixel of the first times the pixel size
        lw = (turnpoints[1]-turnpoints[0])*c.pixel_size
        gap = (turnpoints[2]-turnpoints[1])*c.pixel_size
#If the number of exposed pixels is too great, assume that the lines take up the whole space and the gap is 0        
    elif sum(crosscut)>=(c.width-4):
        lw = c.width*c.pixel_size
        gap = 0
#If all else fails, assume that the lines did not develop at all
    else:
        lw = 0
        gap = c.width*c.pixel_size  


    return lw, gap, crosscut

def pattern_creation():

#creates arrays with values for x and y in terms of nm with 0 at center (offset by 1)
    x = np.linspace(-c.width*c.pixel_size/2,-c.beamstep_px+c.width*c.pixel_size/2,c.width, dtype='float64')
    y = np.linspace(c.height*c.pixel_size/2,c.beamstep_px-c.height*c.pixel_size/2,c.height, dtype='float64')
#steps through map and assigns a value of 1 if the position is within bounds
    for i in range(0, c.height, c.beamstep_px):
        for j in range(0, c.width, c.beamstep_px):
            if abs(x[j])>=100 and abs(x[j])<180:
                g.pattern_map[i][j] = 1                    
    return

def pattern_creation_antennas():

#creates arrays with values for x and y in terms of nm with 0 at center (offset by 1)
    x = np.linspace(-c.width*c.pixel_size/2,-c.beamstep_px+c.width*c.pixel_size/2,c.width, dtype='float64')
    y = np.linspace(c.height*c.pixel_size/2,c.beamstep_px-c.height*c.pixel_size/2,c.height, dtype='float64')

    X,Y = np.meshgrid(x,y)

#setup for perfect shape, does a little math for convenience
    pm = (c.antenna_height-c.gap_height)/(2*c.antenna_width)
    pb = c.gap_height/2
    px_local_p = x-(c.gap_width/2)
    px_local_n = x+(c.gap_width/2)

#setup for pattern shape, does a little math for convenience
    m = (g.antenna_height-g.gap_height)/(2*g.antenna_width)
    b = g.gap_height/2
    x_local_p = x-(g.gap_width/2)
    x_local_n = x+(g.gap_width/2)
    ri_u_p = np.sqrt(((X-g.ci[0])**2)+((Y-g.ci[1])**2))
    ri_l_p = np.sqrt(((X-g.ci[0])**2)+((Y+g.ci[1])**2))
    ri_u_n = np.sqrt(((X+g.ci[0])**2)+((Y-g.ci[1])**2))
    ri_l_n = np.sqrt(((X+g.ci[0])**2)+((Y+g.ci[1])**2))
    ro_u_p = np.sqrt(((X-g.co[0])**2)+((Y-g.co[1])**2))
    ro_l_p = np.sqrt(((X-g.co[0])**2)+((Y+g.co[1])**2))
    ro_u_n = np.sqrt(((X+g.co[0])**2)+((Y-g.co[1])**2))
    ro_l_n = np.sqrt(((X+g.co[0])**2)+((Y+g.co[1])**2))

#steps through map and assigns a value of 1 if the position is within bounds
#first loop creates the target shape, pulled from config file
#note that this does NOT use beamstep
    for i in range(0, c.height, 1):
        for j in range(0, c.width, 1):
            if (y[i]<(pm*px_local_p[j]+pb)) and (y[i]>(-pm*px_local_p[j]-pb)) and (px_local_p[j]>0) and (px_local_p[j]<c.antenna_width):
                g.perfect_map[i][j] = 1    
            if (y[i]<(-pm*px_local_n[j]+pb)) and (y[i]>(pm*px_local_n[j]-pb)) and (px_local_n[j]<0) and (px_local_n[j]>-c.antenna_width):
                g.perfect_map[i][j] = 1

#second loop creates the modified exposure shape
#note that this DOES use beamstep
    for i in range(0, c.height, c.beamstep_px):
        for j in range(0, c.width, c.beamstep_px):

#main trapezoid
            if (y[i]<(m*x_local_p[j]+b)) and (y[i]>(-m*x_local_p[j]-b)) and (x_local_p[j]>0) and (x_local_p[j]<g.antenna_width):
                g.pattern_map[i][j] = g.d0    
            if (y[i]<(-m*x_local_n[j]+b)) and (y[i]>(m*x_local_n[j]-b)) and (x_local_n[j]<0) and (x_local_n[j]>-g.antenna_width):
                g.pattern_map[i][j] = g.d0

#top and bottom borders
            if (y[i]<(m*x_local_p[j]+b)) and (y[i]>(m*x_local_p[j]+b-g.d1_w)) and (x_local_p[j]>0) and (x_local_p[j]<g.antenna_width):
                g.pattern_map[i][j] = g.d1    
            if (y[i]<(-m*x_local_n[j]+b)) and (y[i]>(-m*x_local_n[j]+b-g.d1_w)) and (x_local_n[j]<0) and (x_local_n[j]>-g.antenna_width):
                g.pattern_map[i][j] = g.d1
            if (y[i]<(-m*x_local_p[j]-b+g.d1_w)) and (y[i]>(-m*x_local_p[j]-b)) and (x_local_p[j]>0) and (x_local_p[j]<g.antenna_width):
                g.pattern_map[i][j] = g.d1    
            if (y[i]<(m*x_local_n[j]-b+g.d1_w)) and (y[i]>(m*x_local_n[j]-b)) and (x_local_n[j]<0) and (x_local_n[j]>-g.antenna_width):
                g.pattern_map[i][j] = g.d1

#outside border    
            if (y[i]<(m*x_local_p[j]+b)) and (y[i]>(-m*x_local_p[j]-b)) and (x_local_p[j]>(g.antenna_width-g.d2_w)) and (x_local_p[j]<g.antenna_width):
                g.pattern_map[i][j] = g.d2    
            if (y[i]<(-m*x_local_n[j]+b)) and (y[i]>(m*x_local_n[j]-b)) and (x_local_n[j]<(-g.antenna_width+g.d2_w)) and (x_local_n[j]>-g.antenna_width):
                g.pattern_map[i][j] = g.d2

#inside border    
            if (y[i]<(m*x_local_p[j]+b)) and (y[i]>(-m*x_local_p[j]-b)) and (x_local_p[j]>0) and (x_local_p[j]<g.d3_w):
                g.pattern_map[i][j] = g.d3    
            if (y[i]<(-m*x_local_n[j]+b)) and (y[i]>(m*x_local_n[j]-b)) and (x_local_n[j]<0) and (x_local_n[j]>-g.d3_w):
                g.pattern_map[i][j] = g.d3


#inner and outer circles            
            if (ri_u_p[i][j] <= g.ri) or (ri_l_p[i][j] <= g.ri) or (ri_u_n[i][j] <= g.ri) or (ri_l_n[i][j] <= g.ri):
                g.pattern_map[i][j] = g.di
            if (ro_u_p[i][j] <= g.ro) or (ro_l_p[i][j] <= g.ro) or (ro_u_n[i][j] <= g.ro) or (ro_l_n[i][j] <= g.ro):
                g.pattern_map[i][j] = g.do
    return

def split_exposure():

    threads = []
    exposure_shape=g.exposure_shape

    for i in range(c.nt):
        threads.append(threading.Thread(target=exposure, args=(exposure_shape,i,c.nt,)))

    for i in threads:
        i.start()

    for i in threads:
        i.join()
    return

def exposure(exposure_shape,t,nt):


#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,c.width*c.pixel_size,c.width, dtype='float32')
    y = np.linspace(0,c.height*c.pixel_size,c.height, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(t,c.height,nt):
        for j in range(c.width):
            if g.pattern_map[i][j] > 0:
#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                exposure_shape = exposure_shape+g.pattern_map[i][j]*(c.dose/(m.pi*(1+c.eta)))*((1/(c.alpha**2))*np.exp(-0.5*(r**2)/(c.alpha**2))+(c.eta/(c.beta**2))*np.exp(-0.5*(r**2)/(c.beta**2)))
    g.exposed_map = g.exposed_map + exposure_shape
    return

def plot_shapes():

    plt.figure(1)
    plt.imshow(g.pattern_map, cmap=plt.cm.gray, extent=[0,c.width,0,c.height])
    plt.xticks(range(0,c.width,c.tickspacing))
    plt.yticks(range(0,c.height,c.tickspacing))

    plt.figure(2)
    plt.imshow(g.exposed_map, cmap=plt.cm.gray, extent=[0,c.width,0,c.height])
    plt.xticks(range(0,c.width,c.tickspacing))
    plt.yticks(range(0,c.height,c.tickspacing))

    plt.figure(3)
    plt.imshow(g.developed_map, cmap=plt.cm.gray, extent=[0,c.width,0,c.height])
    plt.xticks(range(0,c.width,c.tickspacing))
    plt.yticks(range(0,c.height,c.tickspacing))
    
    plt.figure(4)
    plt.imshow(g.perfect_map, cmap=plt.cm.gray, extent=[0,c.width,0,c.height])
    plt.xticks(range(0,c.width,c.tickspacing))
    plt.yticks(range(0,c.height,c.tickspacing))

    plt.figure(5)
    plt.imshow(g.overlap_map, cmap=plt.cm.gray, extent=[0,c.width,0,c.height])
    plt.xticks(range(0,c.width,c.tickspacing))
    plt.yticks(range(0,c.height,c.tickspacing))

    plt.show()
