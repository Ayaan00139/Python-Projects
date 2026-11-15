import random
import sys
count = 0
error=0
question=0


def main():
    level = get_level()
    all(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            assert level > 0 and level <= 3
        except (ValueError, AssertionError):
            pass
        else:
            return level


def generate_integer(level):
    if level == 1:
        return random.choice(range(0, 10))
    elif level == 2:
        return random.choice(range(10, 100))
    elif level == 3:
        return random.choice(range(100, 1000))


def all(level):
    global count
    global error
    global question
    question+=1
    error=0
    x=generate_integer(level)
    y=generate_integer(level)
    while True:
        try:
            if level not in [1,2,3]:
                sys.exit("Invalid Level")

            if question>10:
                print("Score:", count)
                sys.exit()

            print(f"{x} + {y} = ", end="")
            z = int(input(""))

            if (x+y) != z:
                error+=1
                print("EEE")
                raise ValueError

        except ValueError:
            if error==3:
                print(f"{x} + {y} = {x+y}")
                all(level)
            pass
        else:
            count += 1
            all(level)


if __name__ == "__main__":
    main()
