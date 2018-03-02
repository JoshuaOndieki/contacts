"""
                        Thank You for using Contacts app!
Type help for assistance.
Or type help followed by the command you need help on.
    Usage:
        add <firstname> <surname> <number>
        edit <number> <firstname> <lastname>
        delete <number>
        view
        quit
        help
"""

from docopt import docopt, DocoptExit
from models.phonebook import Contacts
from ui import success, error, table, magenta
import cmd
import os


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    print(__doc__)


class APP(cmd.Cmd):
    """Application instance class.
    """
    prompt = magenta("CONTACTS $$$ ")

    @docopt_cmd
    def do_add(self, arg):
        """Usage: add <firstname> <surname> <number>"""
        try:
            self.firstname = arg["<firstname>"]
            self.surname = arg["<surname>"]
            self.number = arg["<number>"]
            self.response = app_instance.add(self.firstname, self.surname, self.number)
            if "success" in self.response:
                print(success("\t\t\t\t\t\t" + self.response))
            else:
                print(error("\t\t\t\t\t\t" + self.response))
        except Exception as e:
            print(e)
            print(error("\t\t\t\tInvalid data!"))

    @docopt_cmd
    def do_edit(self, arg):
        """Usage: edit <number> <firstname> <surname>"""
        try:
            self.firstname = arg["<firstname>"]
            self.surname = arg["<surname>"]
            self.number = arg["<number>"]
            self.response = app_instance.edit(self.number, self.firstname, self.surname)

            if "success" in self.response:
                print(success("\t\t\t\t\t\t" + self.response))
            else:
                print(error("\t\t\t\t\t\t" + self.response))
        except Exception as e:
            print(e)
            print(error("\t\t\t\tInvalid data!"))

    @docopt_cmd
    def do_view(self, arg):
        """Usage: view"""
        self.data = app_instance.view()
        # Generate and print table for the data.
        print(table(self.data))

    @docopt_cmd
    def do_delete(self, arg):
        """Usage: delete <number>"""
        try:
            self.number = arg["<number>"]
            self.response = app_instance.delete(self.number)
            if "deleted" in self.response:
                print(success("\t\t\t\t\t\t" + self.response))
            else:
                print(error("\t\t\t\t\t\t" + self.response))
        except Exception as e:
            print(e)
            print(error("\t\t\t\tInvalid data!"))

    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        self.text = magenta("Contacts has quit")
        os.system('cls' if os.name == 'nt' else 'clear')
        print (self.text)
        exit()


if __name__ == "__main__":
    try:
        app_instance = Contacts()
        os.system('cls' if os.name == 'nt' else 'clear')
        intro()
        APP().cmdloop()
    except KeyboardInterrupt:
        text = magenta("Contacts has quit")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(text)
