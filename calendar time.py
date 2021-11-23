import time

print(time.time())
print(time.localtime(time.time()))

import calendar

print(calendar.month(1995,12))
calendar.setfirstweekday(6)
print(calendar.month(1995,12))
print('2021 is leap : ', calendar.isleap(2021))
print(calendar.calendar(2021))

