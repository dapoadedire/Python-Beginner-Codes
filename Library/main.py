from library import Book
from user import User


book1 = Book("Daily Stoics", "Ruan Halliday", "Blue Moon Publisher", 2013, "Country","English", 247, 50)



user1 = User("Adedire Adedapo Farouq", "Student")
user2 = User("Mr. Adedire", "Librarian")
user3 = User("Dr. Tesla", "Teacher")


book1.change_in_quantity()
print(book1.quantity)
book1.change_in_price()
print(book1.price)

print(book1)

print(user1.name)