def main():
    x= int(input("What's x? "))
    if is_Even(x):
        print("Even")
    else:
        print("odd")

def is_Even(x):
    return n%2==0
    # return n%2==0:True?False
    # return True if n % 2 ==0 else False 
    # Or if(x%2==1):\n return False\n else:\nreturn True

main()
