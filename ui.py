from termcolor import colored
from prettytable import PrettyTable


def success(text):
    """Returns a green colored text
    """
    return(colored(text, 'green', attrs=['blink', 'bold']))


def magenta(text):
    """Returns a magenta colored text
    """
    return(colored(text, 'magenta', attrs=['blink', 'bold']))


def error(text):
    """Returns a red colored text
    """
    return(colored(text, 'red', attrs=['blink', 'bold']))


def table(data):
    """Generates and returns a table
    """

    x = PrettyTable()
    name = colored("Name", 'blue')
    phone_number = colored("Phone Number", 'blue')
    x.field_names = [name, phone_number]

    for contact in data:
        contact_name = data[contact][0] + " " + data[contact][1]
        x.add_row([contact_name, contact])

    x.sortby = name
    return(x)
