word = "python"
new = "-"*len(word)
gues = "h"
for i in range(len(word)):
    if word[i] in gues:
        new = new[:i] + word[i] +new[i+1:]
        
print new