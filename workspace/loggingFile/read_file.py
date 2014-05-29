with open("example.log", "r") as f:
    for line in f:
        print line.split(':')
 
 
fo = open("example.log")
for line in fo.readlines():
    pa= line.split(':')
    print pa
    
