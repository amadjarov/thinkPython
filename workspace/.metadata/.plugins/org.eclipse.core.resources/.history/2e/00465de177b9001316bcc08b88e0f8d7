import random
class Word(object):
    def randomCategory(self):
        """
        Randomly select one category
        """
        self.category = (random.choice(["colors","animals","others"]))
        return self.category
    def randomWord(self):
        """
        Open the file with the category and randomly select one word from it
        """
        with open(self.category) as f:
                words = f.read().split()
        word = random.choice(words)
        return word