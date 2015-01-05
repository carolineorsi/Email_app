import requests
import os
import re
from BeautifulSoup import BeautifulSoup

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
SENDGRID_API_USER = os.environ.get('SENDGRID_API_USER')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')


def check_valid_content(message):
    """ Checks that the message object contains valid input. """

    valid = True

    # Verifies that every required field is in message object.
    required_fields = ['to', 'to_name', 'from', 'from_name', 'subject', 'body']
    for field in required_fields:
        if field not in message:
            valid = False
            return valid

    # Verifies that each field contains text.
    for key in message:
        if message[key] == '':
            valid = False
            return valid

    # Verifies that the 'to' and 'from' email addresses are valid.
    if not validate_email(message['to']) or not validate_email(message['from']):
        valid = False

    # Strips HTML tag from 'body' input.
    message['body'] = remove_html(message['body'])

    return valid


def validate_email(email):
    """ Uses regular expression to check that email is valid. """

    if re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._-]+(\.[a-zA-Z]{2,3})+\b',
                email):
        return True
    else:
        return False


def remove_html(body):
    """ Removes HTML tags from body text. """

    return BeautifulSoup(body).text


def send_message_mailgun(message):
    """ Sends email message using Mailgun email provider.

        Accepts dictionary object with following data:
        'to' : recipient email address
        'to_name' : recipient name
        'from' : sender email address
        'from_name' : sender name
        'subject' : email subject
        'body' : text of email

        Returns Mailgun response object. """

    return requests.post(
        'https://api.mailgun.net/v2/sandbox74f4b1d357014aaabd16ecc5f39e75b5.\
            mailgun.org/messages',
        auth=('api', MAILGUN_API_KEY),
        data={'from': (message['from_name'] + ' <' + message['from'] + '>'),
              'to': (message['to_name'] + ' <' + message['to'] + '>'),
              'subject': message['subject'],
              'text': message['body']}
        )


def send_message_sendgrid(message):
    """ Sends email message using SendGrid email provider.

        Accepts dictionary object with following data:
        'to' : recipient email address
        'to_name' : recipient name
        'from' : sender email address
        'from_name' : sender name
        'subject' : email subject
        'body' : text of email

        Returns SendGrid response object. """

    return requests.get(
        'https://api.sendgrid.com/api/mail.send.json',
        params={'api_user': SENDGRID_API_USER,
                'api_key': SENDGRID_API_KEY,
                'to': message['to'],
                'toname': message['to_name'],
                'subject': message['subject'],
                'text': message['body'],
                'from': message['from'],
                'fromname': message['from_name']}
        )
