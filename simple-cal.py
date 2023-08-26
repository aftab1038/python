#welcome message
print("\nWelecome to Arthimatic Calculator\n")

#Variable
v1 = int(input("Enter a value: "))
op = input("Enter a operator: ")
v2 = int(input("Enter another value: "))

#Addition
if (op == "+"):
    print(v1,op,v2,"=",v1+v2)

#Subtraction
elif (op == "-"):
    print(v1,op,v2,"=",v1-v2)

#Mutiplication
elif (op == "*"):
    print(v1,op,v2,"=",v1*v2)

#Division
elif (op == "/"):
    print(v1,op,v2,"=",v1/v2)

#If wrong input enter.
else:
    print("Incorrect input, Do it again!")