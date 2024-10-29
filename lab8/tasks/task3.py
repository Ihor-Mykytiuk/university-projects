import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton,
                               QGroupBox, QMainWindow, QGridLayout)
from lab8.ui.task3_interface import Ui_MainWindow
from lab8.utils.data_structures import Queue


class HospitalQueueSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Список лікарів і черги пацієнтів
        self.doctors = {
            "Терапевт": {
                "queue": Queue(),
                "list": QListWidget(),
                "indicator": QLabel()
            },
            "Стоматолог": {
                "queue": Queue(),
                "list": QListWidget(),
                "indicator": QLabel()
            },
            "Кардіолог": {
                "queue": Queue(),
                "list": QListWidget(),
                "indicator": QLabel()
            },
            "Хірург": {
                "queue": Queue(),
                "list": QListWidget(),
                "indicator": QLabel()
            },
            "Офтальмолог": {
                "queue": Queue(),
                "list": QListWidget(),
                "indicator": QLabel()
            },
            "Дерматолог": {
                "queue": Queue(),
                "list": QListWidget(),
                "indicator": QLabel()
            },
        }

        self.MAX_QUEUE_SIZE = 10  # Максимум 10 пацієнтів в черзі до одного лікаря

        # Створення контейнера для контенту в QScrollArea
        self.scroll_content = QWidget()
        self.grid_layout = QGridLayout(self.scroll_content)
        self.scroll_content.setLayout(self.grid_layout)

        self.ui.scrollArea.setWidget(self.scroll_content)

        self.init_combobox_items()

        # Створення сітки лікарів та їх черг
        self.create_doctor_queues()

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
        self.ui.pushButton_add_patient.clicked.connect(self.add_patient)

    def init_combobox_items(self):
        """Додавання лікарів у випадаючий список"""
        for doctor in self.doctors:
            self.ui.comboBox_doctor_select.addItem(doctor)

    def create_doctor_queues(self):
        """Створення сітки лікарів та їх черг"""
        # Рядок і колонка для сітки
        row = 0
        col = 0
        for doctor_name in self.doctors:
            # Група для кожного лікаря
            doctor_group = QGroupBox(doctor_name)
            doctor_layout = QVBoxLayout()

            # Список черги для пацієнтів цього лікаря
            doctor_layout.addWidget(self.doctors[doctor_name]['list'])

            # Індикатор кількості пацієнтів у черзі
            doctor_layout.addWidget(self.doctors[doctor_name]['indicator'])
            self.update_queue_indicator(doctor_name)

            # Кнопка для прийому пацієнта
            serve_button = QPushButton(f"Прийняти пацієнта")
            serve_button.clicked.connect(
                lambda _, name=doctor_name: self.serve_patient(name))
            doctor_layout.addWidget(serve_button)

            doctor_group.setLayout(doctor_layout)

            self.grid_layout.addWidget(doctor_group, row, col)

            # Розміщення в сітці по 3 елементи в ряд
            col += 1
            if col > 2:
                col = 0
                row += 1

    def add_patient(self):
        """Логіка додавання пацієнта в чергу"""
        patient_name = self.ui.input_patient_name.text()
        selected_doctor = self.ui.comboBox_doctor_select.currentText()

        if not patient_name:
            self.show_message("Помилка: Введіть ім'я пацієнта.", is_error=True)
            return

        if self.doctors[selected_doctor]['queue'].size() >= self.MAX_QUEUE_SIZE:
            self.show_message(f"Помилка: Черга до лікаря {selected_doctor} вже заповнена.")
            return

        self.doctors[selected_doctor]['queue'].enqueue(patient_name)
        self.update_doctor_queue(selected_doctor)
        self.ui.input_patient_name.clear()

        self.show_message(f"Пацієнт {patient_name} успішно доданий до черги лікаря {selected_doctor}.")

    def serve_patient(self, doctor_name):
        """Прийом пацієнта лікарем"""
        if not self.doctors[doctor_name]['queue'].is_empty():
            served_patient = self.doctors[doctor_name]['queue'].dequeue()  # Беремо пацієнта з початку черги
            self.update_doctor_queue(doctor_name)
            self.show_message(f"Пацієнт {served_patient} прийнятий лікарем {doctor_name}.")
        else:
            self.show_message(f"Помилка: Черга до лікаря {doctor_name} порожня.", is_error=True)

    def update_queue_indicator(self, doctor_name):
        """Оновлення індикатора кількості пацієнтів у черзі"""
        self.doctors[doctor_name]['indicator'].setText(f"Пацієнтів у черзі: {self.doctors[doctor_name]['queue'].size()}")

    def update_doctor_queue(self, doctor_name):
        """Оновлення відображення черги лікаря"""
        self.doctors[doctor_name]['list'].clear()
        if self.doctors[doctor_name]['queue'].is_empty():
            self.show_message(f"Помилка: Черга до лікаря {doctor_name} порожня.", is_error=True)
            return

        for i in range(self.doctors[doctor_name]['queue'].size()):
            patient = self.doctors[doctor_name]['queue'].dequeue()
            self.doctors[doctor_name]['list'].addItem(patient)
            self.doctors[doctor_name]['queue'].enqueue(patient)

        self.update_queue_indicator(doctor_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HospitalQueueSystem()
    window.show()
    app.exec()