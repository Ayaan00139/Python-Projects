from attr import NOTHING


x=input("Input: ")

for i in x:
    if i.lower() in ["a","e","i","o","u"]:
        pass
    else:
        print(i,end="")
print()
