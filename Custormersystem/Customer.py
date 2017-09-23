class Customer(object):
    def __init__(self, firstname, lastname, balance=0.0):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def getName(self):
        return self.firstname

    def getlastname(self):
        return self.lastname

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def __str__(self):
        return (self.firstname, self.lastname, self.balance)


def main():
    k = Customer("Ced", "Yest")
    print(k.getName())
    print(k.getlastname())



if __name__ == "__main__":
    main()
