def avoids(word, forbidden):
    for i in word:
        if i in forbidden:
            return False
    
    return True


