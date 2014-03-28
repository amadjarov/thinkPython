from ConfigParser import SafeConfigParser
import gettext
from Display import *
from Player import *
from Words import *
from Game import *


parser = SafeConfigParser()
parser.read('config.ini')

SHOTS = parser.getint('shots', 'number_of_tryes')

currentWord = Word()
category = currentWord.randomCategory()

user = Player()
player=user.askForName()

fileName = "%s.log" %player
logging.basicConfig(filename=fileName,level=logging.DEBUG, format='%(message)s')
logging.info("USER:%s start the game and has %s wrong turns", player,SHOTS )
logging.info("###### [word]:[hidden]:[guess]:[wrongGuess]:[rightGuess]")

word = currentWord.randomWord()
print word

playFun = Game(word)

playFun.play()
