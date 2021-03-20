'''1. Take values of length and breadth of a rectangle from user and check if it is square or not'''

# le=int(input("Enter the value of length"))
# br=int(input("Enter the value of breadth"))
# if(le==br):
#     print("It is a square")
# else:
#     print("It is not a square")

'''2.  A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
     Ask user for quantity
     Suppose, one unit will cost 100.
     Judge and print total cost for user.'''

# purchase_quantity=int(input("Enter the cost of purchased quantity"))
# if(purchase_quantity>1000):
#     discount=(purchase_quantity*10)/100
#     total_cost= purchase_quantity-discount
#     print(f"Total Cost after 10% discount: {total_cost}")
# else:
#     total_cost=purchase_quantity
#     print(f"Total Cost:{total_cost}")


'''3. A company decided to give bonus of 5% to employee if his/her year of 	service is more than 5 years.
      Ask user for their salary and year of service and print the net bonus amount.'''

# yos=int(input("Enter years of service"))
# salary=int(input("Enter your salary amount"))
# if(yos>5):
#     bonus=(salary*5)/100
#     net_amount=salary+bonus
#     print(f"Your Net Bonus Amount:{net_amount}")
# else:
#     print("Sorry, No bonus this year")

'''4.A school has following rules for grading system:
	a. Below 25 - F
	b. 25 to 45 - E
	c. 45 to 50 - D
	d. 50 to 60 - C
	e. 60 to 80 - B
	f. Above 80 - A
	Ask user to enter marks and print the corresponding grade.'''

# marks=float(input("Enter your obtained marks percentage"))
# if(marks<25):
#     print("Your Grade is F")
# elif(marks>=25 and marks<45):
#     print("Your grade is E")
# elif(marks>=45 and marks<50):
#     print("Your Grade is D")
# elif(marks>=50 and marks<60):
#     print("Your grade is C")
# elif(marks>=60 and marks<80):
#     print("Your Grade is B")
# else:
#     print("Your grade is A")

'''5.Take two int values from user and print greatest among them.'''

first=int(input("Enter the first number: "))
second=int(input("Enter the first number: "))
if(first>second):
    print(f"First number {first} is greatest")
elif(second>first):
    print(f"Second number {second} is greatest")
else:
    print("Both numbers are equal")
