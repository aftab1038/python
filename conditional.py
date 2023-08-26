#conditional statement
#condi-oper         > < >= <= == !=
#if else
#elif
#nested if else


num = int(input("Enter a num: "))
print ("Num: ",num)

if (num > 0):
    print ("postive")
    if (num <= 10):
        print("in b/w 1-10")
    else:
        print("greater than 10 ")
    
elif (num == 0):
    print(" zero")
else:
    print ("negative")