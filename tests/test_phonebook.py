import unittest
from models.phonebook import Contacts


class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.instance = Contacts()

    def test_add_contact(self):
        self.instance.add('Joshua', 'Ondieki', '0700009999')
        self.instance.add('Andela', 'Kenya', '0788880000')
        self.instance.add('David', 'Kironde', '0790909090')
        self.instance.add('extra', 'contact', '0711111111')
        self.instance.add('outdated', 'name', '0720502050')
        self.assertEqual(self.instance.data, 3, msg="Should indicate 3 contacts present in phone book!")

    def test_cannot_add_duplicates(self):
        self.instance.add('tobe', 'duplicated', '0700000000')
        response = self.instance.add('tobe', 'duplicated', '0700000000')
        self.assertEqual('Contact exists!', response, msg="Cannot create duplicate contact records")

    def test_retrieves_contact(self):
        self.assertTrue('Joshua' == self.instance.data['0700009999'][0] and self.instance.data['0700009999'][1], msg="Should retrieve contact and reflect the correct contact name!")

    def test_delete_contact(self):
        self.instance.delete('0711111111')
        self.assertNotIn('0711111111', self.instance.data.keys(), msg="Deletes existing contact successfully!")

    def test_edit_contact(self):
        self.instance.edit('0720502050', 'updated', 'name')
        self.assertTrue('updated' == self.instance.data['0720502050'][0], msg="Contact info should be updated successfully!")

    def test_edit_works_only_for existing_contacts(self):
        response = self.instance.edit('0704440666', 'edit', 'new')
        self.assertTrue('No such contact!', response, msg="Only existing contacts can be edited!")


if __name__ == '__main__':
    unittest.main()