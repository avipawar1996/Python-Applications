'''
Write a python program to implement a class named BookStore with the following requirements:
    - Class should contain two instance variable: Name(Book Name) and AUthor (Book Author)
    - Class should contain one class variable:
        NoOfBooks (initialize it to 0)
    - Define a constructor (__init__()) that accept Name and Author and initializes instance variables

    - Inside a constructor, increment the class variable NoOfBooks by 1 whenever new object is created.

    - Implement an instance methods:
        Display()        - Should display the book details in the format:
            <BookName> by <Author>. No of Books: <NoOfBooks>

    Example Usage:
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display() # Linux System Programming by Robert Love. No of Books: 1

    Obj1 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display() # C Programming by Dennis Ritchie. No of Books: 2
'''

class BookStore:

    NoOfBooks = 0

    def __init__(self, NameOfBook, AuthorOfBook):
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
        self.NameOfBook = NameOfBook
        self.AuthorOfBook = AuthorOfBook

    def Display(self):
        print(f"\n {self.NameOfBook} by {self.AuthorOfBook}. No of Books: {BookStore.NoOfBooks}")
        print("-------------------------------------------------")


Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()