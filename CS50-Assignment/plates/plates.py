import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag=True
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False
    for c in s:
        if c.isdigit():
            if c=="0":
                flag=False
            elif not flag:
                return False
    flag=True
    return flag

main()
