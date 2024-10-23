import sys
import random
from collections import deque
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from lab6.ui.task2_interface import Ui_Form  # Імпортуй тут свій інтерфейс

class LinkedListSort(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Ініціалізуємо інтерфейс
        self.ui.setupUi(self)
        self.apply_styles()

        # Використовуємо deque для симуляції зв'язного списку
        self.linked_list = deque()

        # Підключення сигналів до функцій
        self.ui.create_list_button.clicked.connect(self.generate_linked_list)
        self.ui.sort_button.clicked.connect(self.sort_list)

    def apply_styles(self):
        """Застосування стилів з файлу CSS"""
        with open("static/styles/styles.qss", "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def generate_linked_list(self):
        """Генеруємо випадковий зв'язний список на основі введеної кількості елементів"""
        try:
            size = int(self.ui.size_input.text())
            if size <= 0:
                raise ValueError
            # Генеруємо випадковий зв'язний список
            self.linked_list = deque(random.randint(1, 100) for _ in range(size))
            self.display_list(self.linked_list)
            self.display_message("Список згенеровано!")
        except ValueError:
            self.display_message("Будь ласка, введіть дійсну кількість елементів!", error=True)

    def sort_list(self):
        """Сортування зв'язного списку за спаданням"""
        if not self.linked_list:
            QMessageBox.warning(self, "Помилка", "Спочатку згенеруйте список.")
            return

        # Перетворюємо deque у звичайний список, сортуємо його і знову перетворюємо в deque
        sorted_list = deque(sorted(self.linked_list, reverse=True))

        # Оновлюємо наш deque і відображаємо відсортований список
        self.linked_list = sorted_list
        self.display_list(self.linked_list)
        self.display_message("Список відсортовано за спаданням!")

    def display_list(self, linked_list):
        """Відображає список у QLabel"""
        self.ui.list_result.setText(", ".join(map(str, linked_list)))

    def display_message(self, message, error=False):
        """Виводить повідомлення у QLabel для статусу. Якщо помилка - виділяємо червоним"""
        if error:
            self.ui.status_label.setStyleSheet("color: red;")
        else:
            self.ui.status_label.setStyleSheet("color: green;")
        self.ui.status_label.setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinkedListSort()
    window.show()
    sys.exit(app.exec())
