from version1 import *
import sys
print """ Hello this is HANGMAN game!!! Enjooy"
 U can guess wrong only 6 times"
"""
print " The word has you should guess has "+ str(wordLength)+" characters"
print hidden
print HANGMANPICS[0]

while True:
    allreadyGuess = wrongGuess + rightGuess #================== change her
    guess = getChar(wrongGuess, allreadyGuess)
    
    if guess in word:
        rightGuess += guess
    else:
        wrongGuess += guess
    
    display(HANGMANPICS, wrongGuess)
    
    if len(wrongGuess) == SHOTS:
        print " You loose the word was {"+word+"} try next time"
        sys.exit()
    if len(rightGuess) == len(noRepeatWord):
        print hidden

        print " You are smart the word was hhhh {"+word+"} Good job"

        sys.exit()