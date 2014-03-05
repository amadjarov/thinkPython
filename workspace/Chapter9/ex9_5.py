def uses_all(word,required):
    for i in required:
        if i not in word:
            return False
    return True

print uses_all("babagama", "bagm")
print uses_all("babaasdgamra", "bagmtyuttyjuy")