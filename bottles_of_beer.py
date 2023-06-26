def bottles_of_beer():
    bottles = 99
    while bottles > 0:
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall,")
            print(f"{bottles} bottle of beer,")
            print("Take it down,")
            print("Pass it around,")
            print("No more bottles of beer on the wall!")
            bottles -= 1
        else:
            print(f"{bottles} bottles of beer on the wall,")
            print(f"{bottles} bottles of beer;")
            print("Take one down,")
            print("Pass it around,")
            bottles -= 1
            print(f"{bottles} bottles of beer on the wall.\n")

bottles_of_beer()
