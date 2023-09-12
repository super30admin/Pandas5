# Problem 3 :Python program to find number of days between two given dates
# Using Python datetime module:

from datetime import date


def numOfDays(date1, date2):
#check which date is greater to avoid days output in -ve number
	if date2 > date1:
		return (date2-date1).days
	else:
		return (date1-date2).days


date1 = date(2018, 12, 13)
date2 = date(2015, 2, 25)
print(numOfDays(date1, date2), "days")




from dateutil import relativedelta
from datetime import datetime

# Parse the dates from strings into datetime objects
date1 = datetime.strptime("13/10/2018", "%d/%m/%Y")
date2 = datetime.strptime("25/12/2018", "%d/%m/%Y")

# Calculate the difference between the two dates
difference = relativedelta.relativedelta(date2, date1)
# Print the number of days between the two dates
print(difference.months, "months", difference.days, "days")



import time


def days_between_dates(dt1, dt2):
	date_format = "%d/%m/%Y"
	a = time.mktime(time.strptime(dt1, date_format))
	b = time.mktime(time.strptime(dt2, date_format))
	delta = b - a
	return int(delta / 86400)


dt1 = "13/12/2018"
dt2 = "25/2/2019"
print(days_between_dates(dt1, dt2))


