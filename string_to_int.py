def convertStrToInt(stringNum):
    isNegative = False
    x = 1
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
              '6':6, '7':7, '8':8, '9':9}
    if stringNum[0] == '-':
        isNegative = True
    if isNegative:
        x = -1
        stringNum = stringNum[1:]
    intNum = 0
    for i in stringNum:
        intNum = (intNum * 10) + digits[i]
    return intNum * x

for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i