import sys
# yes                
try:
    if len(sys.argv)!=2:
        sys.exit()
    with open(sys.argv[1]) as file:
        for line in file:
            if line.include("#"):
                print(line)
except:
    sys.exit()
