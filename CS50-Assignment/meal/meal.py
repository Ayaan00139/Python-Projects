def main():
    time=input("Enter The Time In 24 Hour Format Seprated By a ':' ")
    time=convert(time)

    if 7.0<=time<=8.0:
        print("breakfast time",end="")

    elif 12.0<=time<=13.0:
        print("lunch time",end="")

    elif 18.0<=time<=19.0:
        print("dinner time",end="")


def convert(time):
    hours,mins=time.split(":")
    hours=int(hours)
    mins=int(mins)
    if hours>24 or mins>60:
        raise ValueError ("Wrong Input")
    if mins in range(60):
        mins=mins/60
    return float(hours+mins)

if __name__ == "__main__":
    main()
