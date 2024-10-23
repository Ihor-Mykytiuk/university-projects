import sys
import random
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from lab8.utils.data_structures import Stack
from lab8.ui.task1_interface import Ui_MainWindow

class StackProcessor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stack = Stack()

        # З'єднуємо кнопки з функціями
        self.ui.pushButton_create_stack.clicked.connect(self.create_stack)
        self.ui.pushButton_process_stack.clicked.connect(self.process_stack)

    def create_stack(self):
        # Створюємо стек з 10 випадкових чисел
        self.stack = Stack()
        for _ in range(10):
            random_integer = random.randint(-10, 10)
            self.stack.push(random_integer)

        self.ui.label_status.setText("Stack created.")
        self.update_stack_label()

    def process_stack(self):
        # Заміщуємо позитивні та негативні значення в стеку
        temp_stack = Stack()  # Використовуємо стек замість списку
        while not self.stack.is_empty():
            value = self.stack.pop()  # Витягуємо значення з стека
            if value > 0:
                temp_stack.push(1)  # Заміщуємо на 1, якщо значення позитивне
            else:
                temp_stack.push(-1)  # Заміщуємо на -1, якщо значення негативне

        # Поміщаємо оброблені значення назад у стек
        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop())

        self.update_stack_label()
        self.ui.label_status.setText("Values processed.")

    def update_stack_label(self):
        self.ui.label_stack.clear()
        if self.stack.is_empty():
            self.ui.label_stack.setText("Stack is empty")
        else:
            temp_stack = Stack()
            output_str = ""
            while not self.stack.is_empty():
                value = self.stack.pop()
                output_str += str(value) + " -> "
                temp_stack.push(value)
            self.ui.label_stack.setText(output_str)
            while not temp_stack.is_empty():
                self.stack.push(temp_stack.pop())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StackProcessor()
    window.show()
    sys.exit(app.exec())
