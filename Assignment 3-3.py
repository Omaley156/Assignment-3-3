
validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 30

year = 0
month = 0
day = 0

year = input("Enter Year:")
month = input("Enter Month:")
day = input("Enter Day:")

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month  
     validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

if validDate == True:
    print("month/day/year is a valid date. ")
else:
    print("month/day/year is an invalid date. ")
