import re
import sys

def main():
    print(value(input(": ").strip()))

def value(greeting):
    if not re.search(r"^(\w+),? ?(?:[a-zA-Z])?",greeting,re.IGNORECASE):
        sys.exit(ValueError)
    greeting=re.search(r"^(\w+),? ?(?:[a-zA-Z])?",greeting,re.IGNORECASE)
    greeting=greeting.group(1)
    if greeting.lower()=="hello":
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


