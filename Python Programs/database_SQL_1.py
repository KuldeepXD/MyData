
''' MySQL'''
#Two types
#SQL and Non-SQL

#DATABASE IS MOST IMPORTANT
### apka main system hi local host hota hai eg. IP= 127.0.0.1 agr cloud pe hai database to uska IP dalna pdega

import mysql.connector
#Create connection

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root"
# )

# print(mydb)
# print("conncection is established")
# mycursor= mydb.cursor()
# mycursor.execute("create DATABASE Study")   #Single quotes b lba skte hai

#IF we forget database name
# mycursor.execute("show databases")
# for i in mycursor:
#     print(i)

##### MAKING a NEW TABLE

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="study"
)
print(mydb)
# print("conncection is established")

mycursor= mydb.cursor()
mycursor.execute("create table product (id int, name VARCHAR(255))") 
# HAR BAR REFRESH KRNA HAI

##### HOMEWORK ####
