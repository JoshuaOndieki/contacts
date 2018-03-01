
class Contact():
    """Contact class for generating a single phonebook contact instance

    Args:
        firstname: First name of the contact owner.
        surname: Surname of the contact owner.
        number: The actual phone number of the owner.

    Returns:
        This class initializes a contact instance and returns nothing

    """

    def __init__(self, firstname, surname, number):
        self.firstname = firstname
        self.surname = surname
        self.number = number
