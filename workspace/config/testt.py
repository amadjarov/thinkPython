class DoesNotCompute(Exception):
    """ Easy to understand naming conventions work best! """
    pass

def this_function(x):
    """ This function only works on numbers."""
    try:
        print x ** x
    except TypeError:
        raise DoesNotCompute

this_function("g")