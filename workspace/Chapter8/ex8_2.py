prefixes = "JKLMNOPQ"
suffix = "ack"

for i in prefixes:
    if i == "O" or i == "Q":
        print i + "u" + suffix
    else:
        print i + suffix
    
    