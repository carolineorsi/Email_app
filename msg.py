import requests
import os
import re
from BeautifulSoup import BeautifulSoup

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')

def process_msg(message):
    if check_content(message):
        message['body'] = remove_html(message['body'])


        pass

    else: 
        # something here to return error
        pass


def check_content(message):
    """ Checks that all fields of the message object contain text. """

    valid = True

    for key in message:
        if message[key] == '':
            valid = False
            return valid

    if not validate_email(message['to']) or not validate_email(message['from']):
        valid = False

    return valid


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
    """ Checks that email is valid. """

    if re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._-]+(\.[a-zA-Z]{2,3})+\b', email):
        return True
    else:
        return False


def remove_html(body):
    """ Removes HTML tags from body text. """

    return BeautifulSoup(body).text



remove_html("<h1>Your Bill</h1><p>$10</p>")