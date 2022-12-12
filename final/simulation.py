import numpy as np
import time

def simul(log):
    #DO simulation
    out = -1
    for i in range(2000):
        pr = "Current:"+ str(out)
        out = i
        log.value = pr
        time.sleep(1)
        print(pr)

