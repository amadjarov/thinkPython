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
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

word = random.choice(words)
print word
noRepeatWord="".join(set(word))
wrongGuess = ""
rightGuess = ""

    
print " Hello this is HANGMAN game!!! Enjooy"
print " U can guess wrong only 6 times"
print "Hint : words are only animals "
print HANGMANPICS[0]
def display(HANGMANPICS, wrongGuess):
    print HANGMANPICS[len(wrongGuess)]
        
def getChar(wrongGuess, allreadyGuess):
    leng = 0
    while leng < 6:
        print " Please enter a character"
        guess = raw_input()
        guess = guess.lower()
       
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in allreadyGuess: #==Change here
            return guess
        else:
            print "You should enter only one character from the alphabet without repeating it"

while True:
    allreadyGuess = wrongGuess + rightGuess #================== change her
    guess = getChar(wrongGuess, allreadyGuess)
    
    if guess in word:
        rightGuess += guess
    else:
        wrongGuess += guess
    
    display(HANGMANPICS, wrongGuess)
    
    if len(wrongGuess) == 6:
        print " You loose the word was {"+word+"} try next time"
        sys.exit()
    if len(rightGuess) == len(noRepeatWord):
        print " You are smart the word was {"+word+"} Good job"
        sys.exit()