def print_n(s, n):
    if n <= 0:
        return
    print s
    print_n(s, n-1)
     
print_n(5, 10)

def print_n2(s, n):
    while n > 0:
        print s
        n -=1
        
print_n2(5, 10)