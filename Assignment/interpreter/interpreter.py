Expression=input("Expression: ")

try:
    x,y,z=Expression.split(" ")
    x=int(x)
    z=int(z)
except ValueError:
    print("Wrong Value")
else:
    if y=="+":
        print(float(x+z))
    elif y=="-":
        print(float(x-z))
    elif y=="*":
        print(float(x*z))
    elif y=="/" and z==0:
        raise ValueError ("With DIvision Z cant Be 0")
    elif y=="/":
        print(float(x/z))
