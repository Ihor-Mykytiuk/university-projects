import sys
import numpy as np
from PySide6.QtWidgets import QApplication
from lab5.ui.task1_interface import Ui_Form
from base_widget import BaseWidget

class ArrayTransform(BaseWidget):
    def __init__(self):
        super().__init__(Ui_Form)

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
        """Функція для перетворення масиву за умовою (додаємо перший елемент до парних, крім першого й останнього)"""
        if not self.array:
            self.display_message("Помилка: спочатку створіть масив.", error=True)
            return
        first_element = self.array[0]

        # Створюємо новий масив, де парні елементи змінюються
        transformed_array = [first_element]  # Перший елемент не змінюється

        # Перетворюємо всі елементи, крім першого й останнього
        for i in range(1, len(self.array) - 1):
            if self.array[i] % 2 == 0:  # Перевірка на парність
                transformed_array.append(self.array[i] + first_element)
            else:
                transformed_array.append(self.array[i])

        transformed_array.append(self.array[-1])  # Останній елемент не змінюється

        # Виводимо результат
        self.display_array(transformed_array)  # Використовуємо метод базового класу
        self.display_message("Масив успішно перетворено.")  # Використовуємо метод базового класу

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArrayTransform()
    window.show()
    sys.exit(app.exec())
