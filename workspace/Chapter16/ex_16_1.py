class Time(object):
    pass

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(t):
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)
    
print_time(time)