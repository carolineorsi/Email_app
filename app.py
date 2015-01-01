import os
import msg
import requests
from flask import Flask, request, render_template, jsonify, make_response
from msg import check_valid_content, send_message_mailgun, send_message_sendgrid

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', "abcdefg")
email_provider = send_message_mailgun

app = Flask(__name__)


@app.route("/")
def index():
    """ This is the 'cover' page of the site """

    return render_template("index.html")


@app.route("/email", methods=["POST"])
def email():
    """ Placeholder. """
    message = request.get_json()
    if not check_valid_content(message):
        return make_response(jsonify({'message': 'Invalid input parameters.'}), 400)

    if email_provider(message).status_code != requests.codes.ok:
        toggle_email_provider()
        if email_provider(message).status_code != requests.codes.ok:
            return make_response(jsonify({'message': 'Error encountered with email provider.'}), 500)

    return make_response(jsonify({'message': 'Message sent.'}), 200)


def toggle_email_provider():
    global email_provider
    if email_provider == send_message_mailgun:
        email_provider = send_message_sendgrid
    else:
        email_provider = send_message_mailgun


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5001))
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)