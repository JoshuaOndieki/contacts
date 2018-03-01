from contact import Contact

class Contacts():
    def __init__(self):
        self.data = {}

    def add(self, firstname, surname, number):
        if number not in self.data.keys():
            self.contact = Contact(firstname, surname, number)
            self.data[self.contact.number] = [firstname, surname]
            return("Contact added successfully!")
        else:
            return("Contact exists!")


    def edit(self):
        pass

    def view(self):
        pass

    def delete(self):
        pass
