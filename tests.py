import unittest
from app import *
from msg import *
import mock


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


if __name__ == '__main__':
    unittest.main()
