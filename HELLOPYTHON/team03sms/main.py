import os
from twilio import rest
#cmd 창에서 twilio를 install 해줍니다!

account_sid = 'ACb5f9dacf9e30077d8b91db20742967d0'
auth_token = 'd7410be1db377c9a1fd0920b17641961'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+821084459916", 
    from_="+13172254351",
    body="에이")

print(message.sid)
