def getChessSquareColor(a, b):
    if 0 <= a <= 7 and 0 <= b <= 7:
        if (a + b) % 2 == 0:
            return 'White'
        else:
            return 'Black'
    else:
        return 'That is not on the Chess board!'
    
print(getChessSquareColor(0, 1))