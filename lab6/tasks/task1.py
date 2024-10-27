import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from lab6.ui.task1_interface import Ui_Form
from llist import sllist, sllistnode, sllistiterator, sllistnodeiterator


class ListManipulator(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Ініціалізуємо інтерфейс
        self.ui.setupUi(self)

        # Список для роботи
        self.list = sllist()

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
        """Генерація списку"""
        self.list.clear()
        size = self.ui.input_size.text()
        for i in range(int(size)):
            self.list.append(sllistnode(random.randint(1, 100)))
        self.show_list()

    def show_list(self):
        """Відображення списку"""
        self.ui.label_result_list.clear()
        iterator = sllistiterator(self.list)
        try:
            # Перший елемент
            item = next(iterator)
            label_text = str(item)

            while True:
                item = next(iterator)
                label_text += " -> " + str(item)
        except StopIteration:
            self.ui.label_result_list.setText(label_text)

    def delete_elements(self):
        """Видалення елементів з позицій N по K"""
        n = int(self.ui.input_n.text())
        k = int(self.ui.input_k.text())

        if n < 0 or k > self.list.size or n >= k:
            self.show_message("Помилка: некоректні значення N та K", is_error=True)
            return

        current_node = self.list.nodeat(n)
        while current_node is not None and n < k:
            next_node = current_node.next
            self.list.remove(current_node)
            current_node = next_node
            n += 1
        self.show_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListManipulator()
    window.show()
    sys.exit(app.exec())
