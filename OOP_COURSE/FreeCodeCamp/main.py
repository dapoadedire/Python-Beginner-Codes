from items import Item
from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("LaserJet", 200, 3)
item1.apply_discount()
print(item1.price)
"""
item0 = Item("Tesla Roadster", 200, 11)
item1 = Item("iPhone", 500, 5)
item2 = Item("MacBook Pro", 650, 5)
item3 = Item("Airpods", 100, 3)
item4 = Item("Starship", 1700, 26)
item5 = Item("Falcon Heavy", 230, 9)
item6 = Item("Falcon 9", 5400, 13)
item7 = Item("Model S", 1500, 40)
item8 = Item("Model 3", 1900, 5)
item9 = Item("Model X", 570, 3)
item10 = Item("Model Y", 200, 7)
item11 = Item("Tesla Bot", 340, 8)


#Setting an attribute
item1.name = "Tequila"      

# Getting an attribute
print(item1.name)

item3.apply_increment(1.2)
item4.apply_discount()
print(item3.price)
print(item4.price)


#Abstraction

item1.send_email()




phone1 = Phone("Nokia3310", 342, 6, 2)
phone2 = Phone("Nokia C3", 390, 16, 3)
print(phone1.calculate_total_price())

print(Item.all)
print(Phone.all)


Item.instantiate_from_csv()
#print(Item.all)
print(Item.is_integer(9.3))

for instance in Item.all:
    print(instance.name)

    instance.pay_rate = 0.5
item1.apply_discount()
print(item1.price)
item0 = Item("Tesla Roadster", 200, 11)
item1 = Item("iPhone", 500, 5)
item2 = Item("MacBook Pro", 650, 5)
item3 = Item("Airpods", 100, 3)
item4 = Item("Starship", 1700, 26)
item5 = Item("Falcon Heavy", 230, 9)
item6 = Item("Falcon 9", 5400, 13)
item7 = Item("Model S", 1500, 40)
item8 = Item("Model 3", 1900, 5)
item9 = Item("Model X", 570, 3)
item10 = Item("Model Y", 200, 7)
item11 = Item("Tesla Bot", 340, 8)


item1 = Item("iPhone", 500, 5)
item1.apply_discount()
print(item1.price)


item2 = Item("MacBook", 1500, 23)
item2.pay_rate = 0.5
item2.apply_discount()
print(item2.price)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())


# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)
# print(Item.__dict__) #All attributes for the Class level
# print(item1.__dict__) #All attributes for the instance level 

# item2.has_numpad = False

"""

