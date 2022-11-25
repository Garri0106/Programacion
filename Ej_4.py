day = int(input("Enter the day:"))
month = int(input("Enter the month:"))
year = int(input("Enter the year"))
def getDaysOfWeek(day, month, year):
    a = (14 - month) / 12
    y = year - a
    m = month + 12 * a - 2
    d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) % 7
    return a, d, m, y
    
print(getDaysOfWeek(day, month, year))