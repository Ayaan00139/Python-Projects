# for _ in range(3):
#     print("#")

def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
    # for _ in range(height):
    #     print("#")
    #or 
    print("# \n"*height, end="")

def print_row(width):
    print("?"*width,end="Square-> \n\n")

def print_square(size):
    for i in range(size): #for each row in square
        for j in range(size):#for each brick in row
            print("#", end="")# Print Brick
        print("")#goes to new line after every row 
    #or---------
    for i in range(size):
        print("#"*size, end="\n")

main()