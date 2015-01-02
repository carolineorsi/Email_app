import unittest
import mock
import json
from app import *
from msg import *


class TestMsgFunctions(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email('someone@gmail.com'))
        self.assertTrue(validate_email('someone@gmail.com.uk'))
        self.assertTrue(validate_email('firstname-lastname@gmail.com'))
        self.assertFalse(validate_email('someone@gmail'))
        self.assertFalse(validate_email('@gmail.com'))
        self.assertFalse(validate_email('someone@gmail@gmail.com'))

    def test_valid_content(self):
        self.assertFalse(check_valid_content({'to': '',
                                              'to_name': '',
                                              'from': '',
                                              'from_name': '',
                                              'subject': '',
                                              'body': ''}))
        self.assertFalse(check_valid_content({'to': ''}))
        self.assertTrue(check_valid_content({'to': 'someone@email.com',
                                             'to_name': 'Someone',
                                             'from': 'someoneelse@gmail.com',
                                             'from_name': 'Someone Else',
                                             'subject': 'This is the subject.',
                                             'body': 'This is the body.'}))

    def test_remove_html(self):
        self.assertEqual(remove_html('<h1>Header</h1>'),
                         'Header')
        self.assertEqual(remove_html('<h1>Header</h1><p>and some text</p>'),
                         'Headerand some text')
        self.assertEqual(remove_html('<div><h1>Header within div</h1></div>'),
                         'Header within div')

    # @mock.patch('__main__.send_message_sendgrid', return_value=200)
    # @mock.patch('__main__.send_message_mailgun', return_value=200)
    # def test_send_message_sendgrid(self, sendgrid_function, mailgun_function):
    #     assert send_message_sendgrid("test") == 200

    # # @mock.patch('__main__.send_message_sendgrid', side_effect=mock_message_sendgrid)
    # # def test_send_message_sendgrid(self, send_message_sendgrid_function):
    # #     assert send_message_sendgrid("test")['status_code'] == 1234

class TestFlask(unittest.TestCase):

    # TODO: Fix this so that it doesn't send message.
    @mock.patch('send_message_sendgrid', return_value=500)
    @mock.patch('send_message_mailgun', return_value=500)
    def test_email(self, sendgrid_function, mailgun_function):
        app_test = app.test_client(self)
        data = json.dumps({'to': 'caroline.orsi@gmail.com',
                 'to_name': 'Recipient',
                 'from': 'juliabrown.sf@gmail.com',
                 'from_name': 'Sender',
                 'subject': 'This is the subject line',
                 'body': 'This is the message body'})
        response = app_test.post('/email', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data_missing = json.dumps({})
        response = app_test.post('/email', data=data_missing, content_type='application/json')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
