import os
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()

fo = open("foo.txt", "r+")
stri = fo.read()
print "Read String is : ", stri
# Close opend file
fo.close()

str =os.getcwd() 
print str
os.mkdir("bambam")
#os.rmdir("bambam")
