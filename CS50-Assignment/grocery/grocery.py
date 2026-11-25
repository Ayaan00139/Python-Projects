grocery=[]

all=[]
i=0
while True:
    flag=False
    try:
        item={}
        x=input("").lower().strip()
        for i in range(len(grocery)):
            if x in grocery[i]["name"]:
                grocery[i]["count"]+=1
                flag=True
                break
        if flag==True:
            pass
        else:
            item["name"]=x
            item["count"]=1
            grocery.append(item)

    except EOFError:
        break

for i in range(len(grocery)):
    temp=[]
    temp=[grocery[i]["name"].upper(),grocery[i]["count"]]
    all.append(temp)

all=sorted(all)

for i in all:
    print(f"{i[1]} {i[0].upper()}")


