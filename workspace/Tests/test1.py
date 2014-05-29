import re
a = "Once upon a time there was a little red hooded girl"
b =  re.search(r"banan", a)
if b:
    print b.group()
else:
    print "No match"

print re.sub(r"upon", r"bonbon", a)

raw = r'this\t\n and that'
print raw