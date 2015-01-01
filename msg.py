import requests
import os
import re
from BeautifulSoup import BeautifulSoup

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
SENDGRID_API_USER = os.environ.get('SENDGRID_API_USER')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')



def check_valid_content(message):
    """ Checks that all fields of the message object contain text. """

    valid = True

    for key in message:
        if message[key] == '':
            valid = False
            return valid

    if not validate_email(message['to']) or not validate_email(message['from']):
        valid = False

    message['body'] = remove_html(message['body'])

    return valid


def validate_email(email):
    """ Checks that email is valid. """

    if re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._-]+(\.[a-zA-Z]{2,3})+\b', email):
        return True
    else:
        return False


def remove_html(body):
    """ Removes HTML tags from body text. """

    return BeautifulSoup(body).text


def send_message_mailgun():
    response = requests.post( #return this and handle error in parent function?
        "https://api.mailgun.net/v2/sandbox74f4b1d357014aaabd16ecc5f39e75b5.mailgun.org/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": "Caroline Yahoo <wiredoats@yahoo.com>",
              "to": "Caroline Orsi <caroline.orsi@gmail.com>",
              "subject": "Hello Caroline Orsi",
              "text": "Test of API Key"})


    print response.status_code
    print response.text

def send_message_sendgrid():
    message = {'api_user': SENDGRID_API_USER,
               'api_key': SENDGRID_API_KEY,
               'to': 'caroline.orsi@gmail.com',
               'toname': 'Caroline Orsi',
               'subject': 'Yo from sendgrid',
               'text': 'this is your test message',
               'from': 'juliabrown.sf@gmail.com'}

    response = requests.get( #return this and handle error in parent function?
        "https://api.sendgrid.com/api/mail.send.json",
        params=message)

    print vars(response)