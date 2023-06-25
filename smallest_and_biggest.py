def get_smallest(numbers):
    if numbers:
        smallest = numbers[0]
        for number in numbers:
            if number < smallest:
                smallest = number
        return smallest
    return None


def get_biggest(numbers):
    if numbers:
        biggest = numbers[0]
        for number in numbers:
            if number > biggest:
                biggest = number
        return number
    return None

assert get_smallest([1, 2, 3]) == 1
assert get_smallest([3, 2, 1]) == 1
assert get_smallest([28, 25, 42, 2, 28])
assert get_smallest([1]) == 1
assert get_smallest([]) == None