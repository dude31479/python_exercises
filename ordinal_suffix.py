def ordinal_suffix(num):
    num = str(num)
    # Always check the most specific possibility first.
    if num[-2:] == '13' or num[-2:] == '11' or num[-2:] == '12':
        return num + "th"
    elif num[-1] == '3':
        return num + "rd"
    elif num[-1] == '2':
        return num + "nd"
    elif num[-1] == '1':
        return num + "st"
    else:
        return num + "th"
    
assert ordinal_suffix(0) == "0th"
assert ordinal_suffix(1) == "1st"
assert ordinal_suffix(2) == "2nd"
assert ordinal_suffix(3) == "3rd"
assert ordinal_suffix(4) == "4th"
assert ordinal_suffix(10) == "10th"
assert ordinal_suffix(11) == "11th"
assert ordinal_suffix(12) == "12th"
assert ordinal_suffix(13) == "13th"
assert ordinal_suffix(14) == "14th"
assert ordinal_suffix(101) == "101st"
assert ordinal_suffix(113) == "113th"
assert ordinal_suffix(11113) == "11113th"