class Library:

    def __init__(self, booklist,library_name):
        self.booklist = booklist
        self.library_name = library_name
        self.bookdata = {}
        for books in self.booklist:
            self.bookdata[books] = None


    def display_books(self):
        for books in self.booklist:
            print(books)


    def withdraw_books(self,nm,book):
        if book in self.bookdata:
            if self.bookdata[book] == None:
                self.bookdata = nm
                print(f"Please take this book {book}")
            else:
                print("Sorry the book is already taken")

        else:
            print(f"{book} is a invalid book")



    def add_book(self,book):
        if book in self.bookdata:
            print("Book already exists")
        else:
            self.booklist.append(book)

    def return_book(self,nm,book):
        if self.bookdata[book] == nm:
            print(f"Hi {nm} thanks for returning the book")
            self.bookdata[book] = None

    def delete_book(self,book):
        if book in self.bookdata:
            self.bookdata.pop(book)
            self.booklist.remove(book)
        else:
            print("The mentioned book doesnt exist in our Library")

    def show_users(self):
        for book in self.bookdata:
            print(self.bookdata[book])


def main():
    mybooklist = ["How to build good resume", "Data Structures", "Panchatantra", "Tinkle", "Chandamama"]
    name = "Sandeep"
    secret_key = 47356

    lib = Library(mybooklist,name)

    print("="*30)
    print(f"                    welcome to {lib.library_name} Library")
    print("="*30)
    print("\nTo display all books type 'l'")
    print("To withdraw any book type 'w'")
    print("To add any book type 'a'")
    print("To return any book type 'r'")
    print("To delete any book type 'del'")
    print("To check Books data type 'data'")
    print("To quit type 'q'")


    while True:
        print("Enter the Input/n")
        task = str(input())

        if task == 'l':
            lib.display_books()

        elif task == 'w':
            nm1 = input("Enter your name : ")
            book1 = input("Enter the book name: ")
            lib.withdraw_books(nm1,book1)

        elif task == 'a':
            book2 = input("Enter the book name: ")
            lib.add_book(book2)

        elif task == 'r':
            nm3 = input("Enter your name : ")
            book3 = input("Enter the book name: ")
            lib.return_book(nm3,book3)



        elif task == "del":
            task_secret = int(input("Write the secret key to delete:"))
            if (task_secret == secret_key):
                input1 = input("Book Which you want to delete:")
                lib.delete_book(input1)
            else:
                print("Sorry We can't Delete the Book")

        elif task == 'data':

            lib.show_users()

        elif task == 'q':
            break

        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
