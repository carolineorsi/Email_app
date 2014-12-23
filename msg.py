import requests
import os
import re

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')

def send_simple_message():
    request = requests.post(
        "https://api.mailgun.net/v2/sandbox74f4b1d357014aaabd16ecc5f39e75b5.mailgun.org/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": "Caroline Yahoo <caroline.orsi@yahoo.com",
              "to": "Caroline Orsi <caroline.orsi@gmail.com>",
              "subject": "Hello Caroline Orsi",
              "text": "Test of API Key"})

    print request.status_code
    print request.text


def validate_email(email):
    # Instead of making this one function, could do "if not re.match(...)" elsewhere
    if re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._-]+(\.[a-zA-Z]{2,3})+\b', email):
        return "Valid"
    else:
        return "invalid"
    pass

send_simple_message();