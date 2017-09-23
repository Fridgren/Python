class Customer(object):
    def __init__(self, firstname, lastname, balance=0.0):
        self.firstname = firstname
        self.lastname = firstname
        self.balance = balance

    def getName(self):
        return self.firstname

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance


def main():
    k = Customer("Ced")
    print(k.getName())
    print(k.withdraw(-10))
    print(k.deposit(100))


if __name__ == "__main__":
    main()
