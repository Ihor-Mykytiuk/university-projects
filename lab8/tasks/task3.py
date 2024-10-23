from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton,
                               QComboBox, QLineEdit, QGridLayout, QScrollArea, QGroupBox, QSizePolicy)
from lab8.utils.data_structures import Queue

class HospitalQueueSystem(QWidget):
    def __init__(self):
        super().__init__()

        # Список лікарів і черги пацієнтів
        self.doctors = {
            "Терапевт": Queue(),
            "Стоматолог": Queue(),
            "Кардіолог": Queue(),
            "Хірург": Queue(),
            "Офтальмолог": Queue(),
            "Дерматолог": Queue(),
        }

        self.MAX_QUEUE_SIZE = 10  # Максимум 10 пацієнтів в черзі до одного лікаря

        # Основне вікно
        self.setWindowTitle("Запис до лікаря")
        self.layout = QVBoxLayout(self)

        # Верхній блок для введення пацієнта і вибору лікаря
        self.create_patient_input()

        # Скролл для відображення списку лікарів
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        # Контейнер для сітки лікарів
        self.scroll_content = QWidget()
        self.scroll_layout = QGridLayout(self.scroll_content)

        # Сітка для черг лікарів
        self.queues = {}  # Словник для зберігання списків черг для кожного лікаря
        self.indicators = {}  # Індикатори черг для відображення кількості пацієнтів
        self.create_doctor_queues()

        self.scroll_area.setWidget(self.scroll_content)

        # Лейбл для повідомлень
        self.message_label = QLabel(self)
        self.layout.addWidget(self.message_label)

    def create_patient_input(self):
        # Поле для введення імені пацієнта
        self.patient_name_input = QLineEdit(self)
        self.patient_name_input.setPlaceholderText("Введіть ім'я пацієнта")
        self.layout.addWidget(self.patient_name_input)

        # Вибір лікаря
        self.doctor_selector = QComboBox(self)
        self.doctor_selector.addItems(self.doctors)
        self.layout.addWidget(self.doctor_selector)

        # Кнопка для додавання пацієнта в чергу
        self.add_patient_button = QPushButton("Записатися")
        self.add_patient_button.clicked.connect(self.add_patient)
        self.layout.addWidget(self.add_patient_button)

    def create_doctor_queues(self):
        # Рядок і колонка для сітки
        row = 0
        col = 0
        for doctor_name in self.doctors:
            # Створюємо групу для кожного лікаря з рамкою
            doctor_group = QGroupBox(doctor_name)
            doctor_group.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
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

            self.scroll_layout.addWidget(doctor_group, row, col)

            # Розміщення в сітці по 3 елементи в ряд
            col += 1
            if col > 2:
                col = 0
                row += 1

    def add_patient(self):
        # Отримання введеного ім'я та обраного лікаря
        patient_name = self.patient_name_input.text()
        selected_doctor = self.doctor_selector.currentText()

        # Перевірка, чи введено ім'я пацієнта
        if not patient_name:
            self.update_message("Помилка: Введіть ім'я пацієнта!")
            return

        # Перевірка, чи не перевищено кількість пацієнтів у черзі
        if self.doctors[selected_doctor].size() >= self.MAX_QUEUE_SIZE:
            self.update_message(f"Помилка: Черга до {selected_doctor} заповнена. Максимум {self.MAX_QUEUE_SIZE} осіб.")
            return

        # Додавання пацієнта в чергу
        self.doctors[selected_doctor].enqueue(patient_name)
        self.queues[selected_doctor].addItem(patient_name)
        self.patient_name_input.clear()

        self.update_queue_indicator(selected_doctor)

        self.update_message(f"Пацієнт {patient_name} успішно записаний до {selected_doctor}.")

    def serve_patient(self, doctor_name, doctor_queue):
        # Логіка прийому пацієнта
        if not self.doctors[doctor_name].is_empty():
            served_patient = self.doctors[doctor_name].dequeue()  # Беремо пацієнта з початку черги
            doctor_queue.takeItem(0)  # Видаляємо його зі списку в інтерфейсі
            self.update_queue_indicator(doctor_name)
            self.update_message(f"Лікар {doctor_name} прийняв пацієнта {served_patient}.")
        else:
            self.update_message(f"Інформація: Черга до лікаря {doctor_name} порожня.")

    def update_queue_indicator(self, doctor_name):
        self.indicators[doctor_name].setText(f"Пацієнтів у черзі: {self.doctors[doctor_name].size()}")

    def update_message(self, message):
        self.message_label.setText(message)


if __name__ == "__main__":
    app = QApplication([])
    window = HospitalQueueSystem()
    window.show()
    app.exec()