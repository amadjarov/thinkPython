def increment(time, seconds):
 
    n = seconds/60
    time.second += seconds - 60.0*n
    time.minute += n
 
    m = time.minute/60
    time.minute -= m*60
    time.hour += m
