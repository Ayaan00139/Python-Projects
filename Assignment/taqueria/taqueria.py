import sys
price={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total=0
while True:
    try:
        x= input("Item: ").title()
        assert x in price
        if type(x)!=str:
            raise ValueError
    except (ValueError,AssertionError):
        pass
    except EOFError:
        print()
        sys.exit()
    else:
        z=float(price[x])
        total+=z
        print(f"Total: ${total:.2f}")

