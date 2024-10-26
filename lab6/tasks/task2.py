import random
import sys
from PySide6.QtWidgets import QApplication, QWidget
from lab6.ui.task2_interface import Ui_Form


class LinkedListSort(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.linked_list = deque()

        # Налаштування зв'язків кнопок
        self.setup_connections()

        # Застосування стилів
        self.apply_styles()

    def apply_styles(self):
        """Застосування стилів з файлу CSS"""
        with open("static/styles/styles.qss", "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def show_message(self, message, is_error=False):
        """Відображення повідомлення"""
        color = "red" if is_error else "green"
        self.ui.label_status.setStyleSheet(f"color: {color};")
        self.ui.label_status.setText(message)

    def setup_connections(self):
        """Налаштування зв'язків кнопок"""
        self.ui.pushButton_create_list.clicked.connect(self.generate_linked_list)
        self.ui.pushButton_sort.clicked.connect(self.sort_list)

    def generate_linked_list(self):
        """Генеруємо випадковий зв'язний список на основі введеної кількості елементів"""
        try:
            size = int(self.ui.size_input.text())
            if size <= 0:
                raise ValueError
            # Генеруємо випадковий зв'язний список
            self.linked_list = deque(random.randint(1, 100) for _ in range(size))
            self.display_list(self.linked_list)
            self.show_message("Список згенеровано успішно")
        except ValueError:
            self.show_message("Помилка: Введіть коректне значення для розміру списку", is_error=True)

    def sort_list(self):
        """Сортування зв'язного списку за спаданням"""
        if not self.linked_list:
            self.show_message("Помилка: Список порожній", is_error=True)
            return

        sorted_list = deque(sorted(self.linked_list, reverse=True))

        self.linked_list = sorted_list
        self.display_list(self.linked_list)
        self.show_message("Список відсортовано успішно")

    def display_list(self, linked_list):
        """Відображає список у QLabel"""
        self.ui.label_result_list.setText(", ".join(map(str, linked_list)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinkedListSort()
    window.show()
    sys.exit(app.exec())
