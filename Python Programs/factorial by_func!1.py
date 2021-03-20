'''FACTORIAL USING FUCTION for loop'''

a=int(input("Enter your number"))

def factorial(a):
    fact=1
    for i in range (1,a+1):
        fact=fact*i
    return fact

print(factorial(a))
