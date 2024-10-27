import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
# Імпорти всіх завдання
from lab4.tasks import NumberDescriptionApp, VariableCheckApp, StudentLoginApp
from lab5.tasks import ArrayTransformApp, ArraySortApp, MatrixSumApp, MatrixTransformApp
from lab6.tasks import ListManipulatorApp, LinkedListSortApp, LinkedListOperationsApp
from lab7.tasks import FileProcessor, FileSwapper
from lab8.tasks import StackProcessor, QueueProcessor, HospitalQueueSystem
from lab9.tasks import MapStudentApp, ProductCheckerApp, PhoneBookApp
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
            'Лабораторна робота №4': {
                'Завдання 1': NumberDescriptionApp,
                'Завдання 2': VariableCheckApp,
                'Завдання 3': StudentLoginApp,
            },
            'Лабораторна робота №5': {
                'Завдання 1': ArrayTransformApp,
                'Завдання 2': ArraySortApp,
                'Завдання 3': MatrixSumApp,
                'Завдання 4': MatrixTransformApp,
            },
            'Лабораторна робота №6': {
                'Завдання 1': ListManipulatorApp,
                'Завдання 2': LinkedListSortApp,
                'Завдання 3': LinkedListOperationsApp,
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
                'Завдання 2': ProductCheckerApp,
                'Завдання 3': PhoneBookApp,
            },
            'Лабораторна робота №10': {
                'Калькулятор': Calculator,
            }
        }# Створюємо кнопки для лабораторних
        self.create_lab_buttons()

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        self.apply_styles("static/styles/styles.qss")

    def create_lab_buttons(self):
        """Створюємо кнопки для лабораторних робіт динамічно"""
        self.clear_layout()

        for lab_name in self.labs_data.keys():
            button = QPushButton(lab_name)
            button.clicked.connect(lambda checked, lab=lab_name: self.show_tasks(lab))
            self.layout.addWidget(button)

    def apply_styles(self, style_file_path):
        """Застосування стилів з файлу CSS"""
        with open(style_file_path, "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def show_tasks(self, lab_name):
        """Відображаємо кнопки завдань для обраної лабораторної"""
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
        """Видаляє всі віджети з поточного макета"""
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def run_task(self, task_class):
        """Запускає відповідне завдання"""
        self.task_window = task_class()
        self.task_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec())