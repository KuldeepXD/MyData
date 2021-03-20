#####  08/03/2021  #####
#SETS

#sets are shown by curl brackets {}
#it sortes elements itself if reapeated elements are present only one is shown
#We can not access sets because it does not work on index values
#values are initially sorted by ASCII codes
#IT is used in Machine Learning in order to avoid duplication and repetition.

# a={1,2,3,3,5,8,9,8,0,7}
# print(a)
# # a.update([34,2]) #for adding multiple elements
# # set ke andr set is not allowed because it doesnot work in index values 
# #EG b={1,2,{3,4}} not allowed

# #add 
# a.add(7.5)
# #REMOVING HAS 3 METHODS
# a.remove(7.5)
# a.pop() #first element is removed or last
# a.discard()

# #remove vs discard(jo element nahi h)
# a.discard(10)
# print(a)

# a.remove(10)
# print(a)
# #Discard error nahi deta jabki remove error(Keyerror) deta hai
# #Methods which can be used are Length,max,min,all, any ,sorted( ye wala apne aap sort krdega ascending value me)

# #SETS
# #Union of set
# b={1,2,3,4}
# c={4,5,6,7}

# print(b.union(c))

# #Similarly intersection
# print(b.intersection(b))


#now set B-C
# print(b.difference(c))
# #Symmetric
# print(b.symmetric_difference(c))
# print(b.symmetric_difference_update(c))
# print(b.isdisjoint(c)) #/kya ye joint ho skte hai ya nahi
# print(c.issubset(b)) #kya ye subset hai ya nahi
# print(b.issuperset(c))
#Similarly membership commands a in,  b in are used.

#It is used in development time

# #Booloean
# a=bool(1)
# print(a)
# #O/P true
# a=bool()
#O/P false

#Dictionary (Dict)

#IT works with key and values, every key has specific value

# a={"1":"b", "2":"d"}

# print(type(a))

#Comprehension
#EK hi line me
# a={x:x**2 for x in range (1,10)}
# print(a)
# b={1:"abc",'abc':[1,2,3]}
# print(b)
# c=dict(([1,2],[3,4],[5,6])) #isko aise bhi likh skte hai
# print(c)
# d=dict(([a,2],[b,4],[c,6])) #isko aise bhi likh skte hai
# print(d)

# e={1:2,2:3,1:4,2:5}
# print(e)
#only latest updated value will be printed
# d[1]='abc'
# d[2]='bcd'
# d[3]='efg'
# d[4]='ghi'
# print(d)
# print(d[5]) #blank ajegi /value not present examples
# print(d.get(6) # none error dega
# print(d.keys()) 
# print(d.values())