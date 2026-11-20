month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
month1 = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


import re

while True:
    try:
        x=input("Date: ").strip()
        if re.search(r"^[\w]+ (1[0-2]|0?[1-9]), [0-9]{4}$",x):
            break
        elif re.search(r"^(1[0-2]|0?[1-9])/(3[0-1]|[1-2][0-9]|0?[1-9])/[0-9]{4}",x):
            break
        else:
            raise ValueError

    except ValueError:
        pass
    else:
        break

if re.search(r"^[\w]+ [0-9]{1,2}, [0-9]{4}$",x):
    response=re.search(r"^([\w]+) ([0-9]{1,2}), ([0-9]{4})$",x)
    print(f"{response.group(3).zfill(2)}-{str(month1[response.group(1).title()]).zfill(2)}-{response.group(2).zfill(2)}")
else:
    response=re.search(r"^([0-9]{1,2})/([0-9]{1,2})/([0-9]{4})",x)
    print(f"{response.group(3).zfill(2)}-{response.group(1).zfill(2)}-{response.group(2).zfill(2)}")

