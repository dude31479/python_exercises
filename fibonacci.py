def fibonacci(num):
    fibo = 0
    nacci = 1
    fibonacci = []
    while nacci < num:
        fibonacci.append(str(fibo))
        fibonacci.append(str(nacci))
        fibo += nacci
        nacci += fibo
    return " ".join(fibonacci)

print(fibonacci(300))