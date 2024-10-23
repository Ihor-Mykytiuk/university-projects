import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from lab6.ui.task1_interface import Ui_Form  # Імпортуй тут свій інтерфейс
from llist import sllist, sllistnode, sllistiterator


class ListManipulator(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Ініціалізуємо інтерфейс
        self.ui.setupUi(self)
        self.apply_styles()

        # Список для роботи
        self.list = sllist()

        # Налаштування зв'язків кнопок
        self.ui.create_array_button.clicked.connect(self.generate_list)
        self.ui.delete_button.clicked.connect(self.delete_elements)


    def apply_styles(self):
        """Застосування стилів з файлу CSS"""
        with open("../../static/styles/styles.qss", "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def generate_list(self):
        """Генерація списку"""
        self.list.clear()
        size = self.ui.size_input.text()
        for i in range(int(size)):
            self.list.append(sllistnode(random.randint(1, 100)))
        self.show_list()

    def show_list(self):
        """Відображення списку"""
        self.ui.array_result.clear()
        iterator = sllistiterator(self.list)
        try:
            while True:
                item = next(iterator)
                label_text = self.ui.array_result.text() + str(item) + " -> "
                self.ui.array_result.setText(label_text)
        except StopIteration:
            pass


    def delete_elements(self):
        """Видалення елементів з позицій N по K"""
        n = int(self.ui.n_input.text())
        k = int(self.ui.k_input.text())

        if n < 0 or k > self.list.size or n >= k:
            QMessageBox.critical(self, "Помилка", "Неправильно вказані індекси!")
            return



        self.show_list()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListManipulator()
    window.show()
    my_list = sllist([1, 2, 3, 4, 5])
    my_list2 = [1, 2, 3, 4, 5]
    iterator = sllistiterator(my_list)
    iterator2 = iter(my_list2)
    while True:
        try:
            node = next(iterator)  # Отримуємо наступний вузол
            print(node)  # Виведе значення вузла
        except StopIteration:
            print("End of list")
            break  # Виходимо з циклу, коли досягнуто кінця списку

    sys.exit(app.exec())
