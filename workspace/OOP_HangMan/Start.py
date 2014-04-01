"""From here we Start the game"""
from ConfigParser import SafeConfigParser
from Player import Player
from Words import Word
from Game import Game, logging

def main():
    """hack"""
    parser = SafeConfigParser()
    parser.read('config.ini')

    shots = parser.getint('shots', 'number_of_tryes')

    current_word = Word()
    category = current_word.random_category()

    user = Player()
    player = user.ask_for_name()

    file_name = "%s.log" % player
    logging.basicConfig(filename=file_name, level=logging.DEBUG,
                         format='%(message)s')
    logging.info("USER:%s start the game and has %s wrong turns",
                  player, shots )
    logging.info("###### [word]:[hidden]:[guess]:[wrong_guess]:[right_guess]")
    
    word = current_word.random_word()
    print word
    
    play_fun = Game(word)
    
    play_fun.play()
    
if __name__ == "__main__":
    main()
