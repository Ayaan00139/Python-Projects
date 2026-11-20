import sys
def main():
    try:
        x=input("")
        float(x)
    except ValueError:
        pass
    else:
        sys.exit("")
    string=shorten(x)
    print(*string)


def shorten(x):
    try:
        float(x)
    except ValueError:
        pass
    else:
        sys.exit("")
    temp=[]
    for i in x:
        if i.lower() in ["a","e","i","o","u"]:
            pass
        else:
            temp.append(i)
    return temp

if __name__ == "__main__":
    main()
