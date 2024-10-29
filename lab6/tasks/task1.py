import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from lab6.utils.data_structures import SLinkedList
from lab6.ui.task1_interface import Ui_MainWindow


class ListManipulatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Однозв'язний список
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
        self.ui.pushButton_delete_elements.clicked.connect(self.delete_elements)

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

    def show_list(self):
        """Відображення списку"""
        self.ui.label_result_list.clear()
        self.ui.label_result_list.setText(str(self.list))


    def delete_elements(self):
        """Видалення елементів з позицій N по K"""
        n = int(self.ui.input_n.text())
        k = int(self.ui.input_k.text())

        if n < 0 or k < 0:
            self.show_message("Помилка: Некоректні дані.", is_error=True)
            return
        if n >= k:
            self.show_message("Помилка: Позиція N має бути менша за K.", is_error=True)
            return

        current = self.list.head
        for i in range(n - 1):
            if current.next is None:
                self.show_message("Помилка: Позиція N виходить за межі списку.", is_error=True)
                return
            current = current.next
        node1 = current

        for i in range(k - n + 1):
            if current.next is None:
                self.show_message("Помилка: Позиція K виходить за межі списку.", is_error=True)
                return
            current = current.next
        node2 = current

        node1.next = node2.next
        self.show_list()
        self.show_message("Елементи успішно видалені.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListManipulatorApp()
    window.show()
    sys.exit(app.exec())
