class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Gets
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_pages(self):
        return self.pages

    # Sets
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def set_pages(self, pages):
        self.pages = pages

    @classmethod
    def estimated_reading_time(cls, pages, words_per_minute):
        
        # Apparently books hav 300 words per page at average (so says google)
        words = 300 * pages
        return words / words_per_minute

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"


class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Format: {self.format}"


book1 = Book("Idk some cool book", "Me", 560)
print(book1)  

book1.set_title("cool book")
print(book1.get_title())  

estimated_time = Book.estimated_reading_time(book1.get_pages(), 100)
print(f"Estimated reading time at 100 wpm: {estimated_time:.2f} minutes")

ebook1 = Ebook("awsome book", "again me", 1138, "mobi")
print(ebook1)
