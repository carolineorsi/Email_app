import requests
import os

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v2/sandbox74f4b1d357014aaabd16ecc5f39e75b5.mailgun.org/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": "Caroline Yahoo <caroline.orsi@yahoo.com",
              "to": "Caroline Orsi <caroline.orsi@gmail.com>",
              "subject": "Hello Caroline Orsi",
              "text": "Test of API Key"})

send_simple_message();