def commaFromat(num):
    num = str(num)
    if '.' in num: # If the number is a decimal
        fractionalPart = num[num.index('.'):] # Save the part after and incl the decimal
        num = num[:num.index('.')] # Change num to everything up to but not the decimal
    else:
        fractionalPart = '' # Otherwise, do nothing

    triplet = '' # Create a temp variable to store digits
    commaNum = '' # And a second variable to format triplets with commas

    for i in range(len(num) - 1, -1, -1): # Iterate backwards through the number string
        triplet = num[i] + triplet # Add the next digit to the left, to the left of triplet 
        if len(triplet) == 3: # ...until triplet has 3 digits
            commaNum = triplet + ',' + commaNum # Concatenate triplet with a comma + commaNum
            triplet = '' # Result the temp triplet variable to store the next 3 digits
    if triplet != '': # If there are two or one digits left in num
        commaNum = triplet + ',' + commaNum # Add them to the start of commaNum
    return commaNum[:-1] + fractionalPart # Get rid of trailing comma and tack on the decimal

print(commaFromat(4423445.345))
