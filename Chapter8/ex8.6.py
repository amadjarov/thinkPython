def find(word, letter, index):
    index = index
    while index < len(word):
        if word[index] == letter:
            print index
            break
        index += 1
    else:
        print - 1


def count_v2 (word, letter, start):
    
    how_many = 0
    index = find(word, letter, start)
    
    if index == -1:
        how_many = 0
    else:
        while index > -1:
            how_many = how_many + 1
            index = index+1
            index = find(word, letter, index)
    print how_many
    
count_v2 ('banana', 'x', 0)    
count_v2 ('banana', 'a', 4)
count_v2 ('banana', 'a', 2)
count_v2 ('banana', 'a', 0)