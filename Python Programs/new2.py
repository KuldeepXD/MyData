#Day 2 - 17/2/2021

'''Conditions'''
#IF is a keyword to start condition statement

# a= int(input("Enter your number"))


# if a%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")

'''2 numbers'''

# a= int(input("Enter your number"))
# b= int(input("Enter your number"))
#Nested IF ELSE
# if a%2==0:
#     print("A Number is even")
#     if b%2==0:
#         print("B Number is Even")
# else:
#      print("Print A is odd
#     ")
# if a%2==0 and b%2==0:
#     print("A and B are Even")
# elif a%2==0 and b%2!=0:
#     print("A is even and B is odd")
# elif

#use insert key if the  cursor is out of the loop

# '''3 numbers'''
# a= int(input("Enter number a"))
# b= int(input("Enter number b"))
# c= int(input("Enter number c"))

# if a%2==0 and b%2==0 and c%2==0:
#     print("a,b,c are even numbers")
# elif a%2==0 and b%2==0 and c%2!=0:
#     print("a,b are even, c is odd")
# elif a%2==0 and b%2!=0 and c%2==0:
#     print("a,c are even, b is odd")
# elif a%2==0 and b%2!=0 and c%2!=0:
#     print("a is even, b and c are odd")
# elif a%2!=0 and b%2==0 and c%2==0:
#     print("a is odd, b and c are even")
# elif a%2!=0 and b%2!=0 and c%2==0:
#     print("a,b are odd, c is even")
# elif a%2!=0 and b%2==0 and c%2!=0:
#     print("a,c are odd, b is even")
# elif a%2!=0 and b%2!=0 and c%2!=0:
#     print("a,b,c are odd numbers")


'''same program in nested if else - Homework'''
'''3 numbers'''
a= int(input("Enter number a"))
b= int(input("Enter number b"))
c= int(input("Enter number c"))

if a%2==0:
    print("A is even")
    if b%2==0:
        print("B is even")
        if c%2==0:
            print("C is even")
        else:
            print("C is odd")
    else:
        print("B is odd")
        if c%2==0:
            print("C is even")
        else:
            print("C is odd")
else:
    print("A is odd")
    if b%2==0:
        print("B is even")
        if c%2==0:
            print("C is even")
        else:
            print("C is odd")
    else:
        print("B is odd")
        if c%2==0:
            print("C is even")
        else:
            print("C is odd")                     
                       