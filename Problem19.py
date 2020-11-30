'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

months={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
print(months)
day=2 #Tuesday
cnt=0
for year in range(1901,2001):
    for month in months:
        day+=months[month]
        if year%4==0 and month=="February"  and  year%400!=0:
            day+=1
        if year==2000 and month=='December':#This will prevent the program from going to 2001 and checking whether 1st January 2001 is sunday or not
            break
        if day%7==0:
            cnt+=1
        
print(cnt," sundays occur fell on the first of the month")


#Another method
from datetime import date
cnt=0
for year in range(1901,2001):
    for month in range(1,13):
        day=date(year,month,1)
        if day.weekday()==6:
            cnt+=1
print(cnt," sundays occur fell on the first of the month")
