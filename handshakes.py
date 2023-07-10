def printHandshakes(a_list):
    shaken = []
    num = 0
    for x in a_list:
        for y in a_list:
            if x != y:
                if(x, y) not in shaken or (y,x) not in shaken:
                    num += 1
                    print(f"{x} shakes hands with {y}")
                    shaken.append((x, y))
                    shaken.append((y, x))
    print()
    return num

assert printHandshakes(['Alice','Bob']) == 1
assert printHandshakes(['Alice','Bob', 'Carol']) == 3
assert printHandshakes(['Alice','Bob', 'Carol', 'David']) == 6
