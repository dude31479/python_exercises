def printASCIITABLE():
    for i in range(32, 100):
        print(i, chr(i).rjust(3))
    for i in range(100, 127):
        print(i, chr(i).rjust(2))

printASCIITABLE()