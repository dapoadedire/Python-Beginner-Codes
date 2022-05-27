from random import randrange
import csv

class Book:
    discount =  randrange(60, 100)/100
    all_book = []
    def __init__(self, title, author, year, country, language, pages:int, price:float, quantity):
        
        #assert price >= 0, f"Price {price} is not greater than or equals to zero!"
        self.title = title
        self.author = author
        self.year = year
        self.country = country
        self.language = language
        self.pages = pages
        self.price = price
        self.quantity = quantity

        Book.all_book.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.title}, {self.author}, {self.year}, {self.country}, {self.language}, {self.pages}, {self.price}')"


    def change_in_quantity(self):
        self.quantity = self.quantity - int(1)
        return self.quantity

    def change_in_price(self):
        self.price = self.price * self.discount
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('PYTHON/Library/books.csv', 'r') as f:
            reader = csv.DictReader(f)
            books = list(reader)

        for book in books:
            Book(
                title = book.get('title'),
                author = book.get('author'),
                year = book.get('year'),
                country = book.get('country'),
                language = book.get('language'),
                pages = book.get('pages'),
                price = book.get('price'),
                quantity = book.get('quantity')
            )

Book.instantiate_from_csv()
print(Book.all_book)

        


