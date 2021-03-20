#######   5/03/2021    ######
'''Methods in List'''

# Find all the number not divisble by 5 and 7 from 1k to 5k
# list1=[]

# for i in range (1000,5000):
#     if(i%5!=0 and i%7!=0):
#         list1.append(i)
# # print(list1)
# print(list1.index(1018)) # for knowing the index location of item

# list1=[0,5,77,8,8,7,5,55,1,1,152]

# print(sorted(list1)) #sorting elements

'''Concatenation'''#*Adidition/Joddna/join

# list2=[1,3,4,5]
# list3=[4,5,6]

# list3=list2+list3
# print(list3)

#multiply lists
# list3=[4,5,6]*5
# print(list3)

# #Counting length of list/no of elements
# print(len(list3))

#Similarly we can use max and min commands to know highest and lowest element.

#now to know sum of elements

# print(sum(list3))

### FIND SUM OF THIS LIST WITHOUT USING FUNCTION

# list1=[]

# for i in range (1000,5000):
#     if(i%5!=0 and i%7!=0):
#         list1.append(i)
# # # print(list1)

# a=0 #for intitialisation
# for i in list1:
#     a+=i

# print(a)

# list1=[1,1,1,5,55,88]
# print(any(list1))
# print(all(list1))

# print(list1.count('1'))

# list2=list1.copy
# print(list2)

#to check if something is present in list

list1=[1,1,1,5,55,88]
a=1

while a in list1:
    a=input("Enter the number")
    print("Number is present:")
    
print("Number is not present")