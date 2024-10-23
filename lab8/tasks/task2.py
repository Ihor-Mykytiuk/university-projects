import sys
import random
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from lab8.utils.data_structures import Queue  # Переконайся, що в тебе є реалізація черги
from lab8.ui.task2_interface import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.queue = Queue()

        # З'єднуємо кнопки з функціями
        self.ui.pushButton_create_queue.clicked.connect(self.create_queue)
        self.ui.pushButton_process_queue.clicked.connect(self.process_queue)

    def create_queue(self):
        # Створюємо чергу з 10 випадкових чисел
        self.queue = Queue()
        for _ in range(10):
            random_integer = random.randint(-10, 10)
            self.queue.enqueue(random_integer)

        self.ui.label_status.setText("Queue created.")
        self.update_queue_label()

    def process_queue(self):
        # Збільшуємо всі значення в черзі на максимальний елемент
        if self.queue.is_empty():
            self.ui.label_status.setText("Queue is empty. Cannot process.")
            return

        temp_queue = Queue()  # Тимчасова черга для зберігання значень
        max_value = None  # Змінна для зберігання максимального значення

        # Знаходимо максимальний елемент
        while not self.queue.is_empty():
            value = self.queue.dequeue()
            if max_value is None or value > max_value:
                max_value = value  # Оновлюємо максимальне значення
            temp_queue.enqueue(value)  # Поміщаємо значення в тимчасову чергу

        # Збільшуємо значення на максимальний елемент і зберігаємо в нову чергу
        while not temp_queue.is_empty():
            value = temp_queue.dequeue()
            new_value = value + max_value
            self.queue.enqueue(new_value)  # Поміщаємо нове значення назад у чергу

        self.update_queue_label()
        self.ui.label_status.setText("Values processed.")

    def update_queue_label(self):
        self.ui.label_queue.clear()
        if self.queue.is_empty():
            self.ui.label_queue.setText("Queue is empty")
        else:
            temp_queue = Queue()
            output_str = ""

            # Витягуємо значення з основної черги
            while not self.queue.is_empty():
                value = self.queue.dequeue()
                output_str += str(value) + " -> "
                temp_queue.enqueue(value)  # Зберігаємо значення в тимчасовій черзі

            self.ui.label_queue.setText(output_str)  # Відображаємо значення

            # Повертаємо значення назад у основну чергу
            while not temp_queue.is_empty():
                self.queue.enqueue(temp_queue.dequeue())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
