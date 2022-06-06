# Re prompt to the user if it's input it's different to a integer
# And avoid to exit the program
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not a integer")
    else:
        break

print(f"x is {x}")