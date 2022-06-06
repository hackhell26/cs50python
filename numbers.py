try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not a integer")
# else statement to handle the NameError: "name x is not defined"
else:
    print(f"x is {x}")
