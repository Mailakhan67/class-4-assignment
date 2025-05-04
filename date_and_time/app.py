import datetime
import time
import math

# print(time.time())
 #x=datetime.datetime.now()
 #print(x)


#print(time.gmtime(0))



print(time.localtime(1746120480))




ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)



localtime = time.localtime(time.time())
print ("Local current time :", localtime)



localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)



import calendar
cal = calendar.month(2025, 1)
print ("Here is the calendar:")
print (cal)




# Poore saal (2025) ka calendar print karna
cal = calendar.calendar(2025)
print("Here is the calendar for the year 2025:")
print(cal)



from datetime import date

date1 = date(2023,4 ,19)
print("Date1:" , date1)

date2 = date(2023,4 ,30)
print("Date2:" , date2)


import datetime

x = datetime.datetime.now() #The date contains year, month, day, hour, minute, second, and microsecond.
print(x)






import datetime

x = datetime.datetime(2025, 1, 1)

print(x.strftime("%f")) #Display Microsecond 000000-999999
print(x.strftime("%A")) #Display the name of the Day
print(x.strftime("%Y")) #Display the Year
print(x.strftime("%B")) #Display the name of the month



