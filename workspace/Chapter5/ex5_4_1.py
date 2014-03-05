def is_triangle(a, b, c):
    if a + b == c or a + c ==b or c + b == a:
        print "YES"
    else:
        print "NO"
        
is_triangle(3 , 1, 1)
