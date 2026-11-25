import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        if not re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip):
            return False
        response=re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip)
        if int(response.group(1))>255 or int(response.group(2))>255 or int(response.group(3))>255 or int(response.group(4))>255:
            return False
        if int(response.group(1))==0 or int(response.group(4))==0:
            return False
        return True
    except:
        return False
if __name__ == "__main__":
    main()
