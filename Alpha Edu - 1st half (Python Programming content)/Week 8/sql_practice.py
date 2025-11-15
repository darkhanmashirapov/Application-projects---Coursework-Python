
import sqlite3

# Class for working with tthe databases:

class DatabaseManager:
    # Class for managing connection and interaction with databases SQLite.
    def __init__(self, db_name):
        #Contructor: initialization for connection to database.
        #:param dm_name: Name of the database
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        print(f"Connection to database is '{db_name} is successfull'")

    def create_table(self, table_name, columns):
        #Creates tables with given column names
        #param table_name: Name of the table.
        #param columns: Dictionary type (name of the table: type of the

        #We formulate SQL request for creating table
        column_definitions = ", ".join([f"{name} {dtype}" for name, dtype in columns.items()])
        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"

        try:
            self.cursor.execute(create_query)
            self.connection.commit()
            print(f"Table '{table_name}' was successfully created")
        except sqlite3.Error as e:
            print(f" Error while creating table: {e}")


    def insert_data(selfself, table_name, data):
        #
