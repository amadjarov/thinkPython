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

def display(HANGMANPICS):
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
    
    print HANGMANPICS[6]


    
display(HANGMANPICS)