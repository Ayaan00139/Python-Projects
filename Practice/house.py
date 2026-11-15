name= input("What's Your Name")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# -------------- Using MATCH----------------------#


# match name:
#     case "Harry":
#         print("Grinffindor")
#     case "Hermione":
#         print("Grinffindor")
#     case "Ron":
#         print("Grinffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

#------------------------Shorten-------------------#

match name:
    case "Harry" | "Hermione" |"Ron":
        print("Grinffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

        