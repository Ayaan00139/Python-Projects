grocery=[]
i=0
while True:
    try:
        x=input("")
        grocery[i]["name"]=x
        i=i+1
    except EOFError:
        break

# for i in range(len(grocery)):
#     counts[f"count{i}"] = 0
#     if grocery[i] in grocery:
#         counts[f"count{i}"] +=1

print(*grocery, sep="\n")


