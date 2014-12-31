import requests
import os
import re
from BeautifulSoup import BeautifulSoup

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')

def process_msg(msg):
    
    pass

def send_simple_message():
    request = requests.post(
        "https://api.mailgun.net/v2/sandbox74f4b1d357014aaabd16ecc5f39e75b5.mailgun.org/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": "Caroline Yahoo <juliabrown.sf@gmail.com>",
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


def remove_html(body):
    return BeautifulSoup(body).text



remove_html("<h1>Your Bill</h1><p>$10</p>")