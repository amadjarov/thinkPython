from Words import *
from Player import *
from calssDisplayMe import *
import logging
import gettext
class Game(object):

    display = desplayME()

    def __init__(self,word,wrongGuess="",rightGuess="",SHOTS=6,hidden=""):
        self.word=word
        self.wrongGuess=wrongGuess
        self.rightGuess=rightGuess
        self.SHOTS=SHOTS
        self.hidden=hidden
        self.allreadyGuess=self.rightGuess + self.wrongGuess
        
    
    def get_hidden(self):
        """
        Create the "hidden" word wit dashes "-" equal to the number of characters
        in the word and return this "hidden" word
        """
        self.hidden = '-'*len(self.word)
        for i in range(len(self.word)):
            if self.word[i] in self.rightGuess:
                self.hidden = self.hidden[:i] + self.word[i] +self.hidden[i+1:]
        return self.hidden
    
    def getChar(self):
        """
        Create an object from the Player class ask the actor to enter a character
        check if this character is vlid one and return it
        """
        #while True:
        user = Player()
        guess = user.askForChar()
        guess = guess.lower()
                
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in self.allreadyGuess: #==Change here
            self.guess = guess
                #return
        else:
            self.display.desplayText("valid")

    
    def play(self):
        noRepeatWord="".join(set(self.word))
        hidden = "-"*len(self.word)
        while True:
            do_exit = False
            result = None
            self.allreadyGuess = self.wrongGuess + self.rightGuess #================== change here
            self.getChar()
            if self.guess in self.word:
                self.rightGuess += self.guess
        
            else:
                self.wrongGuess += self.guess
    
            hidden = self.get_hidden()
    
            self.display.set_state(self.word, hidden, self.wrongGuess)
            self.display.desplayMan()
            self.display.desplayHidden()
    
            logging.info("%s:%s:%s:%s:%s",self.word ,self.hidden ,self.guess ,self.wrongGuess, self.rightGuess)
    
            if len(self.wrongGuess) == self.SHOTS:
                self.display.desplayText("lose")
                result = 'lost'

            if len(self.rightGuess) == len(noRepeatWord):
                self.display.desplayText("win")
                result = 'win'
            if result is not None:
                logging.info("Player %s and finish the game", result )
                exit()
                
                
    