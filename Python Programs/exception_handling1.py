''' Exception Handling'''
# It is used in ML Data science,Automatic server program.

#Note
'''In terminal(Linux) to stop executing program is stopped by two keyboard shortcuts 
1. ctrl + c
2. ctrl + z (FORCEFUL)
'''

"Try and Except"
a=1
b=0

try:
    print(a/b)
# except: TypeError
#     print("Error")
except ZeroDivisionError:
    print("Error")