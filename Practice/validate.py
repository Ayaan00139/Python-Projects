import re
email = input("Whats Your Email? ").strip().lower()
#-------------------BEFORE---------------------
# username, domain=email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

# --------------------- AFTER--------------------
#\w-> word character means -> [a-zA-Z0-9_]
if re.search(r"^[\w|\.]+@(\w+\.)?\w+\.edu$",email, re.IGNORECASE): #we use this raw with a "r" string so 
    print("Valid")         #that python does not expect another character 
else:                      # after the "\" like a "\n" or something
    print("InValid")
