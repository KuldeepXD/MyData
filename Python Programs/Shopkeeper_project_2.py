#Delivery Charges Calculator Program
a='y'
while a=='y':
    Purchase_cost=float(input("Please enter the purchase cost"))
    if(Purchase_cost>150):
        Items=float(input("Please enter the number of items"))
        Delivery_day=float(input("Please enter delivery day ([1] for 1st day and [2] for 2nd day)"))
        if(Items<=5):
            if(Delivery_day==1):
                Delivery_charges= 8.0
                print(f"Delivery Charges={Delivery_charges}$")
                Cost= (Purchase_cost+Delivery_charges)
                print(f"Total Cost= {Cost}$")
            elif(Delivery_day==2):
                Delivery_charges=Items*1.50
                print(f"Delivery Charges={Delivery_charges}$")
                Cost= (Purchase_cost+Delivery_charges)
                print(f"Total Cost={Cost}$")
        elif(Items>=6):
            if(Delivery_day==1):
                Delivery_charges=Items*2.50
                print(f"Delivery Charges={Delivery_charges}$")
                Cost= (Purchase_cost+Delivery_charges)
                print(f"Total Cost={Cost}$")
            elif(Delivery_day==2):
                Delivery_charges=Items*1.20
                print(f"Delivery Charges={Delivery_charges}$")
                Cost= (Purchase_cost+Delivery_charges)
                print(f"Total Cost={Cost}$")
    else:
        print("\nSorry, purchase total need to be above $150\n")
    
    v= str(input("Do you want to calculcate for another purchase: y/n"))
    if(v=='y'):
        a='y'
    else:
        a='n'
        print("\nThanks for using the delivery charges Calculator!\nSee you again!")


'''Special Note: While me koi else nahi hota.'''