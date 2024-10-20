from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit,
                               QRadioButton, QPushButton, QButtonGroup)
import sys

class MapStudentApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mapStudent")

        # Студенти та групи
        self.students = {
            "Ivan Petrenko": "ІПЗ-31",
            "Olga Ivanova": "ІПЗ-31",
            "Serhii Shevchenko": "ІПЗ-32",
            "Oksana Dovhal": "ІПЗ-32",
            "Andrii Bondarenko": "ІПЗ-33",
            "Yulia Kalyna": "ІПЗ-31",
            "Mykola Savchuk": "ІПЗ-33",
            "Svitlana Moroz": "ІПЗ-32",
            "Oleksandr Vasilenko": "ІПЗ-31",
            "Nadiia Honchar": "ІПЗ-33",
        }

        # Основний лейаут
        self.layout = QVBoxLayout()

        # Віджет для відображення студентів
        self.students_list = QTextEdit(self)
        self.students_list.setReadOnly(True)
        self.update_students_list()
        self.layout.addWidget(self.students_list)

        # Поле для пошуку
        self.search_label = QLabel("Введіть ім'я студента або групу:")
        self.layout.addWidget(self.search_label)
        self.search_field = QLineEdit(self)
        self.layout.addWidget(self.search_field)

        # Поле для результату
        self.result_label = QLabel("Результат пошуку:")
        self.layout.addWidget(self.result_label)
        self.result_field = QLineEdit(self)
        self.result_field.setReadOnly(True)
        self.layout.addWidget(self.result_field)

        # Вибір типу пошуку
        self.search_by_name_button = QRadioButton("Пошук по імені", self)
        self.search_by_group_button = QRadioButton("Пошук по групі", self)
        self.search_by_name_button.setChecked(True)

        # Додаємо кнопки в групу, щоб вони перемикалися
        self.radio_group = QButtonGroup(self)
        self.radio_group.addButton(self.search_by_name_button)
        self.radio_group.addButton(self.search_by_group_button)

        # Лейаут для кнопок радіо
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.search_by_name_button)
        radio_layout.addWidget(self.search_by_group_button)
        self.layout.addLayout(radio_layout)

        # Кнопка для пошуку
        self.search_button = QPushButton("Пошук")
        self.search_button.clicked.connect(self.perform_search)
        self.layout.addWidget(self.search_button)

        # Встановлюємо основний лейаут
        self.setLayout(self.layout)

    def update_students_list(self):
        """Оновлює текстовий віджет зі списком студентів"""
        student_info = "\n".join([f"{name}: {group}" for name, group in self.students.items()])
        self.students_list.setText(student_info)

    def perform_search(self):
        """Виконує пошук за вибраними критеріями"""
        search_text = self.search_field.text().strip()
        result = ""

        if self.search_by_name_button.isChecked():
            # Пошук по імені студента
            result = self.students.get(search_text, "Студента не знайдено")
        elif self.search_by_group_button.isChecked():
            # Пошук по групі
            students_in_group = [name for name, group in self.students.items() if group == search_text]
            if students_in_group:
                result = ", ".join(students_in_group)
            else:
                result = "Групу не знайдено"

        self.result_field.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapStudentApp()
    window.show()
    sys.exit(app.exec())
