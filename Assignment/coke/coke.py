total=0
print(f"Amount Due: {50-total}",end="\n")
while total<50:
    x=int(input("Insert Coin: "))
    if x in [25,5,10]:
        total=total+x
    print(f"Amount Due: {abs(50-total)}",end="\n")

print(f"Change Owed: {total-50}",end="\n")
