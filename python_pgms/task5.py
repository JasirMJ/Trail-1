import time

tick=time.time()
print(tick)

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

localtime=time.asctime(time.localtime(time.time()))
print(localtime)

import calendar
cal=calendar.month(2019,1)
print(cal)

ti=time.clock()
print(ti)

#time.sleep(10)
call=calendar.calendar(2003,2,1,5)
print(call)
print(calendar.leapdays(1,12))
print("2009 is a leap year:",calendar.isleap(2009))
