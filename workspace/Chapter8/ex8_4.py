def find(word, letter, index):
    index = index
    while index < len(word):
        if word[index] == letter:
            print index
            break
        index += 1
    else:
        print - 1

find ("bagarom", "r", 0)