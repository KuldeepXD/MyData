#04/03/2021
# Next level from Functions

'DATA STRUCTURES'

#1. Built in Data Structure {List,tuple,dict,sets}
#2. User defined DS {queue(line system),tree, hash,linked link, slack}

'''Array is a collection of same type data elements.'''

'''1. List'''

# We store heterogenous element in list.
# We can add,delete,update i.e. CRUD(Create, Remove, Update, Delete)
# Kabhi bhi list naam ka variable nahi le skte***

# a=[1,2,3]
# print(type(a))

#O/P= <class 'list'>
#SLicing and Accessing

# list2=['abc','bcd','cde']
# print(list2[2]) 
#here[2] indicates the index value which starts from 0, therefore element cde is printed because index value is 2.

list2=['abc','bcd','cde',['def','efg','hij']]
print(list2[3][0]) # DOUBT****

#slicing
# print(list2[2:]) # means index value 2 ke baad wale sare elements (including 2)

# print(list2[1:2]) # matlab index value 1 aur 2 ke beech ka element i.e bcd becuse index value 1 included

print(list2[::2]) # it means 2 2 ke gap ke baad to first element abc include hoga uske baad cde 
# ****Doubt- why efg is not included

# print(list2[1::3]) # only bcd because in between index gap 1 and 3 (not present) bcd is the only element

#list mein append,insert,pop,remove,update____* use kiye jaate hai.
'Append'

# list1=[]
# for i in range(0,2):
#     name=input("Enter Name")
#     list1.append(name)
# print(list1)
# ''' insert'''****Doubt
# list1=['tiwari','iot']

# list1.insert(1,list1) # isme index value as a parameter pass kia jata hai to us value pe insert hojati hai value

# print(list1)

# list1.pop(0)
# #list1.remove(1)

# print(list1)

# #### Square numbers list from 1 to 10

# list2= [x**2 for x in range(1,11)] # 11 because range takes one less value 
# print(list2)

#  Cube of numbers 1 to 10

# list3= [x**3 for x in range(1,11)]
# print("Cubes of the numbers is:",list3)

# ### Make a list of even and odd number from 0 to 100 
# even=[] #Blank list li hai
# odd=[]

# num=[x for x in range(1,100)]
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Odd Numbers:", odd)
# # agar lists me space lana hai to
# print("    ")

# print("Even Numbers:", even)

