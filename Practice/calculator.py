# def main():
#     x=int(input("What's x? "))
#     y=int(input("What's y? "))
#     z=add(x,y)
#     print(z)


# def add(x,y):
#     z=x+y;
#     return z

# main()

def main():
    x=int(input("What's x? "))
    print("Square Of X Is:", square(x))


def square(x):
    return x*x # or return pow(x,2)
if (__name__=="__main__"):
    main()