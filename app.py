"""
    Usage:
        add <firstname> <surname> <number>
        edit <number> <firstname> <lastname>
        view
        delete <number>
        quit
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
    os.system("clear")
    print(__doc__)


class APP(cmd.Cmd):
    prompt = magenta("CONTACTS $$$ ")

    @docopt_cmd
    def do_add(self, arg):
        """Usage: add <firstname> <surname> <number>"""
        firstname = arg["<firstname>"]
        surname = arg["<surname>"]
        number = arg["<number>"]
        response = app_instance.add(firstname, surname, number)
        if "success" in response:
            print(success("\t\t\t\t\t\t" + response))
        else:
            print(error("\t\t\t\t\t\t" + response))

    def do_edit(self, arg):
        """Usage: edit <number> <firstname> <surname>"""
        pass

    def do_view(self, arg):
        data = app_instance.view()
        # Generate a table for the data.
        data_table = table(data)
        print(data_table)

    def do_delete(self, arg):
        """Usage: <number>"""
        pass

    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        os.system('clear')
        print ('Contacts has quit')
        exit()


if __name__ == "__main__":
    try:
        intro()
        app_instance = Contacts()
        APP().cmdloop()
    except KeyboardInterrupt:
        os.system("clear")
        print('Contacts has quit!')
