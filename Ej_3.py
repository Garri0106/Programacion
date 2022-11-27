year = int(input("Enter a year:"))

while year < 0 or year >9999:
    year = int(input("Enter a valid year:"))

month = int(input("Enter a month (in number):"))

while month < 0 or month > 12:
    month = int(input("Enter a valid month:"))

def isLeapYear(year):
    if year %4==0 and (year %100 != 0 or year %400==0):
        return True
    else:
        return False
    
def computeDaysInMonth(month):
    days = 0
    if month == 1:
        days = 31
    elif month == 2 and isLeapYear(year) == True:
        days = 29
    elif month == 2 and isLeapYear(year) == False:
        days = 28
    elif month == 3:
        days = 31
    elif month == 4:
        days = 30
    elif month == 5:
        days = 31
    elif month == 6:
        days = 30
    elif month == 7:
        days = 31
    elif month == 8:
        days = 31
    elif month == 9:
        days = 30
    elif month == 10:
        days = 31
    elif month == 11:
        days = 30
    elif month == 12:
        days = 31
    return days

print(f"For the year {year}, the month {month} have a total of {computeDaysInMonth(month)} days.")