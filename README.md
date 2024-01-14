Bulk SMS Sender

Overview:

This Python script allows you to send bulk SMS messages using the Twilio API. You can customize the recipients and the message to be sent.
Prerequisites

Before using this script, make sure you have the following:

    Python installed on your machine.
    A Twilio account. If you don't have one, you can sign up here.
    Twilio API credentials:
        Account SID
        Auth Token
        Twilio phone number

Installation:

    Clone this repository to your local machine.

    bash:

git clone https://github.com/NanaBright/bulk_sms_I.git

cd bulk_sms_I


Install the required Python libraries.


bash:

    pip install requests


Configuration:

Open the bulk_sms_sender.py file in a text editor and replace the following placeholders with your Twilio credentials:

python

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
from_number = 'your_twilio_phone_number'

Usage:

    Edit the to_numbers list in the script to include the phone numbers of the recipients.

python

to_numbers = ['recipient_number_1', 'recipient_number_2']

    Modify the message variable to set the content of your bulk SMS message.

python

message = 'Your bulk SMS message goes here.'

    Save the changes.

    Run the script.

    bash

    python bulk_sms_sender.py

The script will iterate through the recipient numbers and send the specified message to each.
Notes

    Keep your Twilio API credentials secure. Avoid hardcoding them directly into your script for production use.
    Be mindful of any rate limits imposed by Twilio to prevent issues.