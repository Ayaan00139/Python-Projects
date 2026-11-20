import csv
import tabulate
import sys
flag=1
header=[]
table=[]

if len(sys.argv)!=2:
    sys.exit("")
if sys.argv[1].strip() not in ["regular.csv","sicilian.csv"]:
    sys.exit("")

with open(sys.argv[1]) as file:
    for line in file:
        temp1,temp2,temp3=line.strip().split(",")
        if flag==1:
            header=[temp1,temp2,temp3]
            flag=0
        else:
            table.append([temp1,temp2,temp3])

print(tabulate.tabulate(table,headers=header,tablefmt="grid"))
