print("Select among the following Calculation Operation:")
print("1. Addition Operation")
print("2. Subtraction Operation")
print("3. Division Operation")
print("4. Multiplication Operation")


userSelection=int(input("Enter your choice:"))
first=int(input("Enter 1st operand: "))
second=int(input("Enter 2nd operand: "))

if(userSelection==1):
    result=first+second
    print("addition of {:d} and {:d} is {:d}" .format(first,second,result))
    
if(userSelection==2):
    result=first-second
    print("subtraction of {:d} and {:d} is {:d}" .format(first,second,result))

if(userSelection==3):
    if(second==0):
        print("divisor can't be zero, please try again")
    else:
        result=first/second
        print("division of {:d} and {:d} is {:d}" .format(first,second,result))

if(userSelection==4):
    result=first*second
    print("multiplication of {:d} and {:d} is {:d}" .format(first,second,result))
