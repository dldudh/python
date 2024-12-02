class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print("title = ", self.title)
        print("author = ", self.author)
        print("price = ", self.price)

    def __eq__(self, other):
        if self.price == other.price:
            print("Ture")

book = Book("abc", "fff",123)
book2 = Book("title", "23", 123)
book.display_info()
book2.display_info()

book.__eq__(book2)

print(book == book2)
