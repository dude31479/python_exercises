def getcostOfCoffee(coffees, price):
    total = 0
    for coffee in range(coffees + 1):
        if coffee % 9 == 0:
            continue
        else:
            total += price
    return total



assert getcostOfCoffee(7, 2.50) == 17.50
assert getcostOfCoffee(8, 2.50) == 20
assert getcostOfCoffee(9, 2.50) == 20
assert getcostOfCoffee(10, 2.50) == 22.50

for i in range(1, 4):
    assert getcostOfCoffee(0, i) == 0
    assert getcostOfCoffee(8, i) == 8 * i
    assert getcostOfCoffee(9, i) == 8 * i
    assert getcostOfCoffee(18, i) == 16 * i
    assert getcostOfCoffee(19, i) == 17 * i
    assert getcostOfCoffee(30, i) == 27 * i