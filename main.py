import requests
from requests.auth import HTTPBasicAuth

# Twilio API credentials
account_sid = ''
auth_token = ''
from_number = '[Your Twilio Number]'

# SMS details
to_numbers = ['+233...', '+233...'] # use tTwilio verified numbers
message = 'testing || Hello World.'

# Twilio API endpoint
url = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json'.format(account_sid)

# Loop through recipient numbers and send SMS
for to_number in to_numbers:
    payload = {
        'To': to_number,
        'From': from_number,
        'Body': message
    }

    response = requests.post(url, auth=HTTPBasicAuth(account_sid, auth_token), data=payload)

    if response.status_code == 201:
        print(f'SMS sent to {to_number}')
    else:
        print(f'Failed to send SMS to {to_number}. Error: {response.text}')
