from calssDisplayMe import *

with open('list.txt') as f:
    for line in f:
        if line.startswith("#"):
            pass

fo=open("list.txt")
lines=fo.readlines()
lineAsList = lines[1].split(":")
print lineAsList[1]   

fo=open("list.txt")
lines=fo.readlines()
lineAsList = lines[4].split(":")

achoHang = desplayME()
achoHang.set_state(lineAsList[0], lineAsList[1],lineAsList[3])
achoHang.desplayMan()
achoHang.desplayHidden()
