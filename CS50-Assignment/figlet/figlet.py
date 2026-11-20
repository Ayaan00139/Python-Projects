import pyfiglet
import sys
import random
fonts=pyfiglet.FigletFont.getFonts()

if len(sys.argv)==1:
    x=input("Input: ").strip()
    font=random.choice(fonts)
    print(pyfiglet.figlet_format(x,font))
    sys.exit()

if len(sys.argv)!=3:
    sys.exit("Invalid Usage")
if sys.argv[1] not in ["-f","--font"] or sys.argv[2] not in fonts:
    sys.exit("Invalid Usage")

try:
    font=sys.argv[2]
    f=pyfiglet.figlet_format("sample",font)
except:
    sys.exit("Invalid Usage")

x=input("Input: ").strip()
print(f"{pyfiglet.figlet_format(x,font)}")
