def area_setup():
    import numpy as np
    import global_variables as g
    import config as c
#This function sets up the empty arrays for both the pattern and the resulting exposure
#x,y in terms of pixels, not nm
#pattern is most likely a lower resolution than the exposure and is based on the Raith stepsize
    pattern_row, pattern_col = (round(g.width/c.pixel_size), round(g.height/c.pixel_size))
#creates the 2D arrays
    g.pattern_shape = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    g.exposure_shape = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    g.exposed_map = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    g.pattern_map = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    g.perfect_map = np.array([[0 for j in range(pattern_row)] for i in range(pattern_col)], dtype=float)
    return

def FoM():
    import config as c
    import global_variables as g
    import numpy as np
    import matplotlib.pyplot as plt

    g.overlap_map = np.logical_xor(g.developed_map,g.perfect_map)
    # plt.figure(1)
    # plt.imshow(g.perfect_map, cmap=plt.cm.gray, extent = [-g.width/2,g.width/2,-g.height/2,g.height/2])
    # plt.figure(2)
    # plt.imshow(g.developed_map, cmap=plt.cm.gray, extent = [-g.width/2,g.width/2,-g.height/2,g.height/2])
    # plt.figure(3)
    # plt.imshow(g.overlap_map, cmap=plt.cm.gray, extent = [-g.width/2,g.width/2,-g.height/2,g.height/2])
    # plt.show()
    return np.count_nonzero(g.overlap_map)

def FoM_lines():
    import config as c
    import global_variables as g

#Takes a crosscut of the map 2 pixels below the top edge of the gap  
    crosscut = g.developed_map[int((g.height/2)+(c.gap_height/(2*c.pixel_size))-2),:]

#turnpoints stores the indices where the step changes
    turnpoints = []
    for i in range(2,g.width,1):
#checks if the step has changed, stores the index if yes
        if (crosscut[i]^crosscut[i-1])==1:
                turnpoints.append(i)
 
#the first line width is the right hand pixel - the left hand pixel times the pixel size
#the gap is the left hand pixel of the second line minus the right hand pixel of the first times the pixel size
        if len(turnpoints) == 6:
            w1 = (turnpoints[5]-turnpoints[0])*c.pixel_size
            gap = (turnpoints[2]-turnpoints[1])*c.pixel_size
            w3 = (turnpoints[3]-turnpoints[2])*c.pixel_size
            #print("4 turnpoints, lw =", lw, ", gap = ", gap)
    
#If the number of exposed pixels is too great, assume that the lines take up the whole space and the gap is 0        
        elif len(turnpoints) == 2:
            w1 = (turnpoints[1]-turnpoints[0])*c.pixel_size/2
            w3 = w1
            gap = 0
            #print("2 turnpoints, lw =", lw, ", gap = ", gap)
#If all else fails, assume that the lines did not develop at all
        else:
            w1 = 0
            w3 =0
            gap = g.width*c.pixel_size
            #print("0 turnpoints, lw =", lw, ", gap = ", gap)  
    return w1, gap, w3

def FoM_antennas():
    import config as c
    import global_variables as g

#Take horizontal crosscuts at the vertical center, 1 pixel below the top edge of the gap, and halfway between the top edge of the gap and the top of the antenna 
    h_crosscut_1 = g.developed_map[int(g.height/2),:]
    h_crosscut_2 = g.developed_map[int((g.height/2)+(c.gap_height/(2*c.pixel_size)))-1,:]
    h_crosscut_3 = g.developed_map[int((g.height/2)+((c.gap_height-c.antenna_height))/(2*c.pixel_size)),:]

#Take vertical crosscuts at the inside edge, horizontal center of the antenna, and outside edge
    v_crosscut_1 = g.developed_map[:,int((g.width/2)+c.gap_width/(2*c.pixel_size))]
    v_crosscut_2 = g.developed_map[:,int((g.width/2)+c.gap_width/(2*c.pixel_size)+c.antenna_width/(2*c.pixel_size))]
    v_crosscut_3 = g.developed_map[:,int((g.width/2)+c.gap_width/(2*c.pixel_size)+c.antenna_width/(c.pixel_size))]

#If there are at least 4 exposed pixels, then there are two developed lines of non-unity width
#If the exposed pixels take up the whole space, then there is no gap 

#turnpoints stores the indices where the step changes
    turnpoints_h1 = []
    turnpoints_h2 = []
    turnpoints_h3 = []
    turnpoints_v1 = []
    turnpoints_v2 = []
    turnpoints_v3 = []
    for i in range(2,g.width,1):
#checks if the step has changed, stores the index if yes
        if (h_crosscut_1[i]^h_crosscut_1[i-1])==1:
                turnpoints_h1.append(i)
        if (h_crosscut_2[i]^h_crosscut_2[i-1])==1:
                turnpoints_h2.append(i)
        if (h_crosscut_3[i]^h_crosscut_3[i-1])==1:
                turnpoints_h3.append(i)
    for i in range(2,g.height,1):
#checks if the step has changed, stores the index if yes
        if (v_crosscut_1[i]^v_crosscut_1[i-1])==1:
                turnpoints_v1.append(i)
        if (v_crosscut_2[i]^v_crosscut_2[i-1])==1:
                turnpoints_v2.append(i)
        if (v_crosscut_3[i]^v_crosscut_3[i-1])==1:
                turnpoints_v3.append(i)
 
#the first line width is the right hand pixel - the left hand pixel times the pixel size
#the gap is the left hand pixel of the second line minus the right hand pixel of the first times the pixel size
    if len(turnpoints_h1) == 4:
        width1 = (turnpoints_h1[1]-turnpoints_h1[0])*c.pixel_size
        gap1 = (turnpoints_h1[2]-turnpoints_h1[1])*c.pixel_size
        #print("4 turnpoints, lw =", lw, ", gap = ", gap)

#If the number of exposed pixels is too great, assume that the lines take up the whole space and the gap is 0        
    elif len(turnpoints_h1) == 2:
        width1 = (turnpoints_h1[1]-turnpoints_h1[0])*c.pixel_size/2
        gap1 = 0
        #print("2 turnpoints, lw =", lw, ", gap = ", gap)
#If all else fails, assume that the lines did not develop at all
    else:
        width1 = 0
        gap1 = g.width*c.pixel_size

    if len(turnpoints_h2) == 4:
        width2 = (turnpoints_h2[1]-turnpoints_h2[0])*c.pixel_size
        gap2 = (turnpoints_h2[2]-turnpoints_h2[1])*c.pixel_size
    elif len(turnpoints_h2) == 2:
        width2 = (turnpoints_h2[1]-turnpoints_h2[0])*c.pixel_size/2
        gap2 = 0
    else:
        width2 = 0
        gap2 = g.width*c.pixel_size

    if len(turnpoints_h3) == 4:
        width3 = (turnpoints_h3[1]-turnpoints_h3[0])*c.pixel_size
        gap3 = (turnpoints_h3[2]-turnpoints_h3[1])*c.pixel_size
    elif len(turnpoints_h3) == 2:
        width3 = (turnpoints_h3[1]-turnpoints_h3[0])*c.pixel_size/2
        gap3 = 0
    else:
        width3 = 0
        gap3 = g.width*c.pixel_size

    if len(turnpoints_v1) == 2:
        height1 = (turnpoints_v1[1]-turnpoints_v1[0])*c.pixel_size
    else:
        height1 = 0
    if len(turnpoints_v2) == 2:
        height2 = (turnpoints_v2[1]-turnpoints_v2[0])*c.pixel_size
    else:
        height2 = 0
    if len(turnpoints_v3) == 2:
        height3 = (turnpoints_v3[1]-turnpoints_v3[0])*c.pixel_size
    else:
        height3 = 0

    return gap1, width1, gap2, width2, gap3, width3, height1, height2, height3

def pattern_creation():
    import numpy as np
    import global_variables as g
    import config as c
    import matplotlib.pyplot as plt

#creates arrays with values for x and y in terms of nm with 0 at center (offset by 1)
    x = np.arange(-0.5*g.width,0,c.pixel_size, dtype='float64')
    y = np.arange(0.5*g.height,0,-c.pixel_size, dtype='float64')
    X,Y = np.meshgrid(x,y)

#steps through map and assigns a value of 1 if the position is within bounds
    for i in range(0, len(y), int(c.beamstep_nm/c.pixel_size)):
        for j in range(0, len(x), int(c.beamstep_nm/c.pixel_size)):
            if ((abs(x[j])<=g.outer_square/2) and (abs(y[i])<=g.outer_square/2)):
                g.pattern_map[i][j] = 1
            if ((abs(x[j])<=g.donut_square/2) and (abs(y[i])<=g.donut_square/2)):
                g.pattern_map[i][j] = 0
            if ((abs(x[j])<=g.inner_square/2) and (abs(y[i])<=g.inner_square/2)):
                g.pattern_map[i][j] = 1

    g.pattern_map=g.pattern_map+np.fliplr(g.pattern_map)+np.flipud(g.pattern_map)+np.fliplr(np.flipud(g.pattern_map))

    for i in range(0, len(y), 1):
        for j in range(0, len(x), 1):
            if ((abs(x[j])<=g.w1) and (abs(y[i])<=g.w1)) and not\
               (((abs(x[j])-g.w1+g.r1)**2+(abs(y[i])-g.w1+g.r1)**2>g.r1**2) and (abs(x[j])>g.w1-g.r1) and (abs(y[i])>g.w1-g.r1)):
                g.perfect_map[i][j] = 1
            if ((abs(x[j])<=g.w2) and (abs(y[i])<=g.w2)) and not\
               (((abs(x[j])-g.w2+g.r2)**2+(abs(y[i])-g.w2+g.r2)**2>g.r2**2) and (abs(x[j])>g.w2-g.r2) and (abs(y[i])>g.w2-g.r2)):
                g.perfect_map[i][j] = 0
            if ((abs(x[j])<=g.w3) and (abs(y[i])<=g.w3)) and not\
               (((abs(x[j])-g.w3+g.r3)**2+(abs(y[i])-g.w3+g.r3)**2>g.r3**2) and (abs(x[j])>g.w3-g.r3) and (abs(y[i])>g.w3-g.r3)):
                g.perfect_map[i][j] = 1
    g.perfect_map= g.perfect_map+np.fliplr( g.perfect_map)+np.flipud( g.perfect_map)+np.fliplr(np.flipud( g.perfect_map))
    return

def pattern_creation_antenna_corners():
    import numpy as np
    import global_variables as g
    import config as c
    import math as m
    import matplotlib.pyplot as plt

#creates arrays with values for x and y in terms of nm with 0 at center (offset by 1)
    x = np.arange(-0.5*g.width,0,c.pixel_size, dtype='float64')
    y = np.arange(0.5*g.height,0,-c.pixel_size, dtype='float64')
    X,Y = np.meshgrid(x,y)
    if g.x1 != g.x2:
        m1 = (g.y2-g.y1)/(g.x2-g.x1)
    else:
        m1=99999
    m2 = (g.y3-g.y2)/(g.x3-g.x2)
    m3 = (g.y4-g.y3)/(g.x4-g.x3)
    if g.x4 != g.x5:
        m4 = (g.y5-g.y4)/(g.x5-g.x4)
    else:
        m4=99999
    b1=g.y1-m1*g.x1
    b2=g.y2-m2*g.x2
    b3=g.y3-m3*g.x3
    b4=g.y4-m4*g.x4

#steps through map and assigns a value of 1 if the position is within bounds
    for i in range(0, len(y), int(c.beamstep_nm/c.pixel_size)):
        for j in range(0, len(x), int(c.beamstep_nm/c.pixel_size)):
            if ((abs(x[j])>=(y[i]-b1)/m1) and (abs(x[j])<=(y[i]-b4)/m4) and ((abs(y[i])<=m2*abs(x[j])+b2) or (abs(y[i])<=m3*abs(x[j])+b3))):
                g.pattern_map[i][j] = g.d0

    g.pattern_map=g.pattern_map+np.fliplr(g.pattern_map)+np.flipud(g.pattern_map)+np.fliplr(np.flipud(g.pattern_map))

    for i in range(0, len(y), 1):
        for j in range(0, len(x), 1):
            if ((abs(x[j])<=c.antenna_width) and (abs(y[i])<=m.tan(m.radians(c.antenna_angle/2))*abs(x[j]))):
                g.perfect_map[i][j] = 1
            if ((abs(x[j])<=c.gap_width/2)):
                g.perfect_map[i][j] = 0
    g.perfect_map= g.perfect_map+np.fliplr( g.perfect_map)+np.flipud( g.perfect_map)+np.fliplr(np.flipud( g.perfect_map))

    return

def pattern_creation_antenna_combined():
    import numpy as np
    import global_variables as g
    import config as c
    import math as m
    import matplotlib.pyplot as plt

#creates arrays with values for x and y in terms of nm with 0 at center (offset by 1)
    x = np.arange(-0.5*g.width,0,c.pixel_size, dtype='float64')
    y = np.arange(0.5*g.height,0,-c.pixel_size, dtype='float64')
    X,Y = np.meshgrid(x,y)
    if g.x1 != g.x2:
        m1 = (g.y2-g.y1)/(g.x2-g.x1)
    else:
        m1=99999
    m2 = (g.y3-g.y2)/(g.x3-g.x2)
    m3 = (g.y4-g.y3)/(g.x4-g.x3)
    if g.x4 != g.x5:
        m4 = (g.y5-g.y4)/(g.x5-g.x4)
    else:
        m4=99999
    b1=g.y1-m1*g.x1
    b2=g.y2-m2*g.x2
    b3=g.y3-m3*g.x3
    b4=g.y4-m4*g.x4

#steps through map and assigns a value of 1 if the position is within bounds
    for i in range(0, len(y), int(c.beamstep_nm/c.pixel_size)):
        for j in range(0, len(x), int(c.beamstep_nm/c.pixel_size)):
            if ((abs(x[j])>=(y[i]-b1)/m1) and (abs(x[j])<=(y[i]-b4)/m4) and ((abs(y[i])<=m2*abs(x[j])+b2) or (abs(y[i])<=m3*abs(x[j])+b3))):
                g.pattern_map[i][j] = g.d0
            if m.sqrt(((abs(x[j])-g.x2)**2)+((abs(y[i])-g.y2)**2))<=g.r1:
                g.pattern_map[i][j] = g.d1
            if m.sqrt(((abs(x[j])-g.x4)**2)+((abs(y[i])-g.y4)**2))<=g.r2:
                g.pattern_map[i][j] = g.d2

    g.pattern_map=g.pattern_map+np.fliplr(g.pattern_map)+np.flipud(g.pattern_map)+np.fliplr(np.flipud(g.pattern_map))

    for i in range(0, len(y), 1):
        for j in range(0, len(x), 1):
            if ((abs(x[j])<=c.antenna_width) and (abs(y[i])<=m.tan(m.radians(c.antenna_angle/2))*abs(x[j]))):
                g.perfect_map[i][j] = 1
            if ((abs(x[j])<=c.gap_width/2)):
                g.perfect_map[i][j] = 0
    g.perfect_map= g.perfect_map+np.fliplr( g.perfect_map)+np.flipud( g.perfect_map)+np.fliplr(np.flipud( g.perfect_map))

    return

def pattern_creation_antenna_circles():
    import numpy as np
    import global_variables as g
    import config as c
    import math as m
    import matplotlib.pyplot as plt

#creates arrays with values for x and y in terms of nm with 0 at center (offset by 1)
    x = np.arange(-0.5*g.width,0,c.pixel_size, dtype='float64')
    y = np.arange(0.5*g.height,0,-c.pixel_size, dtype='float64')
    X,Y = np.meshgrid(x,y)

#steps through map and assigns a value of 1 if the position is within bounds
    for i in range(0, len(y), int(c.beamstep_nm/c.pixel_size)):
        for j in range(0, len(x), int(c.beamstep_nm/c.pixel_size)):
            if ((abs(x[j])<=g.antenna_width) and (abs(y[i])<=m.tan(m.radians(g.antenna_angle/2))*abs(x[j]))):
                g.pattern_map[i][j] = g.d0
            if ((abs(x[j])<=g.gap_width/2)):
                g.pattern_map[i][j] = 0
            if m.sqrt(((abs(x[j])-g.x1)**2)+((abs(y[i])-g.y1)**2))<=g.r1:
                g.pattern_map[i][j] = g.d1
            if m.sqrt(((abs(x[j])-g.x2)**2)+((abs(y[i])-g.y2)**2))<=g.r2:
                g.pattern_map[i][j] = g.d2
    g.pattern_map=g.pattern_map+np.fliplr(g.pattern_map)+np.flipud(g.pattern_map)+np.fliplr(np.flipud(g.pattern_map))

    for i in range(0, len(y), 1):
        for j in range(0, len(x), 1):
            if ((abs(x[j])<=c.antenna_width) and (abs(y[i])<=m.tan(m.radians(c.antenna_angle/2))*abs(x[j]))):
                g.perfect_map[i][j] = 1
            if ((abs(x[j])<=c.gap_width/2)):
                g.perfect_map[i][j] = 0
    g.perfect_map= g.perfect_map+np.fliplr( g.perfect_map)+np.flipud( g.perfect_map)+np.fliplr(np.flipud( g.perfect_map))
    return

def split_exposure():
    import threading
    import global_variables as g
    import config as c

    threads = []
    exposure_shape=g.exposure_shape
    
    while (g.height/2)%c.nt != 0:
        print(g.height/2,c.nt)
        c.nt = c.nt-1
        print(c.nt)

    for i in range(c.nt):
        threads.append(threading.Thread(target=exposure, args=(exposure_shape,i,c.nt,)))

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    return

def exposure(exposure_shape,t,nt):
    import numpy as np
    import math as m
    import global_variables as g
    import config as c

#creates arrays with values for x and y in terms of nm
    x = np.linspace(0,g.width*c.pixel_size,g.width, dtype='float32')
    y = np.linspace(0,g.height*c.pixel_size,g.height, dtype='float32')

#creates  2D versions of x and y

    X,Y = np.meshgrid(x,y)

#steps through the pattern and checks if it should expose the area
    for i in range(int(t*(g.height/(2*nt))),int((t+1)*(g.height/(2*nt))),1):
        for j in range(int(g.width/2)):
            q = 0
            r = int(round(g.charge_rad))
            if g.pattern_map[i][j] > 0:
                for l in range(-r,r+1):
                    for n in range(-r,r+1):
                        if g.pattern_map[i-l][j-n] > 0 and m.sqrt(((x[j]-x[j-n])**2)+((y[i]-y[i-l])**2))<=r :
                            q = q + g.pattern_map[i-l][j-n]
                q = q/(m.pi*r*r)

#if an exposed pixel is found, calculate distance to all other pixels, then add exposure
                r = np.sqrt(((X-x[j])**2)+((Y-y[i])**2))
                v = g.v*q
                exposure_shape = exposure_shape+g.pattern_map[i][j]*(g.dose/(m.pi*(1+g.eta+v)))*((1/(g.alpha**2))*np.exp(-0.5*(r**2)/(g.alpha**2))+\
                                                                                                   (g.eta/(g.beta**2))*np.exp(-0.5*(r**2)/(g.beta**2))+\
                                                                                                    (v/(2*g.gamma**2))*np.exp(-r/(g.gamma)))

    exposure_shape = exposure_shape + np.flipud(exposure_shape)
    exposure_shape = exposure_shape + np.fliplr(exposure_shape)
    g.exposed_map = g.exposed_map + exposure_shape
    return
def side_etch():
    import global_variables as g
    import numpy as np
    g.etch = int(round(g.etch))
    etch_mask = g.developed_map*0
    for i in range(g.etch, g.height-g.etch, 1):
        for j in range(g.etch, g.width-g.etch, 1):
            if etch_mask[i][j] == 0 and g.developed_map[i][j] == 0:

                for n in range(-g.etch,g.etch+1, 1):
                    if etch_mask[i][j] == 0:

                        for m in range(-g.etch,g.etch+1,1):
                            if (g.developed_map[i-n][j-m] == 1) and ((n**2)+(m**2)<=g.etch**2):
                                etch_mask[i][j] =1
                                break

    g.developed_map = np.logical_or(g.developed_map,etch_mask)

    return

def plot_shapes(iter):
    import matplotlib.pyplot as plt
    import numpy as np
    import config as c
    import global_variables as g
    import os

    fn_iter = '0'*(5-len(str(iter)))+str(iter)

    plt.figure(1)
    plt.imshow(g.pattern_map, cmap=plt.cm.gray, extent = [-g.width/2,g.width/2,-g.height/2,g.height/2])

    # plt.clim(0,2)
    plt.title("Pattern, Iteration = "+str(iter))
    plt.savefig(os.path.join(c.folder, fn_iter+"_pattern.png"))

    plt.figure(2)
    plt.imshow(g.exposed_map, cmap=plt.cm.gray, extent = [-g.width/2,g.width/2,-g.height/2,g.height/2])

    plt.title("Exposure, Iteration = "+str(iter))
    plt.savefig(os.path.join(c.folder, fn_iter+"_exposure.png")) 

    plt.figure(3)
    plt.imshow(g.developed_map, cmap=plt.cm.gray, extent = [-g.width/2,g.width/2,-g.height/2,g.height/2])

    plt.title("Development, Iteration = "+str(iter))
    plt.savefig(os.path.join(c.folder, fn_iter+"_development.png"))
    
    plt.figure(4)
    plt.imshow(g.perfect_map, cmap=plt.cm.gray, extent = [-g.width/2,g.width/2,-g.height/2,g.height/2])
    plt.title("Perfect Shape, Iteration = "+str(iter))
    plt.savefig(os.path.join(c.folder, fn_iter+"_perfect.png"))

    plt.figure(5)
    plt.imshow(g.overlap_map, cmap=plt.cm.gray, extent = [-g.width/2,g.width/2,-g.height/2,g.height/2])

    plt.title("Overlap, Iteration = "+str(iter))
    plt.savefig(os.path.join(c.folder, fn_iter+"_overlap.png"))

#    plt.show()
def combine_images():
    import cv2
    import os
    import config as c
    
    image_names = os.listdir(c.folder)
    image_names.sort()
    num_images = len(image_names)-2
 
    for i in range(0,num_images,4):
        img1 = cv2.imread(os.path.join(c.folder,image_names[i]))
        img2 = cv2.imread(os.path.join(c.folder,image_names[i+1]))
        img3 = cv2.imread(os.path.join(c.folder,image_names[i+2]))
        img4 = cv2.imread(os.path.join(c.folder,image_names[i+3]))
        img_tile = cv2.vconcat([cv2.hconcat([img4, img2]),cv2.hconcat([img1, img3])])
        img_name = str("combined"+image_names[i][:5]+".jpg")
        cv2.imwrite(os.path.join(c.folder,img_name),img_tile)
        