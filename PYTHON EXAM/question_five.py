#i)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display_info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.pages}")
my_book = Book("A Clinton Story", "Cathylin Howard", 200)
my_book.display_info()


#ii)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display_info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.pages}")
class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format
    def display_info(self):
        super().display_info()
        print(f"Format: {self.format}")
my_ebook = EBook("Grammer2", "Tom Maganda", 100, "PDF")
my_ebook.display_info()


#iii)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display_info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.pages}")
    def get_title_and_author(self):
        
        return f"Book Title: {self.title}, Author: {self.author}"
my_book = Book("A Clinton Story", "Cathylin Howard", 200)
print(my_book.get_title_and_author()) 


#iv)
#a)
# a class is an object constructor


#b)
# an object is a container of data and functions.
 