import re
import sys
import inflect
from datetime import date


def main():
    birth=input("Date Of Birth: ")
    diff=minutes(birth)
    print(f"{diff}")

def minutes(birth):
    if not re.search(r'^[0-9]{4}-(0?[1-9]|1[0-2])-(0?[1-9]|[1-2][0-9]|3[0-1])$',birth):
        sys.exit(ValueError)
    p = inflect.engine()
    year,month,day=birth.split("-")
    birth=date(int(year),int(month),int(day))
    now=date.today()
    diff=abs(now-birth)
    diff=p.number_to_words(diff.days*24*60,andword="")
    diff=diff.capitalize()
    return f"{diff} minutes"

if __name__ == "__main__":
    main()
