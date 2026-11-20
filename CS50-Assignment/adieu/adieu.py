import inflect

f=inflect.engine()

names=[]
names2=[]
while True:
    try:
        x=input("Name:")
        names.append(x)
    except EOFError:
        print()
        break

for i in range (len(names)):
    names2.append(names[i])
    print(f"Adieu, adieu, to {f.join(names2)}")

