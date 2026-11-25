import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match:=re.search(r'^((?:[0-1]{1})?[0-9]{1}(?:\:[0-5]{1}[0-9]{1})? (?:[AMP]{2})) to ((?:[0-1]{1})?[0-9]{1}(?:\:[0-5]{1}[0-9]{1})? (?:[AMP]{2}))$',s):
            first=match.group(1)
            second=match.group(2)
            if "PM" in first:
                if "12" in first:
                    first=float(12.00)
                else:
                    first=first.replace("PM","").strip()
                    if ":" in str(first):
                        first=first.replace(":",".").strip()
                    first=float(first)+12

            else:
                if "12" in first:
                    first=float(00.00)
                else:
                    first=first.replace("AM","").strip()
                    if ":" in str(first):
                        first=first.replace(":",".").strip()
                    first=float(first)
            if "PM" in second:
                if "12" in second:
                    second=float(12.00)
                else:
                    second=second.replace("PM","").strip()
                    if ":" in str(second):
                        second=second.replace(":",".").strip()
                    second=float(second)+12
            else:
                if "12" in second:
                    second=float(00.00)
                else:
                    second=second.replace("AM","").strip()
                    if ":" in str(second):
                        second=second.replace(":",".").strip()
                    second=float(second)

            time=f"{first:05.2f} to {second:05.2f}"
            return time.replace(".",":")
    else:
        raise ValueError 
if __name__ == "__main__":
    main()
