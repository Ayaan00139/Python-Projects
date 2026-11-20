def main():
    temp=input("")
    temp=convert(temp)
    print(temp)

def convert(temp):
    if ":)" in temp:
        temp=temp.replace(":)","🙂")
    if ":(" in temp:
        temp=temp.replace(":(","🙁")
    return temp

if(__name__=="__main__"):
    main()
