import sys
count=0
try:
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip().startswith("#") :
                # print("NO")
                pass
            elif line.strip()=="":
                # print("NO")
                pass
            else:
                count+=1
except:
    sys.exit("File does not exist")

print(count)
