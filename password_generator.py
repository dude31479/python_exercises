import random

LETTERS = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
LOWER = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".lower().split()
CHARACTERS = "~ ! @ # $ % ^ & * ( ) _ +".split()
NUMBERS = "1 2 3 4 5 6 7 8 9 0".split()
ALL_CHARS = [LETTERS, CHARACTERS, NUMBERS, LOWER]


def generatePassword(number_of_characters):
    random.shuffle(LETTERS)
    random.shuffle(NUMBERS)
    random.shuffle(CHARACTERS)
    raw_password = [random.choice(LETTERS), random.choice(NUMBERS), random.choice(CHARACTERS)]
    if number_of_characters > 12:
        for i in range(number_of_characters - 12):
            raw_password.append(random.choice(ALL_CHARS[i % 4]))
    for i in range(9):
            raw_password.append(random.choice(ALL_CHARS[i % 4]))
    random.shuffle(raw_password)
    return "".join(raw_password)


pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasSpecial = False
hasNumber = False
for character in pw:
    if character in LOWER:
        hasLowercase = True
    if character in LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in CHARACTERS:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial

    
