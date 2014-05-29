import random

SHOTS = 6
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
a = 'colors'
with open(a) as f:
    words = f.read().split()
#words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule hiddent otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

word = random.choice(words)
print word
wordLength = len(word)
noRepeatWord="".join(set(word))
wrongGuess = ""
rightGuess = ""
hidden = "-"*wordLength
    

def display(HANGMANPICS, wrongGuess):
    """
    Displays the pictures from HANGMANPIC according to the wronGuess number
    
    >>> display(HANGMANPICS, 1):
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    
    >>> display(HANGMANPICS, 1):
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """
    global hidden
    print HANGMANPICS[len(wrongGuess)] #================second change here
    for i in range(len(word)):
        if word[i] in rightGuess:
            hidden = hidden[:i] + word[i] +hidden[i+1:]
        
def getChar(wrongGuess, allreadyGuess):
    """
    Ask the user to guess a character, check the entered value to be in the
    alphabet, to be one single character, and NOT to be all ready typed in 
    
    """
    leng = 0
    while leng < SHOTS:
        print " Please enter a character"
        print hidden
        guess = raw_input()
        guess = guess.lower()
        
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in allreadyGuess: #==Change here
            return guess
        else:
            print "You should enter only one character from the alphabet without repeating it"

