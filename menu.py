import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
# Імпорти всіх завдання
from lab5.tasks import ArrayTransform, ArraySort, MatrixSum, MatrixTransform
from lab6.tasks import ListManipulator, LinkedListSort, LinkedList
from lab7.tasks import FileProcessor, FileSwapper
from lab8.tasks import StackProcessor, QueueProcessor, HospitalQueueSystem
from lab9.tasks import MapStudentApp, PhoneBook, ProductChecker
from lab10.calculator import Calculator

# Загальне меню для переходу по лабораторних і завданнях
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.task_window = None
        self.setWindowTitle('Головне меню лабораторних робіт')
        # Головний віджет та макет
        self.main_widget = QWidget()
        self.layout = QVBoxLayout()

        self.labs_data = {
            'Лабораторна робота №5': {
                'Завдання 1': ArrayTransform,
                'Завдання 2': ArraySort,
                'Завдання 3': MatrixSum,
                'Завдання 4': MatrixTransform,
            },
            'Лабораторна робота №6': {
                'Завдання 1': ListManipulator,
                'Завдання 2': LinkedListSort,
                'Завдання 3': LinkedList,
            },
            'Лабораторна робота №7': {
                'Завдання 1': FileProcessor,
                'Завдання 2': FileSwapper,
            },
            'Лабораторна робота №8': {
                'Завдання 1': StackProcessor,
                'Завдання 2': QueueProcessor,
                'Завдання 3': HospitalQueueSystem,
            },
            'Лабораторна робота №9': {
                'Завдання 1': MapStudentApp,
                'Завдання 2': PhoneBook,
                'Завдання 3': ProductChecker,
            },
            'Лабораторна робота №10': {
                'Калькулятор': Calculator,
            }
        }# Створюємо кнопки для лабораторних
        self.create_lab_buttons()

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def create_lab_buttons(self):
        """ Створюємо кнопки для лабораторних робіт динамічно. """
        self.clear_layout()

        for lab_name in self.labs_data.keys():
            button = QPushButton(lab_name)
            button.clicked.connect(lambda checked, lab=lab_name: self.show_tasks(lab))
            self.layout.addWidget(button)

    def show_tasks(self, lab_name):
        """ Відображаємо кнопки завдань для обраної лабораторної. """
        self.clear_layout()

        tasks = self.labs_data[lab_name]

        for task_name, task_class in tasks.items():
            button = QPushButton(task_name)
            button.clicked.connect(lambda checked, task=task_class: self.run_task(task))
            self.layout.addWidget(button)

        # Кнопка для повернення назад до списку лабораторних
        back_button = QPushButton('Назад')
        back_button.clicked.connect(self.create_lab_buttons)
        self.layout.addWidget(back_button)

    def clear_layout(self):
        """ Видаляє всі віджети з поточного макета. """
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def run_task(self, task_class):
        """ Запускає відповідне завдання. """
        self.task_window = task_class()
        self.task_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec())