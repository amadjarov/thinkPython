def format_list(list):
    """
    Take a sequence as a parameter and prints its vlues as a single string with
    new line at the end
    
    >>> format_list(["a", "b", "c"])
    a,b,c
    
    """
    
    print ",".join(list)

format_list(["a", "b", "c"])
