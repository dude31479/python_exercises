def tower(num):
    stars = 1
    spaces = num - 1
    for i in range(num):
        print(" " * spaces, "*" * stars, " " * spaces)
        stars += 2
        spaces -= 1

tower(5)