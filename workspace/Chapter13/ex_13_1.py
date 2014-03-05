import string
 
punctuations = [mark for mark in string.punctuation]
whitespaces = [char for char in string.whitespace]
#split into words
def words():
    data = open('origin.txt', 'r')
    main = []
    for line in data:
        for item in line.split():
            main.append(item)
    return main
    data.close()
 
#remove punctuation, whitespace, uppercase
def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuations) or (char in whitespaces)):
            pass
        else:
            cleansed += char.lower()
    return cleansed