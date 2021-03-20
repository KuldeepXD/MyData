# def abc():
#     "hello"
'''02/03/2021'''

# print(abc.__doc__)
'''Return Fuction'''
#It is used when a value of a fucntion is required outside of the function hence print command use is not justified 
# a=67
# b=9

# def add(a,b):
#     c=a+b
#     return c

# print(add(a,b))
'''Keyword Argument'''
# **kwargs
'''Arbitrary arguments'''
# *args

'''Function for a mail'''
def mail (*name):
    for i in name:
        print(f"Hello {i}, this mail is for greetings")

mail("Kuldeep,Hemant") #ek hi line me output
mail("Kuldeep","Hemant") #alag alag line me output

''' function call krni hai'''
