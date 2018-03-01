from termcolor import colored, cprint
from prettytable import PrettyTable


def success(text):
    """Returns a green colored text
    """
    return(colored(text, 'green', attrs=['blink', 'bold']))


def magenta(text):
    """Returns a green colored text
    """
    return(colored(text, 'magenta', attrs=['blink', 'bold']))


def error(text):
    """Returns a red colored text
    """
    return(colored(text, 'red', attrs=['blink', 'bold']))


def table(data):
    """Generates and returns a table
    """
