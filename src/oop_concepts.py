import csv

class Item:
    # class attribute
    pay_rate = 0.8 # after giving 20% discount

    all = [] # to all the instances
    def __init__(self, name: str, price: float, quantity: int = 0):   # creating the constructor of the class with validating the arguments
        # Run validation to receive arguments
        assert price >= 0, f"Price {price}is not greater than or equal to zero!"
        assert quantity >= 0, f"Price {quantity}is not greater than or equal to zero!"

        #Assign to self object
        # having just the _ is for readonly
        # having __ indicates that it's a private attribute
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)


    @property
    def price(self):
        return self.__price


    def apply_discount(self):
        self.__price = self.__price * self.pay_rate


    def apply_increment(self,incement_rate):
        self.__price = self.__price + self.__price * incement_rate


    @property  # property decorator = read-only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    def calculate_total_price(self):
        total_price = self.__price * self.quantity
        return total_price

    def get_info(self):
        return f"Name: {self.__name}, Price: {self.__price}, Quantity: {self.quantity}"


    @classmethod
    def instanciate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    def __repr__(self): # use of magic method representative
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"

item6 = Item("Cable", 20,30)
print(f"item6:{item6.apply_increment(5)}")
print(f"item6 info:{item6.get_info()}")
Item.instanciate_from_csv()
print(Item.all)

"""
item1 = Item("Phone", 100, 5)   # creating an instance of the class Item()
item2 = Item("Laptop", 2000, 10)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
for instances in Item.all:
    pass
    #print(instances.name)
print(f"Total price for {item1.name} is : {item1.calculate_total_price()}")
print(f"Total price for {item2.name} is : {item2.calculate_total_price()}")

print(item1.get_info())
print(item2.get_info())
item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.5
item2.apply_discount()
print(item2.price)

'''print(Item. __dict__)  # All the attribute for class level (using magic attribute(__dict__))
print(item1. __dict__)  #All the attribute for instance level'''
"""

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0, broken_phone: int = 0):   # creating the constructor of the class with validating the arguments
        #calling super class
        super().__init__(name, price, quantity)

        # Run validation to receive arguments
        assert broken_phone >= 0, f"Broken Phone {broken_phone}is not greater than or equal to zero!"

        #Assign to self object
        self.broken_phone = broken_phone


phone1 = Phone("BlackBerry",25, 30, 3)
phone2 = Phone("Nokia",30, 5, 1)

print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all)

