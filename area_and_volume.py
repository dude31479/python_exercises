def get_area(length, width):
    return length * width

def get_perimeter(length, width):
    return (length + width) * 2

def get_volume(length, width, height):
    return length * width * height

def get_surface_area(length, width, height):
    return ((length * width) + (length * height) + (width * height)) * 2

assert get_area(10, 10) == 100
assert get_area(0, 9999) == 0
assert get_area(5, 8) == 40
assert get_perimeter(10, 10) == 40
assert get_perimeter(0, 9999) == 19998
assert get_perimeter(5, 8) == 26
assert get_volume(5, 8, 10) == 400
assert get_volume(10, 10, 10) == 1000
assert get_volume(9999, 0, 9999) == 0
assert get_surface_area(10, 10, 10) == 600
assert get_surface_area(9999, 0, 9999) == 199960002
assert get_surface_area(5, 8, 10) == 340

def calculation():
    while True:
        calc = input("""Please select from the following options:
            1. Calculate Area
            2. Calculate Perimeter
            3. Calculate Volume
            4. Calculate Surface Area
        > """)
        if calc in list('1234'):
            length = int(input("Please enter the length: "))
            width = int(input("Please enter the width: "))
            if calc == '1':
                area = get_area(length, width)
                return area
            elif calc == '2':
                perimeter = get_perimeter(length, width)
                return perimeter
            elif calc == '3' or calc == '4':
                height = int(input("Please enter the height: "))
                if calc == '3':
                    volume = get_volume(length, width, height)
                    return volume
                else:
                    surface_area = get_surface_area(length, width, height)
                    return surface_area
        else:
            input("Please input a valid selection!")

def main():
    result = calculation()
    print(result)

main()