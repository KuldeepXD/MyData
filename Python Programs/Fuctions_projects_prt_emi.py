#SALARY AND BONUS PROJECT-MAil
# contribute_rate=0.05

# def show_pay_contrib(bonus):
#     contrib= bonus*contribute_rate
#     print("Contribution for gross pay",contrib)

# def show_bonus_contrib(bonus):
#     contrib=bonus*contribute_rate
#     print("Contribution for bonuses",contrib)

# def main():
#     gross_pay= float(input("enter the gross pay: "))
#     bonus = float(input("enter the bonus: "))
#     show_bonus_contrib(bonus)
#     show_pay_contrib(gross_pay)
    

# main()

###### Keyword Argumen!!!!!!
# RAte of interest program

def rate_of_interest(principal,rate,time):
    roi=(principal*rate*time)
    print("Rate of interest is ",roi)

def main():
    principal= float(input("enter the principal: "))
    rate = float(input("enter the rate: "))
    time = float(input("enter the time in months: "))
    time1= time/12
    rate1= rate/100

    rate_of_interest(rate=rate1,principal=principal,time=time1)

main()


##### Loan program using function #############

# def loan(amount,rate,time):
#    emi_amount=amount*(rate/100)
#    gross_loan_per_year= amount+(emi_amount*time)
#    gross_emi_per_month= (gross_loan_per_year/12) #per month calculation of gross loan amount
#    print((gross_loan_per_year))
#    print((gross_emi_per_month))

# def main():
#     amount= float(input("enter the amount: "))
#     rate = float(input("enter the emi rate: "))
#     time= float(input("enter the time period in months: "))
#     loan(amount,rate,time)

# main()