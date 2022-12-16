class Item:
    # def calculate_total_price(self):
    #     return self.price * self.quantity
    
    def calculate_total_price(self, x, y):
        return x * y
        

item1 = Item()
item1.name = "phone"
item1.price = 1000
item1.quantity = 5

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "notebook"
item2.price = 2500
item2.quantity = 3
print(item1.calculate_total_price(item2.price, item2.quantity))
