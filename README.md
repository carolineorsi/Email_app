## Introduction

This app accepts JSON data to send email messages through one of two email service providers, Mailgun and SendGrid. If one email provider fails, the app toggles to the alternate provider.

## Installation

1. Clone this repo: ```git clone https://github.com/carolineorsi/Email_app.git```
2. Install required Python packages: ```pip install -r requirements.txt```
3. Run app: ```python app.py```
4. Open localhost:5000 in web browser to access web input form to send a test message.

## Discussion

I've written this app in Python using the Flask framework, and have included the following features and libraries:
- Messages are sent via POST requests to the Mailgun and SendGrid email service providers. I've written separate functions for the requests to each provider, and have included the ```email_provider``` variable to specify which function should be called to send the message. The app evaluates the status code of the response received from the first provider attempted; if the request was not successful, the ```toggle_email_provider``` function is called to change the value of the ```email_provider``` variable to the function for the alternate provider.
- Prior to sending the requests to the email provider, the input data are validated. The first steps in validation are to verify that all fields are present in the provided input and that none of the fields contain empty strings.
- The to and from email addresses are validated using a regular expression and the Python ```re``` module. I've written a regular expression that will match most email formats. I recognize that there are some unusual email formats that would not be matched by the regex I've used in this app, however I opted to keep it simple given the short timeframe of this coding challenge.
- Once all fields are found to be valid, all HTML tags are removed from the "body" field using the BeautifulSoup library. The ```remove_html``` function simply removes all HTML tags; however, given more time to work on this app, I would write a more sophisticated function that would preserve formatting by recognizing paragraph tags, line breaks, lists, etc. and replacing them with new line characters, bullets, and other formatting as appropriate.