def check_fermat(a, b, c, n):
    if a**n + b**n == c**n and n >2:
        print "Holy shits, Fermat was wrong!"
    else:
        print "Nope, that doesnt work"
        
check_fermat(2,3,5,2)
    