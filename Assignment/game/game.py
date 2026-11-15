import random
import sys

while True:
    try:
        x=int(input("Level: "))
        if x==1:
            number=1
            break
        number=random.choice(range(1,x))
        assert x>0
    except (AssertionError,ValueError):
        pass
    else:
        break

while True:
    try:
        y=int(input("Guess: "))
        assert y>0
        if number == y:
            print("Just right!")
            sys.exit()
        if number>y:
            print("Too small!")
            raise ValueError
        if number<y:
            print("Too Large!")
            raise ValueError

    except (AssertionError,ValueError):
        pass
    else:
        break

