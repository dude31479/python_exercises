import datetime
from leap_year import isLeapYear


def is_valid_date(year, month, day):
    if (month < 1 or month > 12) or (day < 1 or day > 31):
        return False
    elif month == 2 and day > 28:
        if day == 29 and isLeapYear(year):
            return True
        else:
            return False
    elif month in [4, 6, 9, 11] and day > 30:
        return False
    else:
        return True
    
assert is_valid_date(1999, 12, 31) == True
assert is_valid_date(2000, 2, 29) == True
assert is_valid_date(2001, 2, 29) == False
assert is_valid_date(2029, 13, 1) == False
assert is_valid_date(1000000, 1, 1) == True
assert is_valid_date(2015, 4, 31) == False
assert is_valid_date(1970, 5, 99) == False
assert is_valid_date(1981, 0, 3) == False
assert is_valid_date(1666, 4, 0) == False

d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert is_valid_date(d.year, d.month, d.day) == True
    d += oneDay
