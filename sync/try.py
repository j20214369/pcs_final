import mimetypes
from flask import Flask, request, redirect, Response
from twilio.twiml.messaging_response import MessagingResponse
import numpy as np
import time
from multiprocessing import Process, Manager
from ctypes import c_char_p


def sim(start,log):
    while True:
        if start.value:
            #DO simulation
            out = -1
            for i in range(20):
                pr = "Current:"+ str(out)
                out = i
                log.value = pr
                time.sleep(1)
                print(pr)


################UE Receive message which is send by control(target_nember)
app = Flask(__name__)

@app.route("/sms", methods = ['GET','POST'])
def sms_reply():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    print(body)
    global simulation

    if body == 'Sim':
        start.value = True
        
        resp.message("The program start!")
    elif body == 'Pause':
        start.value = False
        simulation.terminate()
        simulation = Process(target=sim, args=(start,log,) )
        simulation.start()

        resp.message("The program stop!")
    elif body == 'Print':
        resp.message(log.value)
    else:
        resp.message("Parameter has been set!")
    return Response(str(resp), mimetype="application/xml")
    


if __name__ == "__main__":
    global first
    first = True
    manager = Manager()
    global start
    start = manager.Value('flag',True)
    manager2 = Manager()
    global log
    log = manager2.Value(c_char_p,'test')
    global simulation
    global temp
    simulation = Process(target=sim, args=(start,log,) )
    print('start')
    simulation.start()
    
    app.run()
    
    

################End of UE Receive message which is send by control(target_nember)
