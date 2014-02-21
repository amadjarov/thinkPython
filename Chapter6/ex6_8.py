def gcd(a, b):
    if b == 0:
        print a
    else:
        r = a % b
        return gcd(b,r)

gcd(6, 3)