def main():
    number = get_number()
    meow(number)

def get_number():
    num = int(input("What's n? "))
    while True:
        if num > 0:
            return num

def meow(n):
    for _ in range(n):
        print("meow")

main()