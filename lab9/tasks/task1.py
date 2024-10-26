import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from lab9.ui.task1_interface import Ui_MainWindow


class MapStudentApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Студенти та групи
        self.students = {
            "Жидун Володимир": "ІПЗ-32",
            "Бойчук Андрій": "ІПЗ-31",
            "Андрусяк Ілля": "ІПЗ-31",
            "Рижкін Олександр": "ІПЗ-33",
            "Погончук Ярослав": "ІПЗ-32",
            "Бабійчук Василь": "ІПЗ-31",
            "Бабійчук Ігор": "ІПЗ-31",
            "Романів Юрій": "ІПЗ-33",
            "Мельник Дмитро": "ІПЗ-32",
            "Мельник Сергій": "ІПЗ-32"
        }

        # Оновлення списку студентів
        self.update_students_list()

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
        self.ui.pushButton_add_student.clicked.connect(self.add_student)
        self.ui.pushButton_delete_student.clicked.connect(self.delete_student)
        self.ui.input_search.textChanged.connect(self.dynamic_search)

    def update_students_list(self):
        """Оновлює текстовий віджет зі списком студентів"""
        student_info = "\n".join([f"{name}: {group}" for name, group in self.students.items()])
        self.ui.list_students.setText(student_info)

    def dynamic_search(self):
        """Виконує динамічний пошук за введеними критеріями"""
        search_text = self.ui.input_search.text().strip().lower()

        if not search_text:
            # Якщо поле пошуку порожнє, показується весь список
            self.update_students_list()
            return

        # Вибір пошуку за іменем або групою
        if self.ui.radioButton_search_by_name.isChecked():
            filtered_students = {name: group for name, group in self.students.items()
                                 if search_text in name.lower()}
        else:
            filtered_students = {name: group for name, group in self.students.items()
                                 if search_text in group.lower()}

        if filtered_students:
            student_info = "\n".join([f"{name}: {group}" for name, group in filtered_students.items()])
            self.ui.list_students.setText(student_info)
        else:
            self.ui.list_students.setText("Результати не знайдено")


    def add_student(self):
        """Додає студента до довідника"""
        name = self.ui.input_name.text().strip()
        group = self.ui.input_group.text().strip()

        if not name or not group:
            self.show_message("Помилка: Будь ласка, введіть ім'я та групу студента.", is_error=True)
            return

        if name in self.students:
            self.show_message(f"Помилка: Студент {name} вже є у списку.", is_error=True)
        else:
            self.students[name] = group
            self.update_students_list()
            self.show_message(f"Студент {name} був успішно доданий до групи {group}.")
            self.ui.input_name.clear()
            self.ui.input_group.clear()

    def delete_student(self):
        """Видаляє студента з довідника"""
        name = self.ui.input_name.text().strip()

        if not name:
            self.show_message("Помилка: Будь ласка, введіть ім'я студента.", is_error=True)
            return

        if name in self.students:
            del self.students[name]
            self.update_students_list()
            self.show_message(f"Студент {name} був успішно видалений зі списку.")
            self.ui.input_name.clear()
        else:
            self.show_message(f"Помилка: Студента {name} не знайдено.", is_error=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapStudentApp()
    window.show()
    sys.exit(app.exec())
