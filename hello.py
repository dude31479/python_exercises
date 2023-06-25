# print("Hello, world!")
# name = input("What is your name?")
# print(f"Hello, {name}.")

# name = input("Hello, world!\nWhat is your name? ")
# print("Hello, {}.".format(name))

# def hello_world():
#     name = input("Hello world!\nWhat is your name? ")
#     return name

# def say_hello(name_func):
#     name = name_func()
#     return f"Hello, {name}."

# def main():
#     hello = say_hello(hello_world)
#     print(hello)
# main()

def get_name():
    name = input("Hello world!\nWhat is your name?")
    return name

def generate_greeting(name):
    return f"Hello, {name}."

def main():
    name = get_name()
    greeting = generate_greeting(name)
    print(greeting)

if __name__ == "__main__":
    main()