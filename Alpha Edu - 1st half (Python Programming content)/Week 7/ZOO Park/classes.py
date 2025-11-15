class Animal:

    def __init__(self, name: str, species: str, age:int, is_endangered=None): # When none we can just not do anything
        self.name = name
        self.species = species
        self.age = age
        self.is_endangered = is_endangered or False

    def make_sound(self):
        pass
        # print(f"{self.name} - {self.species} - MAKES THIS SOUND === {sound}")

    def eat(self, food:str):
        pass
        # print(f"{self.species} is eating {food} and his name is {self.name}")

    def sleep(self):
        pass
        # print(f"{self.name} - {self.species} is sleeping")

class Cheetah(Animal):
    def __init__(self, name, species, age, speed, is_endangered=None): # NOT NECESSESARY VARIABLE IS AT THE END
        super().__init__(name, species, age, is_endangered)
        self.speed = speed

    def make_sound(self):
        super().make_sound("Arrrrhhhhhh")

    def hunting(self):
        print("Cheetah is hunting")

class Lion(Animal):
    def __int__(self, name, species, age, is_endangered=None):
        super().__init__(name, species, age, is_endangered)
        self.speed = 80 #unique parameter

    def make_sound(self):
        print(f"{self.name} is making Prrrr sound")

    def hunting(self):
        print(f"{self.species} with name {self.name}  is hunting")
#     def test_display(self):
#         print(self.name)
#         print(self.species)
#         print(self.age)
#         print(self.is_endangered)
    def __str__(self):
        return f"{self.name}, {self.species}, {self.age}"

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

# test_animal_class = Animal("Simba", "Lion", "3", is_endangered=True)
# test_lion_object2 = Lion("Simba", "Lion", "3", is_endangered=True)
# test_lion_object = Lion("Alex", "Lion", "15")
# test_zebra_object = Zebra("Dark", "Zebra", "4")

# test_giraffe_object = Giraffe("Melman", "Giraffe", 4)
# test_giraffe_object.cures_other_animal(test_lion_object2)
# test_giraffe_object.cures_other_animal(test_zebra_object)
# test_giraffe_object.cures_other_animal(test_animal_class)
#
# test_zebra_object.run_from_lion(test_lion_object)

# test_lion_object.hunting()
# test_lion_object.make_sound()
# test_lion_object 2.hunting()
# test_lion_object2.make_sound()
# test_lion_object.test_display()
# test_lion_object2.test_display()


class Exhibit:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals_list = []

    def add_animal(self, animal_obj: Animal):
        self.animals_list.append(animal_obj)
        print(f"{animal_obj.species} with name  {animal_obj.name} is added to Exhibit {self.name}")

    def remove_animal(self, animal_obj: Animal):
        if animal_obj in self.animals_list:
            self.animals_list.remove(animal_obj)
        else:
            print("No animals found! Error")

    def show_animal(self):
        for animal in self.animals_list:
            print(animal)


class Staff:
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age

    def work(self, exhibits):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе.")

    def report(self):
        print(f"Сотрудник {self.name} составляет отчет.")


class Zookeeper(Staff):
    def work(self, exhibits):
        print(f"Смотритель {self.name} кормит животных.")
        for exhibit in exhibits:
            for animal in exhibit.animals_list:
                animal.eat("Еда для животных")


class Vet(Staff):
    def work(self, exhibits):
        print(f"Ветеринар {self.name} проверяет здоровье животных.")
        for exhibit in exhibits:
            for animal in exhibit.animals_list:
                print(f"Проверка здоровья {animal.name} ({animal.species}).")


class Zoo:
    def __init__(self):
        self.exhibits = []
        self.staff = []

    def add_exhibit(self, name, location):
        exhibit = Exhibit(name, location)
        self.exhibits.append(exhibit)
        print(f"Вольер '{name}' добавлен.")

    def add_staff(self, name, position, age):
        if position.lower() == "zookeeper":
            staff_member = Zookeeper(name, position, age)
        elif position.lower() == "vet":
            staff_member = Vet(name, position, age)
        else:
            print("Неизвестная должность. Сотрудник не добавлен.")
            return
        self.staff.append(staff_member)
        print(f"Сотрудник '{name}' добавлен в должности '{position}'.")

    def add_animal_to_exhibit(self, exhibit_name, animal):
        exhibit = next((ex for ex in self.exhibits if ex.name == exhibit_name), None)
        if exhibit:
            exhibit.add_animal(animal)
        else:
            print(f"Вольер '{exhibit_name}' не найден.")

    def show_all_exhibits(self):
        for exhibit in self.exhibits:
            print(f"Вольер: {exhibit.name} | Местоположение: {exhibit.location}")
            exhibit.show_animal()

    def daily_operations(self):
        for staff_member in self.staff:
            staff_member.work(self.exhibits)









