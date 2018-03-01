from models.contact import Contact


class Contacts():
    """Contains and manages all contacts. This is a phonebook instance.

    Args:
        This class takes no arguments

    Returns:
        Returns nothing.

    """

    def __init__(self):
        self.data = {}

    def add(self, firstname, surname, number):
        """Function for adding contacts to the phonebook instance.

        Args:
            firstname: First name of the contact owner.
            surname: Surname of the contact owner.
            number: The actual phone number of the owner.

        Returns:
            Returns "Contact added successfully!" when a contact is added
            with no issues.
            Returns an error message, "Contact exists!" when an attempt to duplicate is noted.

        """

        if type(number) is not int:
            raise(TypeError)
        # only add non-existent contacts
        if number not in self.data.keys():
            self.contact = Contact(firstname, surname, number)
            self.data[self.contact.number] = [firstname, surname]
            return("Contact added successfully!")
        else:
            return("Contact exists!")

    def edit(self, number, firstname, surname):
        """Function for editing contacts in the phonebook instance.

        Args:
            firstname: First name of the contact owner.
            surname: Surname of the contact owner.
            number: The actual phone number of the owner.

        Returns:
            Returns "Edit successful!" when a contact is edited
            with no issues.
            Returns an error message, "No such contact!" if the contact in
            question is not in the phonebook.

        """

        if type(number) is not int:
            raise(TypeError)
        # prevent accidental addition of new contacts by letting user know
        # if a contact is new.
        if number in self.data.keys():
            self.data[number] = [firstname, surname]
            return("Edit successful!")
        else:
            return("No such contact!")

    def view(self):
        """This function retrieves all existing contacts.

        Args:
            Takes no arguments.

        Returns:
            Returns all contacts in a dictionary format.

        """
        return(self.data)

    def delete(self, number):
        """Function for deleting contacts from the phonebook instance.

        Args:
            number: The contact number to be deleted.

        Returns:
            Returns "Contact deleted!" when a contact is deleted
            with no issues.
            Returns an error message, "No such contact!" if the
            if the contact did not exist on delete request.

        """

        if type(number) is not int:
            raise(TypeError)
        # Check for existence before deletion.
        if number in self.data.keys():
            del self.data[number]
            return("Contact deleted!")
        else:
            return("No such contact!")
