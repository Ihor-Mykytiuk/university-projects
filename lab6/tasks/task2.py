import sys, random
from PySide6.QtWidgets import QApplication, QMainWindow
from lab6.utils.data_structures import SLinkedList
from lab6.ui.task2_interface import Ui_MainWindow


class LinkedListSortApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.list = SLinkedList()

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
        self.ui.pushButton_create_list.clicked.connect(self.generate_list)
        self.ui.pushButton_sort_list.clicked.connect(self.sort_list)

    def show_list(self):
        """Відображення списку"""
        self.ui.label_result_list.clear()
        self.ui.label_result_list.setText(str(self.list))

    def generate_list(self):
        """Генерація випадкового списку на основі введеної кількості елементів"""
        self.list.clear()
        size = self.ui.input_size.text()
        if not size:
            self.show_message("Помилка: Введіть кількість елементів.", is_error=True)
            return
        if int(size) <= 0:
            self.show_message("Помилка: Кількість елементів має бути більше 0.", is_error=True)
            return
        try:
            int(size)
        except ValueError:
            self.show_message("Помилка: Некоректні дані.", is_error=True)
            return
        for i in range(int(size)):
            self.list.append(random.randint(1, 100))
        self.show_list()
        self.show_message("Список успішно створено.")

    def sort_list(self):
        """Сортування зв'язного списку за спаданням"""
        if not self.list.head:
            self.show_message("Помилка: Список порожній.", is_error=True)
            return
        if self.list.head.next is None:
            self.show_message("Помилка: Список має тільки один елемент.", is_error=True)
            return

        is_sorted = False
        while not is_sorted:
            is_sorted = True
            current = self.list.head
            index = 0

            while current is not None and current.next is not None:
                next_node = current.next
                if current.data < next_node.data:
                    self.list.swap(index, index + 1)
                    is_sorted = False
                current = next_node
                index += 1
        self.show_list()
        self.show_message("Список успішно відсортовано.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinkedListSortApp()
    window.show()
    sys.exit(app.exec())
