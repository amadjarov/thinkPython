def count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    print count
        
count ("banana", "n" )