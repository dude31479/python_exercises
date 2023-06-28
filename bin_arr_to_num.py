"""Takes in an array of the digits in a binary number and converts to an integer."""

def binary_array_to_number(arr):
    x = 1
    result = 0
    for i in range(1, len(arr)):
        x = x * 2
    for i in arr:
        if i == 1:
            result += i * x
        x = x / 2
    return int(result)