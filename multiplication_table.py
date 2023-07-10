print("  | 1  2  3  4  5  6  7  8  9 10")
print("--+------------------------------")
for i in range(1, 11):
    if i < 10:
        print(f" {i}| ", end="")
    else:
        print(f"{i}|", end="")
    for j in range(1, 11):
        result = i * j
        if result < 10 and j == 1:
            print(f"{result} ", end="")
        elif result < 10:
            print(f" {result} ", end="")
        else:
            print(f"{result} ", end="")
    print()