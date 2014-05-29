def fibo(n):
    """
    Print fibbonachi series up to n
    
    >>> fibo(5)
    1 1 2 3
    
    """
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b
    
fibo(5)