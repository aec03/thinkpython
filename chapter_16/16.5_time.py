class Time(object):
    """ represents time

    attributes: hour, minute, second """

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
    

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def mul_time(time, num):
    seconds = time_to_int(time) * num
    return int_to_time(seconds)


def div_time(time, num):
    seconds = time_to_int(time) / num
    return int_to_time(seconds)


#time objects
t1 = Time()
t1.hour = 3
t1.minute = 00
t1.second = 00

t2 = Time()
t2.hour = 3
t2.minute = 43
t2.second = 32

# marathon average pace (time per mile)
print_time(div_time(t1, 26.2))