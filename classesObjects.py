# classes so it can Inherit
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        # polymorphs
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Borrowed' if self.is_borrowed else 'Available'}"


class Library:
    def __init__(self):
        # encapsulates a collection of books
        self.books = {}

    def add_book(self, title, author, isbn):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = Book(title, author, isbn)

    def borrow_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if book.is_borrowed:
                print(f"Book '{book.title}' is currently unavailable.")
            else:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
        else:
            print("Book not found.")

    def return_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if not book.is_borrowed:
                print(f"Book '{book.title}' was not borrowed.")
            else:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'.")
        else:
            print("Book not found.")

    def display_available_books(self):
        available_books = [book for book in self.books.values() if not book.is_borrowed]
        if available_books:
            print("\nAvailable Books:")
            for book in available_books:
                print(book)
        else:
            print("No books available.")

# main function to demonstrate the functionality of each 
def main():
    library = Library()
    sample_books = [
        ("Harry Potter and the Sorcerer’s Stone", "J.K. Rowling", "12345"),
        ("Lord of the Rings", "J. R. R. Tolkien", "67891"),
        ("The Great Gatsby", "F. Scott Fitzgerald", "98765"),
        ("To Kill a Mockingbird", "Harper Lee", "43210"),
        ("The Twilight Saga", "Stephenie Meyer", "13579"),
    ]

    for title, author, isbn in sample_books:
        library.add_book(title, author, isbn)

    library.display_available_books()

    while True:
        print("\nOptions:")
        print("1. Display available books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit\n")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            library.display_available_books()
        elif choice == '2':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            isbn = input("Enter the book ISBN (5 digits): ")
            library.add_book(title, author, isbn)
        elif choice == '3':
            isbn = input("Enter ISBN of the book to borrow: ")
            library.borrow_book(isbn)
        elif choice == '4':
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)
        elif choice == '5':
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5. \n")


if __name__ == "__main__":
    main()
