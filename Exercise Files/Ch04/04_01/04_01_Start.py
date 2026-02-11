# Datetime Module Part I
from datetime import datetime, timedelta
import calendar
import time

run = input("Start? >")
seconds = 0

if run == "yes":
    while seconds != 10:
        print(">", seconds)
        time.sleep(1)
        seconds += 1
        
        





# now = datetime.now()
# testdate = now + timedelta(days=2)
# myfirstlinkedincourse = now - timedelta(weeks=3)

# print(testdate.date())

# print(myfirstlinkedincourse.date())

# cal = calendar.month(2026, 10)
# cal2 = calendar.weekday(2026, 1, 31)
# print(cal)
# print(cal2)
# print(calendar.isleap(2024))
# print(now.strftime("%a %A %d"))
# print(now.strftime("%b %B %m"))

# print(now.strftime("%a %B %d"))
# print(now.strftime("%H : %M : %S :%p"))

# now = datetime.now()
# print(now.date())
# print(now.year)
# print(now.month)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.time())
