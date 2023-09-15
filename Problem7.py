'''
1. Using choices and timedelta functions
2. Using randrange and timedelta functions
3. Using numpy.random.choice and timedelta
'''
from datetime import date, timedelta
from random import choices
import random
import numpy as np

test_date1, test_date2 = date(2015, 6, 3), date(2015, 7, 1)
print("The original range : " + str(test_date1) + " " + str(test_date2))

K = 4

res_dates = [test_date1]

# loop to get each date till end date
while test_date1 != test_date2:
	test_date1 += timedelta(days=1)
	res_dates.append(test_date1)

res = choices(res_dates, k=K)
print(f"{K} random dates in range : " + str(res))


#2. Using randrange(), timedelta(), loop
# getting days between dates
test_date1, test_date2 = date(2015, 6, 3), date(2015, 7, 1)
dates_bet = test_date2 - test_date1
total_days = dates_bet.days
K = 6
 
res = []
for idx in range(K):
    random.seed(a=None)
     
    # getting random days until total_days i.e [:total_days+1]
    randay = random.randrange(total_days)
     
    # getting random dates
    res.append(test_date1 + timedelta(days=randay))
 
print(f"{K} random dates in range : " + str(res))

#3: Using numpy.random.choice() + timedelta()
test_date1, test_date2 = date(2015, 6, 3), date(2015, 7, 1)
print("The original range : " + str(test_date1) + " " + str(test_date2))

K = 4
res_dates = [test_date1]
while test_date1 != test_date2:
	test_date1 += timedelta(days=1)
	res_dates.append(test_date1)

res = np.random.choice(res_dates, K,replace= False)
print(f"{K} random dates in range : " + str(res))

