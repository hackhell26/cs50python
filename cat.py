# Calling the function in a variable number of times
# Checking if "n" it is a positive number

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")