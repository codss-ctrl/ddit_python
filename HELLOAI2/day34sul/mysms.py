import os
from twilio import rest
from twilio.rest import Client
#cmd 창에서 twilio를 install 해줍니다!

class MySms:
    def mysendSms(self,mobile,content):
      
        account_sid = 'AC55de193f32e4b0085d4ca27a82259923'
        auth_token = 'e3f47132a9884cc6648f6e62b56fe386'
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
            to="+82"+mobile, 
            from_="+15037555383",
            body=content)
        
if __name__ == '__main__':
    MySms().mysendSms("01073310309", "http://127.0.0.1:5000")
    
    
    
    
    
    
    
    