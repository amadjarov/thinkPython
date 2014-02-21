a = input("Please enter a value for a\n")
b = input("Please enter a value for b\n")
c = input("Please enter a value for c\n")
n = input("Please enter a value for n\n")
int(a)
int(b)
int(c)
int(n)
def check_fermat(a, b, c, n):
    if a**n + b**n == c**n and n >2:
        print "Holy shits, Fermat was wrong!"
    else:
        print "Nope, that doesnt work"

check_fermat(a, b, c, n)