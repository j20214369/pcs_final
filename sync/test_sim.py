import numpy as np
import time
from multiprocessing import Process, Manager
from ctypes import c_char_p

def simul(log):
    #DO simulation
    out = -1
    for i in range(20):
        pr = "Current:"+ str(out)
        out = i
        log.value = pr
        time.sleep(1)
        print(pr)

