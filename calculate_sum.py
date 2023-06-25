def calculate_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def calculate_product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

print(calculate_sum([1, 2, 3, 4, 5, 6]))
print(calculate_product([4, 5, 6]))