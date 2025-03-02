# Custom Exceptions
class BookNotFoundException(Exception):
    def __init__(self, message="The requested book was not found in the library."):
        self.message = message
        super().__init__(self.message)

class BookAlreadyBorrowedException(Exception):
    def __init__(self, message="The book is already borrowed by someone else."):
        self.message = message
        super().__init__(self.message)

class MemberLimitExceededException(Exception):
    def __init__(self, message="A member can borrow only up to 3 books."):
        self.message = message
        super().__init__(self.message)

# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, is_borrowed={self.is_borrowed})"

# Member class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException()
        if book.is_borrowed:
            raise BookAlreadyBorrowedException()
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        else:
            print(f"{book.title} was not borrowed by {self.name}.")

    def __repr__(self):
        return f"Member(name={self.name}, borrowed_books={len(self.borrowed_books)})"

# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book with title '{title}' not found.")

    def __repr__(self):
        return f"Library(Books={len(self.books)}, Members={len(self.members)})"

# Testing the system
if __name__ == "__main__":
    # Create library, books, and members
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    book4 = Book("Moby Dick", "Herman Melville")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    member1 = Member("Alice")
    member2 = Member("Bob")

    library.add_member(member1)
    library.add_member(member2)

    # Borrow books and test exceptions
    try:
        member1.borrow_book(book1)
        member1.borrow_book(book2)
        member1.borrow_book(book3)
        member1.borrow_book(book4)  # Should raise MemberLimitExceededException
    except MemberLimitExceededException as e:
        print(e)

    try:
        member2.borrow_book(book1)  # Should raise BookAlreadyBorrowedException
    except BookAlreadyBorrowedException as e:
        print(e)

    # Return book and try borrowing again
    member1.return_book(book1)

    try:
        member2.borrow_book(book1)  # Should be successful now
        print(f"{member2.name} borrowed '{book1.title}'.")
    except Exception as e:
        print(e)

    # Test book not found exception
    try:
        book_not_found = library.find_book("Nonexistent Book")  # Should raise BookNotFoundException
    except BookNotFoundException as e:
        print(e)

    # Show current state of library and members
    print(library)
    print(member1)
    print(member2)
