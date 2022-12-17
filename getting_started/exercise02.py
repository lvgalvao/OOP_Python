class Item:
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity:int=0) -> None:
        # Run validations to the received aruments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # Assign to self object
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
item1 = Item("Phone", 1000.0, 2)
print(item1.price)
item1.apply_discount()
print(item1.price)

item2 = Item("Notebook", 1000.0)
print(item2.price)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)


item2 = Item("Notebook", 2500)

# print(item1.calculate_total_price(item2.price, item2.quantity))

# print(item1.name, item1.quantity, item1.pay_rate)
# print(item2.name, item2.quantity)
# print(item1.calculate_total_price())

# print(item1.__dict__) # All the attributes for Instance Level
# print(Item.__dict__) # All the attributes for Class Level