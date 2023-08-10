def uppercase(text):
    res = ''
    for i in text:
        if i.isalpha() and i.lower() == i:
            i = chr(ord(i) - 32)
        res += i
    return res


assert uppercase('Hello') == 'HELLO'
assert uppercase('hello') == 'HELLO'
assert uppercase('HELLO') == 'HELLO'
assert uppercase('Hello, world!') == 'HELLO, WORLD!'
assert uppercase('goodbye 123!') == 'GOODBYE 123!'
assert uppercase('12345') == '12345'
assert uppercase('') == ''