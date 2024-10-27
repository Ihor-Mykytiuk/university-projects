import sys, random
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from lab6.ui.task3_interface import Ui_MainWindow
from lab6.utils.data_structures import DLinkedList, DNode


class ExtendedDLinkedList(DLinkedList):
    def __init__(self):
        super().__init__()

    def count(self, first, last, value):
        """Підраховує кількість входжень значення value в діапазоні позицій від first до last"""
        if first < 0 or last < 0:
            raise ValueError("Позиції мають бути додатніми числами.")
        if first > last:
            raise ValueError("Позиція first має бути меншою за last.")
        if self.head is None:
            raise ValueError("Список порожній.")
        current = self.head
        count = 0
        for i in range(last + 1):
            if i >= first and current.data == value:
                count += 1
            current = current.next
            if current is None:
                break
        return count

    def reverse(self, first, last):
        """Реверсує підсписок від позиції first до last"""
        if first < 0 or last < 0:
            raise ValueError("Позиції мають бути додатніми числами.")
        if first > last:
            raise ValueError("Позиція first має бути меншою за last.")
        if self.head is None:
            raise ValueError("Список порожній.")
        current = self.head
        for i in range(first):
            if current is None:
                raise ValueError("Позиція first виходить за межі списку.")
            current = current.next
        if current is None:
            raise ValueError("Позиція first виходить за межі списку.")
        first_node = current
        for i in range(last - first):
            if current is None:
                raise ValueError("Позиція last виходить за межі списку.")
            current = current.next
        if current is None:
            raise ValueError("Позиція last виходить за межі списку.")

        last_node = current
        while first_node != last_node and first_node.prev != last_node:
            first_node.data, last_node.data = last_node.data, first_node.data
            first_node = first_node.next
            last_node = last_node.prev

    def iter_swap(self, first, last):
        """Міняє місцями значення елементів списку в позиціях first та last"""
        if first < 0 or last < 0:
            raise ValueError("Позиції мають бути додатніми числами.")
        if first > last:
            raise ValueError("Позиція first має бути меншою за last.")
        if self.head is None:
            raise ValueError("Список порожній.")
        current = self.head
        for i in range(last + 1):
            if i == first:
                first_node = current
            if i == last:
                last_node = current
            current = current.next
            if current is None:
                break
        if current is None:
            raise ValueError("Позиція last виходить за межі списку.")
        first_node.data, last_node.data = last_node.data, first_node.data


class LinkedListOperationsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.list = ExtendedDLinkedList()

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
        self.ui.comboBox_select_operation.currentIndexChanged.connect(self.change_layout)
        self.ui.pushButton_execute_operation.clicked.connect(self.execute_operation)

    def show_list(self):
        """Відображення списку"""
        self.ui.label_result_list.clear()
        self.ui.label_result_list.setText(str(self.list))

    def generate_list(self):
        """Генерація випадкового списку на основі введеної кількості елементів"""
        self.list.clear()
        size = self.ui.input_size.text()
        for i in range(int(size)):
            self.list.append(random.randint(1, 100))
        self.show_list()

    def change_layout(self):
        """Змінює кількість полів для введення залежно від обраної операції"""
        operation = self.ui.comboBox_select_operation.currentText()
        if operation == "count":
            self.ui.input_first.setVisible(True)
            self.ui.input_last.setVisible(True)
            self.ui.input_value.setVisible(True)
        if operation == "reverse":
            self.ui.input_first.setVisible(True)
            self.ui.input_last.setVisible(True)
            self.ui.input_value.setVisible(False)
        if operation == "iter_swap":
            self.ui.input_first.setVisible(True)
            self.ui.input_last.setVisible(True)
            self.ui.input_value.setVisible(False)

    def execute_operation(self):
        """Виконує обрану операцію"""
        operation = self.ui.comboBox_select_operation.currentText()
        first = self.ui.input_first.text()
        last = self.ui.input_last.text()

        if not first or not last:
            self.show_message("Помилка: Позиції не вказані.", is_error=True)
            return
        try:
            first = int(first)
            last = int(last)
        except ValueError:
            self.show_message("Помилка: Позиції мають бути цілими числами.", is_error=True)
            return
        if operation == "count":
            value = self.ui.input_value.text()
            if not value:
                self.show_message("Помилка: Значення не вказане.", is_error=True)
                return
            try:
                count = self.list.count(first, last, int(value))
                self.show_message(f"Кількість входжень: {count}")
            except ValueError as e:
                self.show_message(f"Помилка: {str(e)}", is_error=True)

        if operation == "reverse":
            try:
                self.list.reverse(first, last)
                self.show_list()
                self.show_message("Елементи успішно переставлені у зворотньому порядку")
            except ValueError as e:
                self.show_message(f"Помилка: {str(e)}", is_error=True)
        if operation == "iter_swap":
            try:
                self.list.iter_swap(first, last)
                self.show_list()
                self.show_message("Елементи успішно переставлені місцями")
            except ValueError as e:
                self.show_message(f"Помилка: {str(e)}", is_error=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinkedListOperationsApp()
    window.show()
    sys.exit(app.exec())
