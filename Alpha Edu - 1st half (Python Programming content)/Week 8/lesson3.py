import sqlite3
class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        print(f" Connection to the databse {db_name} is successful")

    def create_table(self, table_name, columns):
        column_definitions = []
        for name, dtype in columns.items():
            column_definitions.append(f"{name} {dtype}")
        column_definitions = ", ".join(column_definitions)

        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
        try:
            self.cursor.execute(create_query)
            self.connection.commit()
            print(f" Table named {table_name} is created successfully")

        except sqlite3.Error as e:
            print(f"Error while creating the table {e}")


    def insert_data(self, table_name, data):

        try:
            placeholders = ""
            for element in range(len(data[0])):
                placeholders += "?, "
            """
            placeholders = "?, ?, ?, ?, "
            """
            placeholders = placeholders.rstrip(", ") # deletes the unnessasary spaces and , at the end
            print("This is how placeholders", placeholders)
            """
            placeholder = "?, ?, ?, ?, "
            """
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
            self.cursor.executemany(insert_query, data) #Here we insert data
            self.connection.commit()

        except  sqlite3.Error as error:
            print(f" Error while inserting data: {error}")

    def change_column_name(self, table_name, old_column_name, new_column_name):
        change_query = f"ALTER TABLE {table_name} RENAME COLUMN {old_column_name} to {new_column_name};"
        self.cursor.execute(change_query)
        self.connection.commit()
        print(f"Column name changed successfully from {old_column_name} {new_column_name}")


db = DatabaseManager("students_table.db")


# Создаём таблицу.
db.create_table(
    table_name="students_table",
    columns={
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT",
        "age": "INTEGER",
        "grade": "REAL",
    }
)

# Вставляем данные.
db.insert_data(
    table_name="students_table",
    data=[
        (None, "Alice", 20, 85.5),
        (None, "Bob", 22, 90.0),
        (None, "Charlie", 21, 78.3),
        (None, "Ken", 19, 75.5),
        (None, "Barbie", 17, 90.0),
    ]
)

# def fetch_all(self, table_name):
#     """
#     :param self:
#     :param table_name: Table name str
#     :return:
#     """
#     try:
#         fetch_query = f"SELECT * FROM {table_name};"
#         self.cursor.execute(fetch_query)
#         results = self.cursor.fetchall()
#         # we do commit when we do changes and saves the changes and registers them
#         print(f"Data was obtained from table {table_name}")
#         print(f"Our data: {results}")
#         for row in results:
#             print(row)
#         return results
#     except sqlite3.Error as e

db.change_column_name("students_table.db", "age", "years")
