# If user does not type any input, it will print just "hello, world"
def hello(to="world"):
    print("hello,", to)

hello()
name = input("What is your name? ")
hello(name)

