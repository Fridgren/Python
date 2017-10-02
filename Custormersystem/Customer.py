class Customer(object):
    def __init__(self, firstname, lastname, age, balance=0.0):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.balance = balance
        print("A customer object is created.")

    def get_name(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def getAge(self):
        return self.age

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def __str__(self):
        print("Firstame:", self.firstname)
        print("Lastname:", self.lastname)
        print("Age:", self.age)
        print("Balance:", self.balance)
        print()
    #
    # def print_details(self):
    #     print("Firstame:", self.firstname)
    #     print("Lastname:", self.lastname)
    #     print("Age:", self.age)
    #     print("Balance:", self.balance)
    #     print()

def main():
    k = Customer("Cedric", "Fridgren", 30, 1500)
    print(k.__str__())



if __name__ == "__main__":
    main()
