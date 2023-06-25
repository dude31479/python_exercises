# Create a program that takes input in seconds and converts it 
# into a string like: 1h 25m 32s"""

def getHoursMinutesSeconds(totalSeconds):
    dhms = []
    days = totalSeconds // 86400
    hours = (totalSeconds - (days * 86400))// 3600
    mins = (totalSeconds - (days * 86400 + hours * 3600)) // 60
    secs = totalSeconds - (days * 86400 + hours * 3600 + mins * 60)
    if days:
        dhms.append(str(days) + "d")
    if hours:
        dhms.append(str(hours) + "h")
    if mins:
        dhms.append(str(mins) + "m")
    if not (days or hours or mins) or secs:
        dhms.append(str(secs) + "s")
    return " ".join(dhms)


assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '1d 1h 42s'
assert getHoursMinutesSeconds(0) == '0s'