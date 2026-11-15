import csv

# ---------------------Write Files ---------------------------

# name = input("Whats Your Name? ")

# # file= open("names.txt","a") # "w" will overite every value so we use a as append
# # file.write(name+"\n")
# # file.close

# with open ("names.txt","a") as file:
#     file.write(name+"\n")


#---------------------Write Files With Csv-------------------

name=input("Whats your name?")
home=input("WHats your home")

with open ("names.csv","a") as file:
    writer=csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name.rstrip(),"home":home.rstrip()})


#--------------------Read Files---------------------------

# with open("names.txt","r") as file:
#     lines=file.readlines()

# for line in sorted(lines):
#     print("hello,",line.rstrip())#removes everything beside text 

# with open("names.txt","r") as file:
#     for line in sorted(file):
#         print("hello,",line.rstrip())


#Read Files With Csv with Multiple Info

# with open("names.csv") as file:
#     for line in sorted(file):
#         row=line.rstrip().title().split(",")
#         print(row[0]+" lives in "+row[1])

#--------------- Read With CSV--------------------

# students=[]
# with open("names.csv") as file:
#     reader=csv.DictReader(file) #will auto deal with cornor cases like 2 or 3 commas which stops us to split data
#     for row in reader:
#         students.append({"name":row["name"],"house":row["home"]})
#     # for line in (file):
#     #     name, house=line.rstrip().title().split(",")
#     #     student={"name":name, "house":house}
#     #     students.append(student)

# for student in sorted(students,key=lambda student:student["name"]): #equivalent to get_name
#     print(f'{student["name"]} is in {student["house"]}')

