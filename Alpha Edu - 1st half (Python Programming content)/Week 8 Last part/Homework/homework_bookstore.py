import sqlite3
class Bookstore:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        print(f"Connection to database {db_name} is successful")

    def create_table(self, table_name, column):
        column_definitions = []
        for name, dtype in column.items():
            column_definitions.append(f"{name} {dtype}")
        column_definitions = ", ".join(column_definitions)
        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
        try:
            self.cursor.execute(create_query)
            self.connection.commit() #This line ensures the changes are finalized and stored in the database.
            print(f" Table named {table_name} is created successfully")

        except sqlite3.Error as e:
            print(f"Error while creating the table {e}")

    def add_new_book(self, table_name, data):
        try:
            placeholder = ""
            for element in range(len(data[0])):
                placeholder += "?, "
            placeholder = placeholder.rstrip(", ") # Deletes the last , and space
            query_add_book = f"INSERT INTO {table_name} VALUES ({placeholder});"
            self.cursor.executemany(query_add_book, data)
            self.connection.commit()
        except  sqlite3.Error as error:
            print(f" Error while inserting data: {error}")

    def delete_existing_book(self, table_name, condition):
        try:
            delete_query = f"DELETE FROM {table_name} WHERE {condition};"
            self.cursor.execute(delete_query)
            self.connection.commit()
            print(f"✅ Данные с условием '{condition}' успешно удалены из таблицы '{table_name}'!")
        except  sqlite3.Error as error:
            print(f" Error while deleting data: {error}")

    def update_data(self, table_name, updates, condition):
        """
        :param table_name:  we refer ti the table_name
        :param updates: we update th information
        :param condition: we set the condition
        :return: finish the function
        """
        try:
            update_query = f"UPDATE {table_name} SET {updates} WHERE {condition};"
            self.cursor.execute(update_query)
            self.connection.commit()
            print(f"✅ Data in table '{table_name}' was updated successfully!")
        except  sqlite3.Error as error:
            print(f" Error while updating the data: {error}")


    def search_the_book(self, table_name, title=None, book_author=None, book_year=None, genre=None):
        try:
            base_query = f"SELECT * FROM {table_name}"
            conditions = []
            parameters = []

            if title:
                conditions.append("Title = ?") #Column name is Book name
                parameters.append(title)

            if book_author:
                conditions.append("Author of the book = ?")
                parameters.append(book_author)

            if book_year:
                conditions.append("Book year = ?")
                parameters.append(book_year)

            if genre:
                conditions.append("Genre = ?")
                parameters.append(genre)

            # Combine conditions into the WHERE clause
            if conditions:
                where_clause = " WHERE " + " AND ".join(conditions)
                search_query = base_query + where_clause
            else:
                search_query = base_query

            print(f"Executing query {search_query} with parameters {parameters}")
            self.cursor.execute(search_query, parameters)
            results = self.cursor.fetchall()
            return results

        except sqlite3.Error as error:
            print(f"Error while searching: {error}")
            return None


db = Bookstore("bookstore_table.db") # This is a creation of the INSTANCES

# Создаём таблицу.
db.create_table(
    table_name="bookstore_table",
    column={
        "book_id":"INTEGER PRIMARY KEY AUTOINCREMENT",
        "title": "TEXT",
        "author": "VARCHAR(255)",
        "year": "DATE",
        "genre": "REAL",
        "price": "INTEGER",
        "amount": "INTEGER",
    }
)

db.add_new_book(table_name="bookstore_table",
                data=[
    (None, "1984", "George Orwell", "1949-06-08", "Fantasy", 150, 14),  # Dystopian, Price: 15
    (None, "To Kill a Mockingbird", "Harper Lee", "1960-07-11", "Friction", 180, 13),
    (None, "The Great Gatsby", "F. Scott Fitzgerald", "1925-04-10", "Detective", 10, 14),
    (None, "Moby Dick", "Herman Melville", "1851-10-18", "Romance", 120, 15),
    (None, "Pride and Prejudice", "Jane Austen", "1813-01-28", "Drama", 80, 10),
    (None, "War and Peace", "Leo Tolstoy", "1869-01-01", "Horror", 250, 12),
    (None, "The Catcher in the Rye", "J.D. Salinger", "1951-07-16", "Detective", 140, 5),
    (None, "The Hobbit", "J.R.R. Tolkien", "1937-09-21", "Science fiction", 200, 10),
    (None, "Brave New World", "Aldous Huxley", "1932-08-31", "Motivational", 220, 11),
    (None, "Crime and Punishment", "Fyodor Dostoevsky", "1866-01-01", "Romance", 180, 9),]
                )


# title (название книги) — TEXT. Название книги.
# author (автор книги) — VARCHAR(255). Автор книги (ограничение длины до 255 символов).
# year (год выпуска) — DATE. Год выпуска книги (формат: YYYY-MM-DD).
# genre (жанр) — TEXT. Жанр книги.
# price (цена книги) — REAL. Цена книги (в рублях или другой валюте).
# amount (количество) — INTEGER. Количество доступных экземпляров книги.






