class Time(object):
    pass

time1 = Time()
time1.hour = 11
time1.minute = 33
time1.second = 30

time2 = Time()
time2.hour = 12
time2.minute = 33
time2.second = 30

def is_after(t1, t2):
    print (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

is_after(time1, time2)
