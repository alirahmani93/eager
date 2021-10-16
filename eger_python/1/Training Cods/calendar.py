import calendar
#c = calendar.TextCalendar(calendar.MONDAY)
#str = c.formatmonth(2020,1,0,0)
#print(str)

hc = calendar.HTMLCalendar(calendar.week)
str = hc.formatmonth(2020,1)
print(str)

for i in c.itermonthday(2014,0):
    print(i)

for month in calendar.month_name:
    print(month)

for day in calendar.month_name:
    print(day)

for m in range(13):
    cal = calendar.monthcalendar(2019,m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone [calendar.FRIDAY] != 0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
        print('%10s %2d'% (calendar.month_name[m],meetday))