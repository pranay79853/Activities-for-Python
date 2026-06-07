class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"You have borrowed '{self.title}'."
        else:
            return f"Sorry, '{self.title}' is already borrowed."
        
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"You have returned '{self.title}'."
        else:
            return f"'{self.title}' was not borrowed."
        
book1 = Book("To Kill a Mockingbird", "Harper Lee")
print(book1)

book2 = Book("1984", "George Orwell")
print(book2)

book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(book3)

print(book1.title)
print(book1.author)
print(book1.is_borrowed)
print(book2.title)
print(book2.author)
print(book2.is_borrowed)
print(book3.title)
print(book3.author)
print(book3.is_borrowed)