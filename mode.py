def mode(numbers):
    if numbers:
        freq = {}
        for number in numbers:
            if number in freq.keys():
                freq[number] += 1
            else:
                freq[number] = 1
        mode_val = 0
        for key, val in freq.items():
            if val > mode_val:
                mode_key , mode_val = key, val
        return mode_key
    return None

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4