"""This is a TDD module.

Args:
    Arguments are hard coded.

Returns:
    Returns the status of tests run.

"""

import unittest
from models.phonebook import Contacts


class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.instance = Contacts()

    def test_add_contact(self):
        self.instance.add('Joshua', 'Ondieki', 254700009999)
        self.instance.add('Andela', 'Kenya', 254788880000)
        self.instance.add('David', 'Kironde', 254790909090)
        self.assertEqual(len(self.instance.data), 3, msg="Should indicate 3 contacts present in phone book!")

    def test_does_not_allow_non_integers_as_number(self):
        # Check to ensure add, edit and delete rejects alphanumerics
        with self.assertRaises(ValueError, msg="A telephone number should not contain alphanumeric characters!"):
            self.instance.add('Awkward', 'Number', '65ece89QFS`;-2')
        with self.assertRaises(ValueError, msg="A telephone number should not contain alphanumeric characters!"):
            self.instance.edit('65ece89QFS`;-2', 'Awkward', 'Number')
        with self.assertRaises(ValueError, msg="A telephone number should not contain alphanumeric characters!"):
            self.instance.delete('65ece89QFS`;-2')

    def test_does_not_accept_different_data_types(self):
        with self.assertRaises(TypeError, msg="A telephone number cannot be other data types like dictionary!"):
            self.instance.edit({}, 'Awkward', 'Number')
        with self.assertRaises(TypeError, msg="A telephone number cannot be other data types like list!"):
            self.instance.add('Awkward', 'Number', [])
        with self.assertRaises(TypeError, msg="A telephone number cannot be other data types like tuple!"):
            self.instance.delete(())

    def test_cannot_add_duplicates(self):
        self.instance.add('tobe', 'duplicated', 254700000000)
        response = self.instance.add('tobe', 'duplicated', 254700000000)
        self.assertEqual('Contact exists!', response, msg="Cannot create duplicate contact records")

    def test_allows_similar_contact_names(self):
        self.instance.add('Name', 'Sake', 11144444444)
        self.instance.add('Name', 'Sake', 22244444444)
        self.assertTrue(11144444444 in self.instance.data.keys() and 22244444444 in self.instance.data.keys(), msg="Name sharing should be accepted!")

    def test_retrieves_contacts(self):
        self.instance.add('David', 'Kironde', 254790909090)
        self.retrieved_contacts = self.instance.view()
        self.assertTrue('David' == self.retrieved_contacts[254790909090][0] and "Kironde" == self.instance.data[254790909090][1], msg="Should retrieve contact and reflect the correct contact name!")

    def test_delete_contact(self):
        self.instance.add('extra', 'contact', 254711111111)
        self.instance.delete(254711111111)
        self.assertNotIn(254711111111, self.instance.data.keys(), msg="Deletes existing contact successfully!")

    def test_cannot_delete_nonexisting_contact(self):
        response = self.instance.delete(987654321)
        self.assertEqual("No such contact!", response, msg="Attempt to delete a non-existent contact should be handled!")

    def test_edit_contact(self):
        self.instance.add('outdated', 'name', 254720502050)
        self.instance.edit(254720502050, 'updated', 'name')
        self.assertTrue('updated' == self.instance.data[254720502050][0], msg="Contact info should be updated successfully!")

    def test_edit_works_only_for_existing_contacts(self):
        response = self.instance.edit(254704440666, 'edit', 'new')
        self.assertTrue('No such contact!' == response, msg="Only existing contacts can be edited!")


if __name__ == '__main__':
    unittest.main()
