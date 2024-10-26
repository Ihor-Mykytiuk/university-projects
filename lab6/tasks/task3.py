import random
from collections import deque

class LinkedList:
    def __init__(self):
        self.linked_list = deque()

    def fill_with_random_values(self, size):
        """Заповнення двозв'язного списку випадковими значеннями."""
        self.linked_list = deque(random.randint(1, 10) for _ in range(size))
        return list(self.linked_list)

    def count_value(self, value):
        """Підрахунок кількості входжень значення у список."""
        return self.linked_list.count(value)

    def reverse_list(self):
        """Переворот списку в зворотному порядку."""
        self.linked_list.reverse()
        return list(self.linked_list)

    def iter_swap(self, index1, index2):
        """Обмін значень між двома індексами списку."""
        if 0 <= index1 < len(self.linked_list) and 0 <= index2 < len(self.linked_list):
            self.linked_list[index1], self.linked_list[index2] = self.linked_list[index2], self.linked_list[index1]
            return list(self.linked_list)
        else:
            raise IndexError("Неправильні індекси.")

class UserInterface:
    def __init__(self):
        self.project = LinkedList()

    @staticmethod
    def display_menu():
        """Відображення меню."""
        print("\nМеню:")
        print("1. Заповнити список випадковими значеннями")
        print("2. Підрахувати значення у списку")
        print("3. Перевернути список")
        print("4. Обміняти значення між двома позиціями")
        print("5. Вийти")

    @staticmethod
    def get_choice():
        """Отримання вибору користувача."""
        return input("Виберіть опцію (1-5): ")

    def handle_choice(self, choice):
        """Обробка вибору користувача."""
        if choice == '1':
            size = int(input("Введіть розмір списку: "))
            generated_list = self.project.fill_with_random_values(size)
            print("Згенерований список:", generated_list)
        elif choice == '2':
            value = int(input("Введіть значення для підрахунку: "))
            count = self.project.count_value(value)
            print(f"Значення {value} зустрічається {count} разів.")
        elif choice == '3':
            reversed_list = self.project.reverse_list()
            print("Список після перевороту:", reversed_list)
        elif choice == '4':
            index1 = int(input("Введіть перший індекс: "))
            index2 = int(input("Введіть другий індекс: "))
            try:
                swapped_list = self.project.iter_swap(index1, index2)
                print(f"Список після обміну значень на індексах {index1} і {index2}: {swapped_list}")
            except IndexError as e:
                print(e)
        elif choice == '5':
            print("Вихід з програми.")
            return False
        else:
            print("Неправильний вибір, спробуйте ще раз.")
        return True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinkedListSort()
    window.show()
    sys.exit(app.exec())