# -*- coding: utf-8 -*-


class Time():
    
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds)
    
    def int_to_time(self, seconds):
            time = Time()
            (minutes, time.seconds) = divmod(seconds, 60)
            (time.hours, time.minutes) = divmod(minutes, 60)
            return time
    
    def __add__(self, other):
        return self.int_to_time(self.time_to_int() + other.time_to_int())
    
    def print_time(self, time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
    
    def time_to_int(time):
        minutes = time.hours * 60 + time.minutes
        seconds = minutes * 60
        return seconds

start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
    
'''        
t1 = Time(4,5,36)
t2 = Time(4,5,37)
after = isafter(t1,t2)
#t.print_time(t)
'''