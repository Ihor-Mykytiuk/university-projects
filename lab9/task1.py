from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit,
                               QRadioButton, QPushButton, QButtonGroup, QMessageBox)
from PySide6.QtCore import Qt
import sys

class MapStudentApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mapStudent")

        # Студенти та групи
        self.students = {
            "Іван Петренко": "ІПЗ-31",
            "Ольга Іванова": "ІПЗ-31",
            "Сергій Шевченко": "ІПЗ-32",
            "Оксана Довгаль": "ІПЗ-32",
            "Андрій Бондаренко": "ІПЗ-33",
            "Юлія Калина": "ІПЗ-31",
            "Микола Савчук": "ІПЗ-33",
            "Світлана Мороз": "ІПЗ-32",
            "Олександр Василенко": "ІПЗ-31",
            "Надія Гончар": "ІПЗ-33",
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
        self.search_field.textChanged.connect(self.dynamic_search)
        self.layout.addWidget(self.search_field)

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

        # Поля для додавання/видалення студентів
        self.add_label = QLabel("Додати або видалити студента:")
        self.layout.addWidget(self.add_label)

        # Поле для введення імені
        self.add_name_field = QLineEdit(self)
        self.add_name_field.setPlaceholderText("Введіть ім'я студента")
        self.layout.addWidget(self.add_name_field)

        # Поле для введення групи
        self.add_group_field = QLineEdit(self)
        self.add_group_field.setPlaceholderText("Введіть групу")
        self.layout.addWidget(self.add_group_field)

        # Кнопки додавання і видалення
        self.add_button = QPushButton("Додати студента")
        self.add_button.clicked.connect(self.add_student)
        self.layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Видалити студента")
        self.delete_button.clicked.connect(self.delete_student)
        self.layout.addWidget(self.delete_button)

        # Встановлюємо основний лейаут
        self.setLayout(self.layout)

    def update_students_list(self):
        """Оновлює текстовий віджет зі списком студентів"""
        student_info = "\n".join([f"{name}: {group}" for name, group in self.students.items()])
        self.students_list.setText(student_info)

    def dynamic_search(self):
        """Виконує динамічний пошук за введеними критеріями"""
        search_text = self.search_field.text().strip().lower()

        if not search_text:
            # Якщо поле пошуку порожнє, показуємо весь список
            self.update_students_list()
            return

        # Вибір пошуку за іменем або групою
        if self.search_by_name_button.isChecked():
            # Пошук за іменем
            filtered_students = {name: group for name, group in self.students.items()
                                 if search_text in name.lower()}
        else:
            # Пошук за групою
            filtered_students = {name: group for name, group in self.students.items()
                                 if search_text in group.lower()}

        # Виводимо результати пошуку
        if filtered_students:
            student_info = "\n".join([f"{name}: {group}" for name, group in filtered_students.items()])
            self.students_list.setText(student_info)
        else:
            self.students_list.setText("Результати не знайдено")


    def add_student(self):
        """Додає студента до довідника"""
        name = self.add_name_field.text().strip()
        group = self.add_group_field.text().strip()

        if not name or not group:
            QMessageBox.warning(self, "Помилка", "Будь ласка, введіть ім'я студента та групу.")
            return

        if name in self.students:
            QMessageBox.information(self, "Помилка", f"Студент {name} вже існує в списку.")
        else:
            self.students[name] = group
            self.update_students_list()
            QMessageBox.information(self, "Успіх", f"Студент {name} доданий до групи {group}.")
            self.add_name_field.clear()
            self.add_group_field.clear()

    def delete_student(self):
        """Видаляє студента з довідника"""
        name = self.add_name_field.text().strip()

        if not name:
            QMessageBox.warning(self, "Помилка", "Будь ласка, введіть ім'я студента для видалення.")
            return

        if name in self.students:
            del self.students[name]
            self.update_students_list()
            QMessageBox.information(self, "Успіх", f"Студент {name} був видалений.")
            self.add_name_field.clear()
        else:
            QMessageBox.warning(self, "Помилка", f"Студент {name} не знайдений у списку.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapStudentApp()
    window.show()
    sys.exit(app.exec())
