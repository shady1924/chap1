# # Sharad: Account Class
class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    
    # # accessors
    def getId(self):
        return self.__id
    def getBalance(self):
        return self.__balance
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    # # mutators 
    def setId(self, id):
        self.__id = id
    def setBalance(self, balance):
        self.__balance = balance
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
    
    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12 
    
    def getMonthlyInterest(self):
        monthlyInterest = (self.__annualInterestRate / 12 ) * self.__balance
        return monthlyInterest
    
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        return self.__balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        return self.__balance
