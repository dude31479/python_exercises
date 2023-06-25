"""Takes a number and for every integer up to the target number,
prints Fizz if the integer is divisible by 3, Buzz if divisible
by 5 and FizzBuzz if divisible by both 3 and 5. Otherwise, prints the
integer. Only accepts possitive integers."""

def fizzbuzz():
    upTo = input("Enter a number: ")
    if upTo.isdecimal() and int(upTo) > 0:
        for i in range(1, int(upTo) + 1):
            if i % 15 == 0:
                print("FizzBuzz ", end="")
            elif i % 5 == 0:
                print("Buzz ", end="")
            elif i % 3 == 0:
                print("Fizz ", end="")
            else:
                print(f"{i} ", end="")
    else:
        print("Invalid input!")

fizzbuzz()
