import sys, random
from PySide6.QtWidgets import QMainWindow, QApplication
from lab8.utils.data_structures import Queue
from lab8.ui.task2_interface import Ui_MainWindow


class QueueProcessor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.queue = Queue()

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
        self.ui.pushButton_create_queue.clicked.connect(self.create_queue)
        self.ui.pushButton_process_queue.clicked.connect(self.process_queue)

    def create_queue(self):
        """Створення черги з 10 випадкових чисел"""
        self.queue = Queue()
        for _ in range(10):
            random_integer = random.randint(-10, 10)
            self.queue.enqueue(random_integer)

        self.show_message("Черга створена успішно.")
        self.update_queue_label()

    def process_queue(self):
        """Збільшення кожного значення на максимальне значення у черзі"""
        if self.queue.is_empty():
            self.show_message("Помилка: черга порожня.", is_error=True)
            return

        temp_queue = Queue()
        max_value = None

        while not self.queue.is_empty():
            value = self.queue.dequeue()
            if max_value is None or value > max_value:
                max_value = value
            temp_queue.enqueue(value)

        while not temp_queue.is_empty():
            value = temp_queue.dequeue()
            new_value = value + max_value
            self.queue.enqueue(new_value)

        self.update_queue_label()
        self.show_message("Чергу оброблено успішно.")

    def update_queue_label(self):
        """Оновлення відображення черги"""
        self.ui.label_queue_result.clear()
        if self.queue.is_empty():
            self.show_message("Помилка: черга порожня.", is_error=True)
            return

        temp_queue = Queue()
        output_str = ""

        while not self.queue.is_empty():
            value = self.queue.dequeue()
            output_str += str(value) + " -> "
            temp_queue.enqueue(value)

        self.ui.label_queue_result.setText(output_str)

        while not temp_queue.is_empty():
            self.queue.enqueue(temp_queue.dequeue())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QueueProcessor()
    window.show()
    sys.exit(app.exec())
