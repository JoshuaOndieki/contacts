"""This is a TDD module.

Args:
    Arguments are hard coded.

Returns:
    Returns the status of tests run.

"""

import unittest
from models.contact import Contact


class TestCreateContact(unittest.TestCase):
    def test_creates_contact_instance(self):
        self.contact = Contact('Joshua', 'Ondieki', 254700009999)
        self.assertTrue('Joshua' == self.contact.firstname, msg="Should get first name")
        self.assertTrue('Ondieki' == self.contact.surname, msg="Should get last name")
        self.assertTrue(254700009999 == self.contact.number, msg="Phone number should be saved with accuracy")


if __name__ == '__main__':
    unittest.main()
