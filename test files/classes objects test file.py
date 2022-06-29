class Library:

    def __init__(self, list_of_books):
        self.books = list_of_books

    def display_available_books(self):
        print("Books present in this library are")
        for book in self.books:
            print(" " + book)

    def borrow_books(self, book_name):
        if book_name in self.books:
            print(f"You have been issued {book_name}.Please keep it safe")
            self.books.remove(book_name)
        else:
            print("Sorry, this book is already issued to someone else")

    def returnBooks(self, book_name):
        self.books.append(book_name)
        print("Thank you for retuning this book")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return")
        return self.book


def clear_screen():
    print('\n' * 25)


if __name__ == "__main__":
    clear_screen()
    centralLibrary = Library(
        ["Algorithms in Py", "Py Framework Django", "Py website Flask", "AI with Py", "Data Sc with Py"])
    # centralLibrary.displayAvailableBooks()
    student = Student()
    while True:
        welcomeMsg = '''++++Welcome to Central Library +++++
        Please choose an option
        1 List all books
        2 Request a book
        3 Return a book
        4 Exit the program
         '''

        print(welcomeMsg)
        a = int(input("Enter a choice  - "))
        if a == 1:
            centralLibrary.display_available_books()
        elif a == 2:

            centralLibrary.borrow_books(student.requestBook())
        elif a == 3:
            centralLibrary.returnBooks(student.returnBook())

        elif a == 4:
            exit()

        else:
            print("Invalid choice")
