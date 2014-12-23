import os
from flask import Flask
from flask import render_template

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', "abcdefg")

app = Flask(__name__)


@app.route("/")
def index():
    """ This is the 'cover' page of the site """

    return render_template("index.html")


@app.route("/email", methods=["POST"])
def email():
    """ Placeholder. """
    return "success"


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5001))
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)