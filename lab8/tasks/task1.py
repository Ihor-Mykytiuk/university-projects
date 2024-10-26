import sys, random
from PySide6.QtWidgets import QMainWindow, QApplication
from lab8.utils.data_structures import Stack
from lab8.ui.task1_interface import Ui_MainWindow


class StackProcessor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stack = Stack()

        # Налаштування зв'язків кнопок
        self.setup_connections()

        # Застосування стилів
        self.apply_styles("static/styles/styles.qss")

    def apply_styles(self, style_file_path):
        """Застосування стилів з файлу CSS"""
        with open(style_file_path, "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def show_message(self, message, is_error=False):
        """Відображення повідомлення"""
        color = "red" if is_error else "green"
        self.ui.label_status.setStyleSheet(f"color: {color};")
        self.ui.label_status.setText(message)

    def setup_connections(self):
        """Налаштування зв'язків кнопок"""
        self.ui.pushButton_create_stack.clicked.connect(self.create_stack)
        self.ui.pushButton_process_stack.clicked.connect(self.process_stack)

    def create_stack(self):
        """Створення стека з 10 випадкових чисел"""
        self.stack = Stack()
        for _ in range(10):
            random_integer = random.randint(-10, 10)
            self.stack.push(random_integer)

        self.ui.label_status.setText("Stack created.")
        self.update_stack_label()

    def process_stack(self):
        """Заміна всіх позитивних значень на 1, а негативних на -1"""
        temp_stack = Stack()
        while not self.stack.is_empty():
            value = self.stack.pop()
            if value > 0:
                temp_stack.push(1)
            else:
                temp_stack.push(-1)

        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop())

        self.update_stack_label()

    def update_stack_label(self):
        """Оновлення відображення стека"""
        self.ui.label_stack_result.clear()
        if self.stack.is_empty():
            self.show_message("Помилка: стек порожній.", is_error=True)
            return

        temp_stack = Stack()
        output_str = ""
        while not self.stack.is_empty():
            value = self.stack.pop()
            output_str += str(value) + " -> "
            temp_stack.push(value)
        self.ui.label_stack_result.setText(output_str)
        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StackProcessor()
    window.show()
    sys.exit(app.exec())
