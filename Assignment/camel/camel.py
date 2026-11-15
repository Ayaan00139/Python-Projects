
camel=input("camelCase:").strip()

for i in camel:
    if i == i.upper():
        print("_",end="")
    print(i.lower(),end="")
print()


