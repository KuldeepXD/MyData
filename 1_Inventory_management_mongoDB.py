#Importing mongo db library in python

import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["inventory_system"]

#Getting input from user for given choices

select_option=input("choose an option:\n1. Add Customer data\n2. Add items into database\n3.New purchase")

# Adding Customer's info to Database

if select_option=='1':
    def customers1():
        mycol=mydb["customers"]
        customers=int(input("how many customers you want to add:"))
        for i in range(1,customers+1):
            name=input("enter name of customer:")
            age=int(input("enter your age:"))
            gender = input("enter your gender:")
            address=input("enter your address:")
            _id1=int(input("enter id:"))
            mylist1={"_id":_id1,"name": name,"age": age,"gender": gender,"address": address}
            x=mycol.insert_one(mylist1)
    customers1()
    
# Adding  items into inventory

if select_option=='2':
    def items1():
        mycol1=mydb["items"]
        items=int(input("enter the number of items:"))
        for i in range(1,items+1):
            item_name=input('enter item name:')
            price=int(input("enter the price:"))
            quantity=int(input("enter the quantity:"))
            myitems={"item_name":item_name,"price":price,"quantity":quantity}
            x=mycol1.insert_one(myitems)
    items1()

#Fetching items, multiple purchases, printing final bill
if select_option=='3':
    l=[]
    p=[]
    def buy_item():
        mycol1 = mydb["items"]
        global buyitem
        buyitem=input("which item you want to buy:")
        global g
        h=[]
        for i in mycol1.find():
            g=i.get('item_name')
            h.append(g)
        print(h)
        if buyitem in h:
            for i in mycol1.find({'item_name':buyitem}):
                global a
                a=i.get('quantity')
            global quant
            quant=int(input("how many items you want to purchase:"))
            if quant<=0:
                print('sorry, not valid')
                buy_item()
            elif quant>=0:
                myold={'item_name':buyitem}
                mynew={"$set":{"quantity":a-quant}}
                mycol1.update_one(myold,mynew)

                for i in mycol1.find({'item_name': buyitem}):
                    global b
                    b=i.get('quantity')
                    print('remaining items:',b)


                for i in mycol1.find({'item_name': buyitem}):
                    global c
                    c=i.get('price')

                l.append([buyitem, quant,c])
                price=c*quant
                p.append(price)

                def anotherpurchase():
                    another_purchase=input('do you want to purchase again?')
                    if another_purchase=='y':
                        buy_item()
                    if another_purchase=='n':
                        pass
                anotherpurchase()
        else:
            print('name error')
    buy_item()
    for i in l:
        item=i[0]
        quantity=i[1]
        price=i[2]
        print(f'item: {item} , quantity: {quantity} , price: {price}')
    total_bill=0
    for i in p:
        total_bill+=i
    print('total bill : ',total_bill)







