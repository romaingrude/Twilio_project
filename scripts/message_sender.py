import os
from twilio.rest import Client
import datetime

class TextMessager():

    def __init__(self, customer):
        #Takes instance of customer
        self.customer = customer
        self.current_time = datetime.datetime.now()
        self.new_time = self.current_time + datetime.timedelta(minutes=30)

    def send_message(self):

        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=f"+44{self.customer.get_number()[1:]}",
            from_="+447380314231",
            body=f"Hi {self.customer.get_name()}! Your order was placed and will be delivered at {self.new_time.strftime('%H:%M')}"
        )

        with open('SMS_Log.txt', 'a') as f:
            f.write('SID: ' + str(message.sid))
            f.write('\n')
            f.write('Date created: ' + str(message.date_created))
            f.write('\n')
            f.write('Content: ' + str(message.body))
            f.write('\n' * 3)

