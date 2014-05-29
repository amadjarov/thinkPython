"""Player"""
import gettext

T = gettext.translation('config2', "./locales", languages=['bg_BG','en_US'])
_ = T.ugettext

class MyError(Exception):
    """Class for exception"""
 
    def __init__(self, value="Error my friend"):
        self.value = value
    def __str__(self):
        return repr(self.value)


class Player(object):
    """ Class for the player initialization"""

    name = ''
    char = ''
    def ask_for_name(self):
        """
        Continually ask the user to type the name and rejects an empty string
        """
        while not self.name:
            self.name = raw_input(_("Please enter a name"))

        return self.name

    def ask_for_char(self):
        """
        Ask the user to type a character
        """
        self.char = raw_input(_("Please enter a char"))
        return self.char
