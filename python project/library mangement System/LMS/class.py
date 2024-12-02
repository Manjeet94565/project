class Book:
    def __init__(self, title, author, status='available'):
        self.title = title
        self.author = author
        self.status = status

    def issue_book(self):
        if self.status == 'available':
            self.status = 'issued'
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.status == 'issued':
            self.status = 'available'
        else:
            print("Book is already available.")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def issue_book(self, member_id, book_title):
        for book in self.books:
            if book.title == book_title:
                book.issue_book()
                return
        print("Book not found.")

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                book.return_book()
                return
        print("Book not found.")

def save_books_to_file(library):
    with open("books.txt", "w") as f:
        for book in library.books:
            f.write(f"{book.title},{book.author},{book.status}\n")

def load_books_from_file(library):
    try:
        with open("books.txt", "r") as f:
            for line in f:
                title, author, status = line.strip().split(',')
                library.add_book(Book(title, author, status))
    except FileNotFoundError:
        print("No books found. Starting with an empty library.")

def main():
    library = Library()
    load_books_from_file(library)

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(Book(title, author))
        elif choice == '2':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.register_member(Member(name, member_id))
        elif choice == '3':
            member_id = input("Enter member ID: ")
            book_title = input("Enter book title to issue: ")
            library.issue_book(member_id, book_title)
        elif choice == '4':
            book_title = input("Enter book title to return: ")
            library.return_book(book_title)
        elif choice == '5':
            for book in library.books:
                print(f"{book.title} by {book.author} - {book.status}")
        elif choice == '6':
            save_books_to_file(library)
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

