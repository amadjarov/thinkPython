def has_no_e(word):
    for i in word:
        if i == "e":
            return False
    return True

fin = open('words.txt')

total_words = 0
words_without_e = 0
percent_without_e = 0.0

for line in fin:
    word = line.strip() #renove the empty spaces
    if has_no_e(word):
        print word
        words_without_e += 1
    total_words += 1

percent_without_e = ( words_without_e / total_words ) * 100
