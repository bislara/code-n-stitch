from twilio.rest import Client
import phonenumbers

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
        try:
            self.client.messages.create(from_=self.sender_number, body=message, to=phone_number)
        except Exception as e:
            print('Failed to send message {}'.format(e))

    @staticmethod
    def is_valid_number(number):
        """
        Check whether it's a possible number (e.g. it has the right number of digits)
        or a valid number (e.g. it's in an assigned exchange)
        """
        if not isinstance(number, str):
            number = str(number)
        try:
            parsed = phonenumbers.parse(number)
            return phonenumbers.is_valid_number(parsed)
        except phonenumbers.phonenumberutil.NumberParseException:
            return False


if __name__ == "__main__":
    client = TwilioClient(account_sid=account_sid, auth_token=auth_token, sender_number=sender_number)

    message = str(input("Enter SMS message: "))
    phone_number = input("Enter destination phone number for your SMS (with a '+' and a country code): ")
    while not client.is_valid_number(phone_number):
        phone_number = input(
            "Invalid phone number\nPlease enter destination phone number for your SMS (with a '+' and a country code): "
        )

    client.send_messages(message=message, phone_number=phone_number)
