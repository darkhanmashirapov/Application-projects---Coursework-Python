from zoo import Zoo, Lion, Cheetah, Zebra, Giraffe
from zoo import Exhibit
def main():
    zoo = Zoo()

    while True:
        print("\nДобро пожаловать в зоопарк!")
        print("1. Добавить вольер")
        print("2. Добавить сотрудника")
        print("3. Добавить животное в вольер, cheetah/lion/zebra/giraffe")
        print("4. Показать все вольеры")
        print("5. Ежедневные операции")
        print("6. Add animal")
        print("7. Выйти")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            name = input("Введите название вольера: ")
            location = input("Введите местоположение вольера: ")
            zoo.add_exhibit(name, location)

        elif choice == "2":
            name = input("Введите имя сотрудника: ")
            position = input("Введите должность (Zookeeper/Vet): ")
            age = int(input("Введите возраст сотрудника: "))
            zoo.add_employees(name, position, age)

        elif choice == "3":
            exhibit_name = Exhibit(input("Введите название вольера: "), input("Введите название вольера: "))
            animal_name = input("Введите имя животного: ")
            while True:
                species = input("Введите вид животного: cheetah/lion/zebra/giraffe ")
                if species.lower()=="cheetah" or species.lower()=="lion" or species.lower()=="zebra" or species.lower()=="giraffe":
                    age = int(input("Введите возраст животного: "))
                    is_endangered = input("Под угрозой исчезновения? (yes/no): ").lower() == "yes"
                    if species.lower() == "lion":
                        animal = Lion(animal_name, species, age, is_endangered)
                    elif species.lower() == "cheetah":
                        animal = Cheetah(animal_name, species, age, is_endangered)
                    elif species.lower() == "giraffe":
                        animal = Giraffe(animal_name, species, age, is_endangered)
                    else:
                        print("Неизвестный вид животного.")
                        continue
                    zoo.add_animal_to_exhibit(exhibit_name, animal)
                    break
                else:
                    print("Incorrect animal, that animal cannot be added")



        elif choice == "4":
            zoo.show_all_exhibits()

        elif choice == "5":
            zoo.daily_operations()

        elif choice == "6":
            return

        elif choice == "7":
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
