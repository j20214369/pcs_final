from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

################UE Receive message which is send by control(target_nember)
app = Flask(__name__)

@app.route("/sms", methods = ['GET','POST'])
def sms_reply():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    if body == 'Start':
        resp.message("The program start!")
    elif body == 'Stop':
        resp.message("The program stop!")
    else:
        resp.message("Parameter has been set!")
    return str(resp)

if __name__ == "__main__":
	app.run()

################End of UE Receive message which is send by control(target_nember)