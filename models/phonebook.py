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

    def edit(self, number, firstname, surname):
        if number in self.data.keys():
            self.data[number] = [firstname, surname]
            return("Edit successful!")
        else:
            return("No such contact!")

    def view(self):
        return(self.data)

    def delete(self, number):
        if number in self.data.keys():
            del self.data[number]
            return("Contact deleted!")
        else:
            return("No such contact!")
