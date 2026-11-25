from validator_collection import checkers

email=input("What's your email address? ")

email=checkers.is_email(email)

if email==True:
    print("Valid")
else:
    print("Invalid")
