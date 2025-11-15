from homework_bookstore import *
class Person:
    def __init__(self, name, bookstore):
        """
        :param name: Name of the person
        :param bookstore: Instances of the Bookstore class
        """
        self.name = name
        self.bookstore = bookstore

    def search_book(self, title=None, author=None, year=None, genre=None):
        """
        :param title:
        :param author:
        :param year:
        :param genre:
        :return:
        """
        try:
            results = self.bookstore.search_the_book(
                table_name="bookstore_table",
                title=title,
                book_author=author,
                book_year=year,
                genre=genre,
            )
            if results:
                print("Your book is found")
                for result in results:
                    print(result)
            else:
                print("There is no book in the store matching your criteria")
        except sqlite3.Error as e:
            print(f"Error {e} occurred during the search")

    def buy_book(self, book_title):
        try:
            books = self.bookstore.search_the_book(
                table_name="bookstore_table",
                title=book_title,
            )
            if books:
                book = books[0]
                book_id, title, author, year, genre, price, amount = book # as the first element is tuple, every element will be assigned to new variable
                if amount>0:
                    self.bookstore.update_data(
                        table_name="bookstore_table",
                        updates=f" amount = {amount-1}",
                        condition=f"book_id = {book_id}",
                    )
                    print(f"{self.name} has purchased book '{title}' for {price} tenge")

                else:
                    print(f"Sorry the book named {title} is out of stock.")
            else:
                print(f"No book titled '{book_title}' was found.")
        except Exception as e:
            print(f"Error while purchasing the book: {e}")


# Example usage:
person = Person("Alice", db)
# Search for books
print("Searching for books by 'George Orwell':")
person.search_book(author="George Orwell")

# Purchase a book
print("\nPurchasing '1984':")
person.buy_book("1984")

# Verify the update
print("\nSearching for '1984' after purchase:")
person.search_book(title="1984")



def main_menu():
    db = Bookstore("bookstore_table.db")
    user = Person("User", db)

    while True:
        print("\nMenu:")
        print("1. Add a book (Admin only)")
        print("2. Delete a book (Admin only)")
        print("3. Update book details (Admin only)")
        print("4. Search for books")
        print("5. Buy a book")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year (YYYY-MM-DD): ")
            genre = input("Enter book genre: ")
            price = float(input("Enter book price: "))
            amount = int(input("Enter book amount: "))
            db.add_new_book(
                table_name="bookstore_table",
                data=[(None, title, author, year, genre, price, amount)]
            )
        elif choice == "2":
            title = input("Enter the title of the book to delete: ")
            db.delete_existing_book(
                table_name="bookstore_table",
                condition=f"title = '{title}'"
            )
        elif choice == "3":
            title = input("Enter the title of the book to update: ")
            field = input("Enter the field to update (e.g., price, amount): ")
            value = input(f"Enter the new value for {field}: ")
            db.update_data(
                table_name="bookstore_table",
                updates=f"{field} = '{value}'",
                condition=f"title = '{title}'"
            )
        elif choice == "4":
            title = input("Enter book title (or leave blank): ")
            author = input("Enter author name (or leave blank): ")
            year = input("Enter year (or leave blank): ")
            genre = input("Enter genre (or leave blank): ")
            user.search_books(title, author, year, genre)
        elif choice == "5":
            title = input("Enter the title of the book to buy: ")
            user.buy_book(title)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()