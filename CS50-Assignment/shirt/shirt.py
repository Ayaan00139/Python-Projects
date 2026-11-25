from PIL import Image
from PIL import ImageOps
import sys
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
last=sys.argv[1].split(".")[-1]
if last.strip() not in ["jpg","png","jpeg"]:
    sys.exit("Invalid Input")
last2=sys.argv[2].split(".")[-1]
if last.strip() not in ["jpg","png","jpeg"]:
    sys.exit("Invalid Input")
if last2!=last:
    sys.exit("Input and output have different extensions")

try:
    shirt=Image.open("shirt.png")
    size=shirt.size
    input=Image.open(sys.argv[1])
    new=ImageOps.fit(input,size)
    new.paste(shirt,shirt)
    new.save(sys.argv[2])

except:
    sys.exit("Input Doesnt Exist")

