##Sharad: callign account class 
from Assisgments.ch7_3 import Account


def main():
    ## create object 
    ac1 = Account(1122, 20000, 4.5/100)
    ac1.withdraw(2500)
    ac1.deposit(3000)
    ## use methods to get the required data 
    print("id:",ac1.getId())
    print("balance:", '{}{}'.format("$",ac1.getBalance()) )
    print("monthly interest rate:", ac1.getMonthlyInterestRate())
    print("monthly interest :", '{}{}'.format("$",ac1.getMonthlyInterest()) )

main()