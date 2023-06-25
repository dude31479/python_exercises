def tribonacci(num):
    tri = 0
    bo = 1
    nacci = 2
    tribonacci = []
    while nacci < num:
        tribonacci.append(str(tri))
        tribonacci.append(str(bo))
        tribonacci.append(str(nacci))
        tri += bo + nacci
        bo += tri + nacci
        nacci += tri + bo
    return " ".join(tribonacci)

print(tribonacci(1000))