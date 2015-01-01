import unittest
from app import *
from msg import *

class TestMsgFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_validate_email(self):
        self.assertTrue(validate_email("someone@gmail.com"))
        self.assertTrue(validate_email("someone@gmail.com.uk"))
        self.assertTrue(validate_email("firstname-lastname@gmail.com"))
        self.assertFalse(validate_email("someone@gmail"))
        self.assertFalse(validate_email("@gmail.com"))
        self.assertFalse(validate_email("someone@gmail@gmail.com"))

    def test_valid_content(self):
        self.assertFalse(check_valid_content({'to': '',
                                              'to_name': '',
                                              'from': '',
                                              'from_name': '',
                                              'subject': '',
                                              'body': ''}))
        self.assertFalse(check_valid_content({'to': ''}))

    def test_remove_html(self):
        self.assertEqual(remove_html("<h1>Header</h1>"), 
                                     "Header")
        self.assertEqual(remove_html("<h1>Header</h1><p>and some text</p>"),
                                     "Headerand some text")
        self.assertEqual(remove_html("<div><h1>Header within div</h1></div>"),
                                     "Header within div")

    def test_toggle_email_provider(self):



if __name__ == '__main__':
    unittest.main()