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
print words

word = random.choice(words)
print word
wordIndex = words.index(word) # find where is the randomly chosen word in the list
#print wordIndex
#print "Your word has " +str(len(word))+ " characters"
#print "".join(words)
print "-" * len(word)

wrongGuess = ""
rightGuess = ""
leng = len(wrongGuess)

    
print " Hello this is HANGMAN game!!! Enjooy"
print " U can guess wrong only 6 times"
print HANGMANPICS[0]

def display(HANGMANPICS, wrongGuess):
    print HANGMANPICS[len(wrongGuess)]
        
def getChar(wrongGuess): 
    while leng < 6:
        print " Please enter a character"
        guess = raw_input()
        guess = guess.lower()
       
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz":
            return guess
            
        else:
            print "You should enter only one character from the alphabet"

while True:
    
    guess = getChar(wrongGuess)
    
    if guess in word:
        rightGuess += guess
    else:
        wrongGuess += guess

    display(HANGMANPICS, wrongGuess)
    
    if len(wrongGuess) == 6:
        print " You loose stupid bitch"
        sys.exit()
    if len(rightGuess) == len(word):
        print "DAAAAAAAAMN  You are a smart the word was {"+word+"} Good job"
        sys.exit()