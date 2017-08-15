class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    """This class generates checking account objects."""
    type = "checking"
    #class variable

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

jack_checking = Checking("jack.txt", 1)
jack_checking.transfer(10)
jack_checking.commit()
print(jack_checking.balance)
print(jack_checking.type)
#object instance

jill_checking = Checking("jill.txt", 1)
jill_checking.transfer(10)
jill_checking.commit()
print(jill_checking.balance)
print(jill_checking.type)
#another object instance

print(jack_checking.__doc__)

#account = Account("balance.txt")
#print(account.balance)
#account.withdraw(1)
#account.deposit(1)
#account.commit()
#print(account.balance)
