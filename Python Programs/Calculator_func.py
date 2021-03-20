a=int(input("Enter first number"))

b=int(input("Enter second number"))
v=int(input("Enter the type of arithematic operation:\n1.Addition\n2.Subtraction\n3.Multipication\n4.Division"))
def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def mult(x,y):
    print(x*y)

def div(x,y):
    print(x/y)

if(v==1):
    add(a,b)
elif(v==2):
   sub(a,b)
elif(v==3):
   mult(a,b)
elif(v==4):
    div(a,b)


