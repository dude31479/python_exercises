def commaFromat(num):
    num = str(num)
    if '.' in num:
        fractionalPart = num[num.index('.'):]
        num = num[:num.index('.')]
    else:
        fractionalPart = ''

    triplet = ''
    commaNum = ''

    for i in range(len(num) - 1, -1, -1):
        triplet = num[i] + triplet
        if len(triplet) == 3:
            commaNum = triplet + ',' + commaNum
            triplet = ''
    if triplet != '':
        commaNum = triplet + ',' + commaNum
    return commaNum[:-1] + fractionalPart

print(commaFromat(4423445.345))
