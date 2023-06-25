def is_odd(num):
    # Checks if odd
    return num % 2 == 1

def is_even(num):
    # Checks if even
    return num % 2 == 0

# Assertion statements will stop program if any evaluate to false.

# This statement evaluates 
# to True if is_odd(42) == False:
assert is_odd(42) == False

# etc...
assert is_odd(9999) == True
assert is_odd(-10) == False
assert is_odd(-11) == True
assert is_odd(3.1415) == False
assert is_even(42) == True
assert is_even(9999) == False
assert is_even(-10) == True
assert is_even(-11) == False
assert is_even(3.1415) == False