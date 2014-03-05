a = input("Please type value for a\n")
b = input("Please type value for b\n")
c = input("Please type value for c\n")
int(a)
int(b)
int(c)
 
def is_triangle(a, b, c):
    if a + b == c or a + c ==b or c + b == a:
        print "YES"
    else:
        print "NO"
        
is_triangle(a , b, c)