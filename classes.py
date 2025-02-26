# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class

class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1

# Customer class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

# init user object
ron = User('Ron Ron', 'ron@gmail.com', 26)
mike = User('Mike Mike', 'mike@gmail.com', 16)

# edit property
ron.age = 36

print(ron.name)
print(ron.age)
# print(mike.name)

ron.has_birthday()

# call method
print(ron.greeting())



# init customer
john = Customer('John Doe', 'john@gmail.com' , 50)

john.set_balance(5000)

print(john.greeting())