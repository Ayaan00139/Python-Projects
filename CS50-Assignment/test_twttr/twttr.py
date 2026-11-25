import sys
def main():
    try:
        x=input("")
        float(x)
    except ValueError:
        pass
    else:
        raise AssertionError
    string=shorten(x)
    print(*string)


def shorten(x):
    value=""
    try:
        float(x)
    except ValueError:
        pass
    else:
        raise AssertionError
    temp=[]
    for i in x:
        if i.lower() in ["a","e","i","o","u"]:
            pass

        else:
            temp.append(i)
    for i in temp:
        value=f"{value}{i}"
    return value

if __name__ == "__main__":
    main()
