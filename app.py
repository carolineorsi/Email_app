import os
import msg
import requests
from flask import Flask, request, render_template, jsonify

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', "abcdefg")

app = Flask(__name__)


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

    if msg.send_message_mailgun(message) != requests.codes.ok:
        # toggle email provider

    else:
        return "success"


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5001))
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)