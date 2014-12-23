import os
from flask import Flask, request, render_template

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', "abcdefg")

app = Flask(__name__)


@app.route("/")
def index():
    """ This is the 'cover' page of the site """

    return render_template("index.html")


@app.route("/email", methods=["POST"])
def email():
    """ Placeholder. """
    to_email = request.form.get("to")
    to_name = request.form.get("to_name")
    from_email = request.form.get("from")
    from_name = request.form.get("from_name")
    subject = request.form.get("subject")
    body = request.form.get("body")

    print to_email, to_name, from_email, from_name, subject, body


    return "success"


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)