#Interest Calculator
print("Interest Calculator")

#User input for Principal amount
principal = input("Principal Amount: ")

#Percentage Rate of interest
rate = input("Interest rate in percentage: ")

#Timne Period
time = input("Time period in year: ")

#Formula
interest = int(principal)*int(rate)*int(time)/100

#Print Interest
print("Interest: "+str(interest))
