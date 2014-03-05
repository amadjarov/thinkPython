def tester():
    fin = open('words.txt', 'r')
    value = 1
    wordDict = dict()
    for word in fin:
        wordDict[word] = value
        value += 1
    fin.close()