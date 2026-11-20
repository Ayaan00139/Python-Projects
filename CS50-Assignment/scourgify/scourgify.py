import sys
import csv
flag=1


if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("")

try:
    with open(sys.argv[2],"w") as write:
        writer=csv.writer(write)
        writer.writerow(['first','last','house'])
        with open(sys.argv[1]) as read:
            reader=csv.reader(read)
            for name,house in reader:
                if flag==1:
                    flag=0
                else:
                    print(name,house)
                    last, first =name.strip('""').split(", ")
                    writer.writerow([first, last, house])
except:
    sys.exit(f"Could not read {sys.argv[1]}")
