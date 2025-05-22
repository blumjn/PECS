import threading
from exposure_t_file import *

def split_exposure(pattern,exposure_shape,width,height,*raith):

    threads = []
    nt = 8


    for i in range(nt):
        threads.append(threading.Thread(target=exposure_t, args=(pattern,exposure_shape,width,height,*raith,i,nt)))

    for i in threads:
        i.start()

    for i in threads:
        i.join()