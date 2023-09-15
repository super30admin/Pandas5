'''
1. a. We first calculate the number of days in date1 checking: 
Number of days added by leap years, if month is February or January then there is no possibility of getting an extra day so we decrease years to be considered by 1.
   b. Similarly we check for date2 and return the difference of number of days.
2. Using reduce from itertools
3. Using dateutil,rdelta function from the relativedelta module
4. Using time module
5. Using reduce from functools
'''

from datetime import date, datetime
from functools import reduce
from dateutil import relativedelta
import time


# 1. Approach 1
class Date:
	def __init__(self, d, m, y):
		self.d = d
		self.m = m
		self.y = y


# Store number of days in all months from January to Dec.
monthDays = [31, 28, 31, 30, 31, 30,
			31, 31, 30, 31, 30, 31]

# Count number of leap years before the given date
def countLeapYears(d):

	years = d.y
	# If month is Jan/Feb, do not include as leap year 
	if (d.m <= 2):
		years -= 1

	# leap year is a multiple of 4,400 and not 100
	return int(years / 4) - int(years / 100) + int(years / 400)

def getDifference(dt1, dt2):

	# Initialize number of days as years*365 + current month's days
	n1 = dt1.y * 365 + dt1.d

	# Add the number of days from the prev months using ref array
	for i in range(0, dt1.m - 1):
		n1 += monthDays[i]

	# Add a day for every leap year
	n1 += countLeapYears(dt1)

	# Similarly for date2
	n2 = dt2.y * 365 + dt2.d
	for i in range(0, dt2.m - 1):
		n2 += monthDays[i]
	n2 += countLeapYears(dt2)

	# return difference between two counts
	return (n2 - n1)

# Driver program
dt1 = Date(13, 12, 2018)
dt2 = Date(25, 2, 2019)

print(getDifference(dt1, dt2), "days")

# 2. Using reduce from itertools 
def numOfDays(date1, date2):
	return reduce(lambda x, y: (y-x).days, [date1, date2])

date1 = date(2018, 12, 13)
date2 = date(2019, 2, 25)
print(numOfDays(date1, date2), "days")


# 3. Using dateutil, you can use the rdelta function from the relativedelta module
date1 = datetime.strptime("13/10/2018", "%d/%m/%Y")
date2 = datetime.strptime("25/12/2018", "%d/%m/%Y")

# Calculate the difference between the two dates
difference = relativedelta.relativedelta(date2, date1)
# Print the number of days between the two dates
print(difference.months, "months", difference.days, "days")

# 4. Using time module
def days_between_dates(dt1, dt2):
	date_format = "%d/%m/%Y"
	a = time.mktime(time.strptime(dt1, date_format))
	b = time.mktime(time.strptime(dt2, date_format))
	delta = b - a
	return int(delta / 86400)

dt1 = "13/12/2018"
dt2 = "25/2/2019"
print(days_between_dates(dt1, dt2))

# 5. Using reduce from functools
def numOfDays(date1, date2):
    return reduce(lambda x, y: (y-x).days, [date1, date2])
 
date1 = date(2018, 12, 13)
date2 = date(2019, 2, 25)
print(numOfDays(date1, date2), "days")
