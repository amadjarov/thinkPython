import gettext
t = gettext.translation('config2', "./locales", languages=['bg_BG','en_US'])
_ = t.ugettext
class MyError(Exception):
    def __init__(self, value="Error my friend"):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Player(object):
    def askForName(self):
        """
        Continually ask the user to type the name and rejects an empty string
        """
        while True:
            player = raw_input(_("Please enter a name"))
            if player: # will reject an empty string
                break
        return player
    
    def askForChar(self):
        """
        Ask the user ot type a character
        """
        char = raw_input(_("Please enter a char"))
        return char
