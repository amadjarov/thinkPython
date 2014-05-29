class BalanceError(Exception):
    value = "Sorry you only have $%6.2f in your account"

class BankAccount(object):
    def __init__(self, initialAmount):
        self.balance = initialAmount
        print "Account created with balance %5.2f" % self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            raise BalanceError, BalanceError.value % self.balance

    def checkBalance(self):
        return self.balance
       
    def transfer(self, amount, account):
        try:
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceError:
            print BalanceError.value
            
class InterestAccount(BankAccount):
    def deposit(self, amount):
        #super(InterestAccount, self).deposit(amount)
        BankAccount.deposit(self,amount)
        self.balance = self.balance * 1.03
       
class ChargingAccount(BankAccount):
    def __init__(self, initialAmount):
        BankAccount.__init__(self, initialAmount)
        self.fee = 3
        
    def withdraw(self, amount):
        BankAccount.withdraw(self, amount+self.fee)
        
a = BankAccount(500)
b = BankAccount(200)
a.withdraw(100)
#a.withdraw(1000)
a.transfer(100,b)
print "A = ", a.checkBalance()
print "B = ", b.checkBalance()


# Now an InterestAccount
c = InterestAccount(1000)
c.deposit(100)
print "C = ", c.checkBalance()


# Then a ChargingAccount
d = ChargingAccount(300)
d.deposit(200)
print "D = ", d.checkBalance()
d.withdraw(50)
print "D = ", d.checkBalance()
d.transfer(100,a)
print "A = ", a.checkBalance()
print "D = ", d.checkBalance()


# Finally transfer from charging account to the interest one
# The charging one should charge and the interest one add
# interest
print "C = ", c.checkBalance()
print "D = ", d.checkBalance()
d.transfer(20,c)
print "C = ", c.checkBalance()
print "D = ", d.checkBalance()
