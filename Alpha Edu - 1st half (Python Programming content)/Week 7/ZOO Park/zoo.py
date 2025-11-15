class Animal:
    def __init__(self, name, species, age, is_endangered=None):
        self.name = name
        self.species = species
        self.age = age
        self.is_endangered = is_endangered or False
        self.animals_total = ["cheetah","lion","zebra","giraffe"]

    def make_sound(self):
        pass
        # print(f" Animal {self.name}")

    def eat(self):
        print(f"{self.name} ест {food}.")

    def sleep(self):
        print(f"{self.name} спит.")


class Cheetah(Animal):
    def __init__(self, name, species, age, speed, is_endangered=None):
        super().__init__(self, name, species, age, is_endangered)
        self.speed = speed

    def make_sound(self):
        super().make_sound(f" Animal {self.species} is making a sound HHHHRRRRRR")

    def hunting(self):
        print(f'{self.species} named {self.name} is hunting')

class Lion(Animal):
    def __init__(self, name, species, age, is_endangered=None):
        super().__init__(self, name, species, is_endangered)
        self.age = age

    def make_sound(self):
        super().make_sound(f" Lion named {self.name} is making a sound HHHHRRRRRR")

    def __str__(self):
        return {self.name}

class Zebra(Animal):
    def __init__(self, name, species, age, is_endangered=None):
        super().__init__(name, species, age, is_endangered)
        self.has_stripes = True

    def make_sound(self):
        print(f"{self.species} with name {self.name} is making this sound: ffffffaaaarrr")

    def run_from_lion(self, lion_obj: Lion):
        print(f"Zebra with name {self.name} is running from {lion_obj.name}")
        lion_obj.hunting()


class Giraffe(Animal):
    def __init__(self, name, species, age, is_endangered=None):
        super().__init__(name, species, age, is_endangered)
        self.neck_length = 2

    def make_sound(self):
        print(f"{self.species} with name {self.name} is making this sound: dhdshdgy")

    def cures_other_animal(self, animal_obj: Animal):
        print(f'{self.name} is curing {animal_obj.name} the {animal_obj.species}')
        animal_obj.make_sound()


class Employees:
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age

    def report(self):
        print(f"Employee with the name  {self.name} is making a report")

class Zookeeper(Employees):
    def work(self, exhibits):
        print(f"Zookeeper {self.name} is feeding the animals.")
        for exhibit in exhibits:
            for animal in exhibit.animals_list:
                animal.eat("Еда для животных")

class Vet(Employees):
    def work(self, exhibits):
        print(f"Vet named {self.name} is checking the health of animals")
        for exhibit in exhibits:
            for animal in exhibit.animals_list:
                print(f"Проверка здоровья {animal.name} ({animal.species}).")



class Exhibit:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals_list = []
        self.employee_list = []

    def add_employee(self, employee_obj: Employees):
        self.employee_list.append(employee_obj.name)
        print(f"{employee_obj.name} is added to the Exhibit {self.name} as {employee_obj.position}")

    def remove_employee(self, employee_obj: Employees):
        if employee_obj in self.employee_list:
            self.animals_list.remove(employee_obj.name)
        else:
            print(f"There is no {employee_obj.name} working at the exhibit {self.name}")

    def add_animal(self, animal_obj: Animal):
        self.animals_list.append(animal_obj.name)
        print(f'{animal_obj.species} with {animal_obj.name} is added to Exhibit {self.name} at {self.location}')

    def remove_animal(self, animal_obj: Animal):
        if animal_obj in self.animals_list:
            self.animals_list.remove(animal_obj)
        else:
            print(f"There is no {animal_obj.name} in the exhibit {self.name}")

    def show_animal(self):
        for animal in self.animals_list:
            print(animal, end=", ")

class Zoo:
    def __init__(self):
        self.exhibit = []
        self.employees = []
    def add_exhibit(self, name, location):
        exhibit = Exhibit(name, location)
        self.exhibit.append(exhibit)
        print(f"Exhibit with name {exhibit.name} is added to ZOO")

    def add_employees(self, name, position, age):
        if position.lower() == "zookeeper":
            staff_member = Zookeeper(name, position, age)
        elif position.lower() == "vet":
            staff_member = Vet(name, position, age)
        else:
            print("No position allowed. Staff is not added")
            return
        self.employees.append(staff_member)
        print(f"Staff member with name {staff_member.name} is added to ZOO as {staff_member.position}")

    def show_all_exhibits(self):
        for exhibit in self.exhibit:
            print(f"Вольер: {exhibit.name} | Местоположение: {exhibit.location}")
            exhibit.show_animal()

    def daily_operations(self):
        for staff_member in self.employees:
            staff_member.work(self.exhibit)

    def add_animal_to_exhibit(self, exhibit_obj: Exhibit, animal_obj):
        if animal_obj.name in exhibit_obj.animals_list:
            print("Animal is already there")
        else:
            exhibit_obj.animals_list.append(animal_obj)
            print(f"Animal with the name {animal_obj} is added to Exhibit {exhibit_obj.name}")





