def is_power(a, b):
    if a % b == 0 and a/b % b == 0:
        #str(a)
        #str(b)
        print str(a) + " is power of " + str(b)
    else:
        print str(a) + " is not power of " + str(b)
        
        
is_power(6, 3)
    