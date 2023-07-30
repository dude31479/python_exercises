import random

print("I am thinking of a number between 1 and 20.")
num = random.randint(1, 20)
for guesses in range(7):
    print("Take a guess")
    guess = int(input())

    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        break

if guess == num:
    print("Good job! You guessed the number in {} attempts!".format(guesses))
else:
    print("Nope. The number I was thinking of was {}.".format(num))