from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton,
                               QGroupBox, QSizePolicy, QMainWindow, QGridLayout)
from lab8.utils.data_structures import Queue
from lab8.ui.task3_interface import Ui_MainWindow


class HospitalQueueSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Список лікарів і черги пацієнтів
        self.doctors = {
            "Терапевт": Queue(),
            "Стоматолог": Queue(),
            "Кардіолог": Queue(),
            "Хірург": Queue(),
            "Офтальмолог": Queue(),
            "Дерматолог": Queue(),
        }

        self.queues = {}  # Словник для зберігання списків черг для кожного лікаря
        self.indicators = {}  # Індикатори черг для відображення кількості пацієнтів

        self.MAX_QUEUE_SIZE = 10  # Максимум 10 пацієнтів в черзі до одного лікаря

        # Створюємо контейнера для контенту в QScrollArea
        self.scroll_content = QWidget()
        self.grid_layout = QGridLayout(self.scroll_content)  # Порожній QGridLayout
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
            # Створюємо групу для кожного лікаря з рамкою
            doctor_group = QGroupBox(doctor_name)
            doctor_layout = QVBoxLayout()

            # Створюємо список черги для пацієнтів цього лікаря
            doctor_queue = QListWidget()
            doctor_layout.addWidget(doctor_queue)
            self.queues[doctor_name] = doctor_queue  # Зберігаємо список черги

            # Додаємо індикатор кількості пацієнтів
            queue_indicator = QLabel(f"Пацієнтів у черзі: {self.doctors[doctor_name].size()}")
            doctor_layout.addWidget(queue_indicator)
            self.indicators[doctor_name] = queue_indicator  # Зберігаємо індикатор

            # Кнопка для прийому пацієнта
            serve_button = QPushButton(f"Прийняти пацієнта")
            serve_button.clicked.connect(
                lambda _, name=doctor_name, queue=doctor_queue: self.serve_patient(name, queue))
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

        # Перевірка, чи введено ім'я пацієнта
        if not patient_name:
            self.show_message("Помилка: Введіть ім'я пацієнта.", is_error=True)
            return

        # Перевірка, чи не перевищено кількість пацієнтів у черзі
        if self.doctors[selected_doctor].size() >= self.MAX_QUEUE_SIZE:
            self.show_message(f"Помилка: Черга до лікаря {selected_doctor} вже заповнена.")
            return

        # Додавання пацієнта в чергу
        self.doctors[selected_doctor].enqueue(patient_name)
        self.queues[selected_doctor].addItem(patient_name)
        self.ui.input_patient_name.clear()

        self.update_queue_indicator(selected_doctor)

        self.show_message(f"Пацієнт {patient_name} успішно доданий до черги лікаря {selected_doctor}.")

    def serve_patient(self, doctor_name, doctor_queue):
        """Прийом пацієнта лікарем"""
        if not self.doctors[doctor_name].is_empty():
            served_patient = self.doctors[doctor_name].dequeue()  # Беремо пацієнта з початку черги
            doctor_queue.takeItem(0)  # Видаляємо його зі списку в інтерфейсі
            self.update_queue_indicator(doctor_name)
            self.show_message(f"Пацієнт {served_patient} прийнятий лікарем {doctor_name}.")
        else:
            self.show_message(f"Помилка: Черга до лікаря {doctor_name} порожня.", is_error=True)

    def update_queue_indicator(self, doctor_name):
        self.indicators[doctor_name].setText(f"Пацієнтів у черзі: {self.doctors[doctor_name].size()}")


if __name__ == "__main__":
    app = QApplication([])
    window = HospitalQueueSystem()
    window.show()
    app.exec()