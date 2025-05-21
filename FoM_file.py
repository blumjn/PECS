def FoM(map,col,row,pixel):
#Takes a crosscut of the map at x=0 (actually offset by +-1)    
    crosscut = map[int(row/2),:]

#If there are at least 4 exposed pixels, then there are two developed lines of non-unity width
#If the exposed pixels take up the whole space, then there is no gap 
    if sum(crosscut)>3 and sum(crosscut)<(col-4):
#turnpoints stores the indices where the step changes
        turnpoints = []

        for i in range(1,col,1):
#checks if the step has changed, stores the index if yes
            if (crosscut[i]^crosscut[i-1])==1:
                turnpoints.append(i)
 
#the first line width is the right hand pixel - the left hand pixel times the pixel size
#the gap is the left hand pixel of the second line minus the right hand pixel of the first times the pixel size
        lw = (turnpoints[1]-turnpoints[0])*pixel
        gap = (turnpoints[2]-turnpoints[1])*pixel
#If the number of exposed pixels is too great, assume that the lines take up the whole space and the gap is 0        
    elif sum(crosscut)>=(col-4):
        lw = col*pixel
        gap = 0
#If all else fails, assume that the lines did not develop at all
    else:
        lw = 0
        gap = col*pixel  


    return lw, gap, crosscut