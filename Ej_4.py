import math
day = int(input("Enter a day:"))
while day <0 or day >31:
    day = int(input("Enter a correct day"))

month=int(input("Enter a month:"))
while month < 0 or month > 12:
    month = int(input("Enter a valid month"))

year=int(input("Enter a year:"))
while year < 0 or year > 9999:
    year = int(input("Enter a valid year"))    

a = (14 - month) / 12
y = year - a
m = month + 12 * a - 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) % 7  

def getDayOfWeek(d):
    if math.trunc(d) >=0:
        if math.trunc(d) == 0:
            return "Monday"
        elif math.trunc(d) == 1:
            return "Tuesday"
        elif math.trunc(d) == 2:
            return "Wenesday"
        elif math.trunc(d) == 3:
            return "Thursday"
        elif math.trunc(d) == 4:
            return "Friday"
        elif math.trunc(d) == 5:
            return "Saturday"
        elif math.trunc(d) == 6:
            return "Sunday"
        else:
            return "Incorrect"
    else:
        return "Incorrect"
print(f"For the day {day}, the month {month} and the year {year}. The date falls on {getDayOfWeek(d)}")