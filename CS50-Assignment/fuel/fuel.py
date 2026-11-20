import sys
while True:
    x=input("Fraction: ")
    try:
        x,y=x.split("/")
        x=int(x)
        y=int(y)
        assert y!=0
        assert x>=0
        assert x<=y
    except (ValueError, AssertionError):
        pass
    else:
        break
x=float(x)
y=float(y)
z=int(round((x/y)*100))
if z<=1:
    print("E")
elif z>=95:
    print("F")
else:
    print(f"{z:.0f}%")


