import os
from twilio.rest import Client
import schedule
import random
import time

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

messages = ["Dirt has Nitrogen", "Bats are cute", "Hate is a virus", "Life is good",
"LOL I don't know what tf i am doing at this time"]

recipients = [os.environ['TEST_PHONE_NUMBER']]

def send_sms():
  for number in recipients:
    message = client.messages \
      .create(
        body=random.choice(messages),
        from_='+17324105140',
        to=number
      )
    print(message.sid)

#schedule.every().day.at("06:16").do(send_sms)
schedule.every(10).seconds.do(send_sms)
print("Schedule")

while True:
  schedule.run_pending()
  time.sleep(1)