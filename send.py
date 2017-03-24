from twilio.rest import TwilioRestClient
from info import acc_no, a_token, cell, t_num


client = TwilioRestClient(acc_no, a_token)

my_msg = 'please say something'

message = client.messages.create(to=cell, from_=t_num,body=my_msg)

my_sid= message.sid
print my_sid

sms = client.sms.messages.get(my_sid)


print(sms.body)








