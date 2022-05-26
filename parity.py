def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# Just returning the question withou asking "if" or "else"
def is_even(n):
    return n % 2 == 0


main()