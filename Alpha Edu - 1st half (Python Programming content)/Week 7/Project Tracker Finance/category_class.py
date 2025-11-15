class Category:
    def __init__(self, name):
        #name: Name of the category (Food, entertainment)
        self.name = name

    # Method for string version of category
    # It allows as NORMAL DISPLAY from the print Category
    def __str__(self):
        return f"{self.name}" # Returns string even though integer etc

# a = Category("Food")
# print(a)
