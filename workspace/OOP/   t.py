a=1
b=2
c=3
print a 
print b 
print c
a,b,c = c,a,b

print a
print b
print c
for i in [1,2,3,4,5]:
    print "This is iteration number", i
    

x = 10
while x >= 0:
    print "x is still not negative."
    x = x-1
    
#===============================================================================
# for value in range(100):
#     print value
#===============================================================================

#===============================================================================
# x = input("Please enter a number: ")
# print type(x)
#===============================================================================
list= ["spam","spam","spam","spam","spam","eggs","and","spam"]
print list[-2]