

class Customer(object):

    def __init__(self, name, age):
            self.name = name
            self.age = age
            print("A customer object is created.")

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

