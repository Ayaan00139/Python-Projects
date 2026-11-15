name=input("Whats Your Name? ").strip().title()

name=name.strip() # Removes Spaces In A String

name=name.capitalize() #Capitalize Only First Letter Of A String 

name=name.title() #Capitalize First Letter Of Every Word Of A String

print("hello, ",end="??")
print(name)

print("hello, ", name, sep="?")

#For Short->

########## name=input("Whats Your Name? ").strip().title() do everything here.

#Split User Name In first and last Name

first, last=name.split(" ")

print(f"hello, {first}")


