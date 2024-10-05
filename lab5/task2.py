import sys
import numpy as np
from PySide6.QtWidgets import QApplication
from lab5.ui.task2_interface import Ui_Form
from base_widget import BaseWidget

class ArraySort(BaseWidget):
    def __init__(self):
        super().__init__(Ui_Form)  # Викликаємо конструктор базового класу

        # Ініціалізуємо масив як порожній
        self.array = []

        # Підключення сигналів до функцій
        self.ui.create_array_button.clicked.connect(self.create_array)
        self.ui.transform_array_button.clicked.connect(self.transform_array)
        self.ui.size_input.textChanged.connect(self.size_input_changed)
        self.ui.array_input.textChanged.connect(self.array_input_changed)

    def size_input_changed(self):
        """Якщо користувач вводить розмір масиву, блокуємо поле для введення масиву."""
        if self.ui.size_input.text():
            self.ui.array_input.clear()
            self.ui.array_input.setDisabled(True)
        else:
            self.ui.array_input.setDisabled(False)

    def array_input_changed(self):
        """Якщо користувач вводить масив вручну, блокуємо поле для введення розміру."""
        if self.ui.array_input.text():
            self.ui.size_input.clear()
            self.ui.size_input.setDisabled(True)
        else:
            self.ui.size_input.setDisabled(False)

    def create_array(self):
        """Функція для створення масиву (вручну або випадково)"""
        if self.ui.size_input.text():
            size = int(self.ui.size_input.text())
            self.create_random_array(size)
        elif self.ui.array_input.text():
            str_array = self.ui.array_input.text()
            self.create_array_from_input(str_array)
        else:
            self.display_message("Помилка: заповніть хоча б одне поле.", error=True)

    def create_random_array(self, size):
        """Створює масив випадкових чисел."""
        try:
            if size < 2:
                raise ValueError
            self.array = np.random.randint(1, 101, size=size).tolist()  # Генеруємо випадковий масив
            self.display_array(self.array)  # Використовуємо метод базового класу
            self.display_message(f"Згенеровано масив розміру {size}.")  # Використовуємо метод базового класу
        except ValueError:
            self.display_message("Помилка: введіть дійсний розмір масиву (більше 1).", error=True)

    def create_array_from_input(self, str_array):
        """Створює масив з введених користувачем значень."""
        try:
            self.array = list(map(int, str_array.split()))
            if len(self.array) < 2:
                raise ValueError
            self.display_array(self.array)  # Використовуємо метод базового класу
            self.display_message("Масив успішно введений.")  # Використовуємо метод базового класу
        except ValueError:
            self.display_message("Помилка: введіть дійсний масив чисел (через пробіл).", error=True)

    def transform_array(self):
        """Перетворення масиву: спочатку парні, потім непарні елементи."""
        if not self.array:
            self.display_message("Помилка: спочатку створіть масив.", error=True)
            return

        even_elements = [x for x in self.array if x % 2 == 0]
        odd_elements = [x for x in self.array if x % 2 != 0]
        transformed_array = even_elements + odd_elements

        self.display_array(transformed_array)
        self.display_message("Масив перетворено!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArraySort()
    window.show()
    sys.exit(app.exec())
