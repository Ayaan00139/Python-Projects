import re
name = input("What's Your Name? ").strip()

if matches :=re.search(r"^(.+), *(.+)$",name): # short for matches=re.search(r"^(.+), *(.+)$",name) \n if matches:
    name=matches.group(2)+" "+matches.group(1)

print(f"{name}")
