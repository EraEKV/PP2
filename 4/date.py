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