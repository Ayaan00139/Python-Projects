import sys 

words=sys.argv

# for word in words:
#     print(word)
#Check For Error
if(len(sys.argv)<2):
    sys.exit("Too Few Arguments")

#Main Code
for word in words[1:]: #this can also be used as words=sys.argv[1:]
    print("Hello My Name Is", word.strip(" ").title())

