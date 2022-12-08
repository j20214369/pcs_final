from twilio.rest import Client
import keys

################UE Send message to control(target_nember)
client = Client(keys.account_sid, keys.auth_token)
message = client.messages.create(
    body="Start",
    #body="Stop",
    #body="Set parameter to 8",
    from_=keys.twilio_number_UE,
    to=keys.target_number,
)
print(message.body)
################End of UE Send message to control(target_nember)

