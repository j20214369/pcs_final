import numpy as np
import time
from multiprocessing import Process, Manager
from ctypes import c_char_p
from test_sim import simul

def sim(start,log):
    while True:
        if start.value:
            simul(log)
            #DO simulation
            """
            out = -1
            for i in range(20):
                pr = "Current:"+ str(out)
                out = i
                log.value = pr
                time.sleep(1)
                print(pr)
            """
if __name__ == '__main__':
    manager = Manager()
    start = manager.Value('flag',False)
    manager2 = Manager()
    log = manager2.Value(c_char_p,'test')
    simulation = Process(target=sim, args=(start,log,) )
    simulation.start()
    while True:
        print(start.value)
        text = input('Command:')
        print("main_test:",log.value)
        if text == 'g':#go
            start.value = True
        elif text == 's':#stop
            start.value = False
            simulation.terminate()
            simulation = Process(target=sim, args=(start,log,) )
            simulation.start()
        elif text == 'p':#print
            print('main',log.value)
        elif text == 'e':#Exit
            simulation.terminate()
            break
        else:
            print("Err")
