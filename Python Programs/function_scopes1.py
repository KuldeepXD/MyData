'''02/03/2021'''
#using local scope
#using global variable

'''local and global example'''
# a=1
# b=5

# def add(a,b):
#     c=1
#     d=a+b+c
#     return d

# print(add(a,b))

# '''Global Scope'''
a=int(input("Enter first number"))
b=int(input("Enter second number"))

y=1 #here y is a Global scope or global variable i.e defined outside function

def add(a,b):
    d=a+b+y
    return d

print(add(a,b))
''''Homework Factorial Number by function'''
