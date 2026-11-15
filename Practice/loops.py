""""
i = 3

while i!=0:
    print("1 meow")
    i-=1


#--------------------------------------------------------------

for i in [0,1,2]:
    print("2 meow")


#--------short in for-------------
for _ in range(3): # Name the variable "_" so cause its a global name which specifies that we care about this variable this and is only for the loop
    print("3 meow")

print("4 meow \n" *3 ,end="" )



while True: #will run inf
    n=int(input("What's n? "))
    if(n>0):
        break

for _ in range(n):
    print("meow",)



def main():
    number=getNum()
    meow(number)

def getNum():
    while True: #will run inf
        n=int(input("What's n? "))
        if(n>0):
            return n

def meow(x):
    for y in range(x):
        print("meow",y+1)

main()


students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i+1, students [i])

"""

x= range(3)

print(x[0])