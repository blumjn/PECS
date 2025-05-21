def plots(tickspacing, xrange, yrange, pixel, pattern, exposed_map, developed_map, crosscut):
    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure(1)
    plt.imshow(pattern, extent=[0,xrange,0,yrange])
    plt.xticks(range(0,xrange,tickspacing))
    plt.yticks(range(0,yrange,tickspacing))

    plt.figure(2)
    plt.imshow(exposed_map,cmap=plt.cm.gray, extent=[0,xrange,0,yrange])
    plt.xticks(range(0,xrange,tickspacing))
    plt.yticks(range(0,yrange,tickspacing))

    plt.figure(3)
    plt.imshow(developed_map,cmap=plt.cm.gray, extent=[0,xrange,0,yrange])
    plt.clim(0,1)
    plt.xticks(range(0,xrange,tickspacing))
    plt.yticks(range(0,yrange,tickspacing))

    plt.figure(4)
    plt.plot(np.linspace(0,xrange,int(xrange/pixel)),crosscut)
    plt.xticks(range(0,xrange,tickspacing))

    plt.show()