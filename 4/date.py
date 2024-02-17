from datetime import datetime, timedelta

current = datetime.now()



# 1 Write a Python program to subtract five days from current date.

# five = current - timedelta(days = 5)
# print(five)





# 2 Write a Python program to print yesterday, today, tomorrow

# yesterday = current - timedelta(days = 1)
# tomorrow = current + timedelta(days = 1)

# print(yesterday.strftime("%A"), current.strftime("%A"), tomorrow.strftime("%A"))




# 3 Write a Python program to drop microseconds from datetime.

# now = current.replace(microsecond = 0)
# print(now)





# 4 Write a Python program to calculate two date difference in seconds.

# from math import ceil 

# second_date = '2024-01-18 15:12:22'

# date1 = current
# date2 = datetime.strptime(second_date, "%Y-%m-%d %H:%M:%S")

# seconds = (date1 - date2).total_seconds()
# print(ceil(seconds))





# %a	    Weekday, short version	Wed	
# %A	    Weekday, full version	Wednesday	
# %w	    Weekday as a number 0-6, 0 is Sunday	3	
# %d	    Day of month 01-31	31	
# %b	    Month name, short version	Dec	
# %B	    Month name, full version	December	
# %m	    Month as a number 01-12	12	
# %y	    Year, short version, without century	18	
# %Y	    Year, full version	2018	
# %H	    Hour 00-23	17	
# %I	    Hour 00-12	05	
# %p	    AM/PM	PM	
# %M	    Minute 00-59	41	
# %S	    Second 00-59	08	
# %f	    Microsecond 000000-999999	548513	
# %z	    UTC offset	+0100	
# %Z	    Timezone	CST	
# %j	    Day number of year 001-366	365	
# %U	    Week number of year, Sunday as the first day of week, 00-53	52	
# %W	    Week number of year, Monday as the first day of week, 00-53	52	
# %c	    Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	    Century	20	
# %x	    Local version of date	12/31/18	
# %X	    Local version of time	17:41:00	
# %%	    A % character	%	
# %G	    ISO 8601 year	2018	
# %u	    ISO 8601 weekday (1-7)	1	
# %V	    ISO 8601 weeknumber (01-53)	01