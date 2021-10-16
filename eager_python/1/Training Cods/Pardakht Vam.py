#Pardakht Vam
# Your function for calculating payment goes here
def monthly_payment(principal,annual_rate,duration):
    r= (annual_rate/100)/12
    duration=duration*12
    if annual_rate==0:
        payment=principal/n
        return payment
    else:
        payment = (principal*(r*((1+r)**duration)))/(((1+r)**duration) - 1)
        return payment
# Your function for calculating remaining balance goes here
def RLB(principal,annual_rate,duration,p):
    r= (annual_rate/100)/12
    duration=duration*12    
    if annual_rate==0:
        repayment=principal*(1-p/duration)
        return repayment
    else:
        repayment = (principal*(((1+r)**duration)-((1+r)**p)))/(((1+r)**duration) - 1)
        return repayment         
# Your main program goes here

principal=float(input("Enter loan amount: "))
annual_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

print("LOAN AMOUNT: {} INTEREST RATE (PERCENT): {}".format(int(principal),int(annual_rate)))
print("DURATION (YEARS): {} MONTHLY PAYMENT: {}".format(duration,int(monthly_payment(principal,annual_rate,duration))))
a=range(1,duration+1)
for n in a:

    print("YEAR: {} BALANCE: {} TOTAL PAYMENT {}"
            .format(n,int(RLB(principal,annual_rate,duration,n*12)),int(monthly_payment(principal,annual_rate,duration)*n*12)))



"""
# Your function for calculating payment goes here
def monthly_payment(principal,annual_rate,duration):
    r= (annual_rate/100)/12
    duration=duration*12
    if annual_rate==0:
        payment=principal/n
        return payment
    else:
        payment = (principal*(r*((1+r)**duration)))/(((1+r)**duration) - 1)
        return payment
# Your function for calculating remaining balance goes here
def RLB(principal,annual_rate,duration,p):
    r= (annual_rate/100)/12
    duration=duration*12    
    if annual_rate==0:
        repayment=principal*(1-p/duration)
        return repayment
    else:
        repayment = (principal*(((1+r)**duration)-((1+r)**p)))/(((1+r)**duration) - 1)
        return repayment         
# Your main program goes here
principal=float(input("Enter loan amount: "))
annual_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

print("LOAN AMOUNT: {} INTEREST RATE (PERCENT): {}".format(int(principal),int(annual_rate)))
print("DURATION (YEARS): {} MONTHLY PAYMENT: {}".format(duration,int(monthly_payment(principal,annual_rate,duration))))

print("YEAR: 1 BALANCE: {} TOTAL PAYMENT {}"
      .format(int(RLB(principal,annual_rate,duration,12)),int(monthly_payment(principal,annual_rate,duration)*12)))
print("YEAR: 2 BALANCE: {} TOTAL PAYMENT {}"
      .format(int(RLB(principal,annual_rate,duration,24)),int(monthly_payment(principal,annual_rate,duration)*24)))
print("YEAR: 3 BALANCE: {} TOTAL PAYMENT {}"
      .format(int(RLB(principal,annual_rate,duration,36)),int(monthly_payment(principal,annual_rate,duration)*36)))
print("YEAR: 4 BALANCE: {} TOTAL PAYMENT {}"
      .format(int(RLB(principal,annual_rate,duration,48)),int(monthly_payment(principal,annual_rate,duration)*48)))
print("YEAR: 5 BALANCE: {} TOTAL PAYMENT {}"

#print("YEAR: 2 BALANCE: {} TOTAL PAYMENT {}"
#   .format(int(RLB(principal,annual_rate,duration,24)),int(monthly_payment(principal,annual_rate,duration)*24)))
#print("YEAR: 3 BALANCE: {} TOTAL PAYMENT {}"
#   .format(int(RLB(principal,annual_rate,duration,36)),int(monthly_payment(principal,annual_rate,duration)*36)))
#print("YEAR: 4 BALANCE: {} TOTAL PAYMENT {}"
#   .format(int(RLB(principal,annual_rate,duration,48)),int(monthly_payment(principal,annual_rate,duration)*48)))
#print("YEAR: 5 BALANCE: {} TOTAL PAYMENT {}"
#   .format(int(RLB(principal,annual_rate,duration,60)),int(monthly_payment(principal,annual_rate,duration)*60)))
"""
