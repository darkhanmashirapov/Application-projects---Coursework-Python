data=[
    (None, "1984", "George Orwell", "1949-06-08", 1.5, 15),  # Dystopian, Price: 15
    (None, "To Kill a Mockingbird", "Harper Lee", "1960-07-11", 2.0, 18),
    (None, "The Great Gatsby", "F. Scott Fitzgerald", "1925-04-10", 3.0, 10),
    (None, "Moby Dick", "Herman Melville", "1851-10-18", 4.5, 12),
    (None, "Pride and Prejudice", "Jane Austen", "1813-01-28", 1.0, 8),
    (None, "War and Peace", "Leo Tolstoy", "1869-01-01", 5.0, 25),
    (None, "The Catcher in the Rye", "J.D. Salinger", "1951-07-16", 2.5, 14),
    (None, "The Hobbit", "J.R.R. Tolkien", "1937-09-21", 3.0, 20),
    (None, "Brave New World", "Aldous Huxley", "1932-08-31", 3.5, 22),
    (None, "Crime and Punishment", "Fyodor Dostoevsky", "1866-01-01", 4.0, 18),]

placeholder = ""
for element in range(len(data[0])):
    placeholder += "?, "
placeholder = placeholder.rsplit(", ") # Deletes the last , and space
placeholder = ", ".join(placeholder)
print(placeholder)