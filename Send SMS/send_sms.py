from twilio.rest import Client

account_sid = 'your_acount_sid'
auth_token = 'your_auth_token'
sender_number = (
    'your_phone_number'  # This must be a Twilio phone number that you own, formatted with a '+' and country code
)


class TwilioClient:
    def __init__(self, account_sid, auth_token, sender_number):
        self.sender_number = sender_number
        self.client = Client(account_sid, auth_token)

    def send_messages(self, message, phone_number):
        self.client.messages.create(from_=self.sender_number, body=message, to=phone_number)


if __name__ == "__main__":
    client = TwilioClient(account_sid=account_sid, auth_token=auth_token, sender_number=sender_number)

    message = str(input("Enter SMS message: "))
    phone_number = input("Enter destination phone number for your SMS (with a '+' and a country code): ")
    client.send_messages(message=message, phone_number=phone_number)
