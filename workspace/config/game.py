import random
from ConfigParser import SafeConfigParser
import gettext
import logging
from calssDisplayMe import *
from Player import *

t = gettext.translation('config', "./locales", languages=['bg_BG','en_US'])
_ = t.ugettext

parser = SafeConfigParser()
parser.read('config.ini')

SHOTS = parser.getint('shots', 'number_of_tryes')
fileWords = parser.get('categories', 'file_with_words')

user = Player()
player=user.askForName()

fileName = "%s.log" %player
logging.basicConfig(filename=fileName,level=logging.DEBUG, format='%(message)s')
logging.info("USER:%s start the game and has %s wrong turns", player,SHOTS )
logging.info("###### [word]:[hidden]:[guess]:[wrongGuess]:[rightGuess]")

with open(fileWords) as f:
    words = f.read().split()

word = random.choice(words)
print word

wordLength = len(word)
noRepeatWord="".join(set(word))
wrongGuess = ""
rightGuess = ""
hidden = "-"*wordLength

def get_hidden(word, rightGuess):
    hidden = '-'*len(word)
    for i in range(len(word)):
        if word[i] in rightGuess:
            hidden = hidden[:i] + word[i] +hidden[i+1:]
    return hidden

def getChar(allreadyGuess):
    """
    Ask the user to guess a character, check the entered value to be in the
    alphabet, to be one single character, and NOT to be all ready typed in 
    
    >>>Please enter a character
    >>>1
    You should enter only one character from the alphabet without repeating it
    
    >>>Please enter a character
    >>>asdasd
    You should enter only one character from the alphabet without repeating it
    
    >>> Please enter a character
    >>>a
    True
    """
    leng = 0
    while leng < SHOTS:
        print _(" Please enter a character")
        guess = user.askForChar()
        guess = guess.lower()
        
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in allreadyGuess: #==Change here
            
            return guess
            
        else:
            print _("You should enter only one character from the alphabet without repeating it")

print _(" Hello this is HANGMAN game!!! Enjooy")
print _(" U can guess wrong only 6 times")
print _(" Hint : words are only animals ")
print _(" The word you should guess has {word_length} characters ").format(word_length=wordLength)
print hidden
#print HANGMANPICS[0]

desplay=desplayME()

while True:
    do_exit = False
    result = None
    allreadyGuess = wrongGuess + rightGuess #================== change her
    guess = getChar(allreadyGuess)
    
    if guess in word:
        rightGuess += guess
        
    else:
        wrongGuess += guess
    
    hidden = get_hidden(word, rightGuess)
    
    desplay.set_state(word, hidden, wrongGuess)
    desplay.desplayMan()
    desplay.desplayHidden()
    
    logging.info("%s:%s:%s:%s:%s",word ,hidden ,guess ,wrongGuess, rightGuess)
    
    if len(wrongGuess) == SHOTS:
        print _(" You lose the word was[ {word} ] try next time").format(word=word)
        result = 'lost'

    if len(rightGuess) == len(noRepeatWord):
        print _(" You are smart the word was [ {word} ] Good job").format(word = word)
        result = 'win'
    if result is not None:
        logging.info("user:%s %s and finish the game", result )
        exit()
