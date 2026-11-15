def main():
    x=get_int("What's x? ")
    print(f"x is {x}")

def get_int(x):
    while True:
        try:
            return int(input(x))
            # x=int(input("What's x "))
            # return x?
        except ValueError:
            pass


main()
