import re

greetings=input(": ").strip().lower()

greeting=re.search(r"^(\w+),? ?(?:[a-zA-Z])?",greetings,re.IGNORECASE)

greeting=greeting.group(1)

if greeting=="hello":
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
