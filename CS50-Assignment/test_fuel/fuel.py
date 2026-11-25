import sys

def main():
    z=convert(input("Fraction: "))
    print(gauge(z))
def convert(fraction):
    x,y=fraction.split("/")
    x,y=int(x),int(y)
    if int(y)==0:
        raise ZeroDivisionError
    if x<0 or x>y:
        raise ValueError

    x=float(x)
    y=float(y)
    z=int(round((x/y)*100))
    return z

def gauge(z):
    if z<=1:
        return ("E")
    elif z>=95:
        return ("F")
    else:
        return (f"{z:.0f}%")


if __name__ == "__main__":
    main()
