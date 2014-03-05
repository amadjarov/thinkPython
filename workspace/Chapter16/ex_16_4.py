from copy import deepcopy
 
def increment(time, seconds):
    r = deepcopy(time)
 
    r.second += seconds
    r.minute += r.second//60
    r.hour += r.minute//60
 
    r.second %= 60
    r.minute %= 60
    r.hour %= 24
 
    return r