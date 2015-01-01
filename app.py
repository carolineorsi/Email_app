import os
import msg
import requests
from flask import Flask, request, render_template, jsonify

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', "abcdefg")

app = Flask(__name__)
email_provider = msg.send_message_mailgun


@app.route("/")
def index():
    """ This is the 'cover' page of the site """

    return render_template("index.html")


@app.route("/email", methods=["POST"])
def email():
    """ Placeholder. """
    message = request.get_json()
    if not msg.check_valid_content(message):
        return "failure" #whatever this should be

    if email_provider(message) != requests.codes.ok:
        toggle_email_provider()
        print email_provider(message)

    else:
        return "success"


def toggle_email_provider():
    global email_provider
    if email_provider == msg.send_message_mailgun:
        email_provider = msg.send_message_sendgrid
    else:
        email_provider = msg.send_message_mailgun


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5001))
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)