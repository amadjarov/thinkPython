import random
import sys
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

with open('pythonwords.txt') as f:
    words = f.read().split()

word = random.choice(words)
noRepeatWord="".join(set(word))
hidden = "-" * len(word)

class HangMan(object):
    def __init__(self,word):
        self.word = word
        self.wrongGuess = ""
        self.rightGuess = ""
    
    def gues(self, letter):
        if letter in self.word and letter not in self.wrongGuess:
            self.wrongGuess += letter
        if letter not in self.word and letter not in self.rightGuess:
            self.rightGuess += letter
    
    def display(self):
        print HANGMANPICS[len(self.wrongGuess)]
        for i in range(len(word)):
            if word[i] in self.rightGuess:
                hidden = hidden[:i] + word[i] +hidden[i+1:]
        print hidden
    def hangman_win(self):
        if len(self.rightGuess) == len(noRepeatWord):
            print " You are smart the word was hhhh {"+word+"} Good job"
            sys.exit()
            
    def hangman_lose(self):
        if len(self.wrongGuess) == 6:
            print " You loose the word was {"+word+"} try next time"
            sys.exit()
        
def main():
    game = HangMan(word)
    
