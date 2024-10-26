import os, sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from lab7.ui.task2_interface import Ui_MainWindow


class FileSwapper(QMainWindow):
    def __init__(self):
        super().__init__()
        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Ініціалізація атрибутів для збереження шляхів до файлів
        self.f1_path = ""
        self.f2_path = ""

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
        self.ui.pushButton_select_first_file.clicked.connect(lambda: self.select_file("f1"))
        self.ui.pushButton_select_second_file.clicked.connect(lambda: self.select_file("f2"))
        self.ui.pushButton_select_standard_files.clicked.connect(self.select_standard_files)

        self.ui.pushButton_run_processing.clicked.connect(self.process_files)
        self.ui.pushButton_clear_results.clicked.connect(self.clear_results)

    def select_file(self, file_type):
        """Вибір файлу через QFileDialog"""
        file_name, _ = QFileDialog.getOpenFileName(self, f"Вибрати файл {file_type}", "",
                                                   "Text Files (*.txt);;All Files (*)")
        if file_name:  # Якщо користувач вибрав файл
            if file_type == "f1":
                self.f1_path = file_name
                label = self.ui.label_first_file
            elif file_type == "f2":
                self.f2_path = file_name
                label = self.ui.label_second_file
            label.setText(f"Файл {file_type}: {os.path.basename(file_name)}")
            self.show_message(f"Файл {file_type} вибрано успішно.")
        else:
            self.show_message(f"Помилка: Файл {file_type} не вибрано.", is_error=True)

    def select_standard_files(self):
        """Вибір стандартних файлів з директорії проєкту"""
        base_path = os.path.dirname(os.path.abspath(__file__))
        first_file_name = "f1.txt"
        second_file_name = "f2.txt"
        self.f1_path = os.path.join(base_path, "../", "files", first_file_name)
        self.f2_path = os.path.join(base_path, "../", "files", second_file_name)

        # Оновлення тексту на мітках
        self.ui.label_first_file.setText(f"Файл f1: {first_file_name}")
        self.ui.label_second_file.setText(f"Файл f2: {second_file_name}")

        self.show_message("Стандартні файли вибрано успішно.")

    def create_help_file(self):
        """Створення порожнього допоміжного файлу"""
        help_file_path = os.path.join(os.path.dirname(self.f1_path), "h.txt")  # Шлях до допоміжного файлу

        try:
            help_file = QFile(help_file_path)
            if help_file.open(QIODevice.OpenModeFlag.WriteOnly):
                help_file.write(b"")
                return help_file_path
        except Exception as e:
            self.show_message(f"Помилка створення файлу: {str(e)}", is_error=True)

    def delete_help_file(self):
        """Видалення допоміжного файлу"""
        help_file_path = os.path.join(os.path.dirname(self.f1_path), "h.txt")  # Шлях до допоміжного файлу
        file = QFile(help_file_path)
        if file.exists():
            file.remove()

    def swap_files_content(self):
        """Обмін вмісту файлів"""
        help_file_path = self.create_help_file()

        try:
            file1 = QFile(self.f1_path)
            file2 = QFile(self.f2_path)
            help_file = QFile(help_file_path)

            file1.open(QIODevice.OpenModeFlag.ReadOnly)
            help_file.open(QIODevice.OpenModeFlag.WriteOnly)
            help_file.write(file1.readAll())  # Запис вмісту першого файлу у допоміжний
            file1.close()
            help_file.close()

            file1.open(QIODevice.OpenModeFlag.WriteOnly)
            file2.open(QIODevice.OpenModeFlag.ReadOnly)
            file1.write(file2.readAll())  # Запис вмісту другого файлу у перший
            file1.close()
            file2.close()

            help_file.open(QIODevice.OpenModeFlag.ReadOnly)
            file2.open(QIODevice.OpenModeFlag.WriteOnly)
            file2.write(help_file.readAll())  # Запис вмісту допоміжного файлу у другий
            help_file.close()
            file2.close()

            self.delete_help_file()

            self.show_message("Вміст файлів обміняно успішно.")
        except Exception as e:
            self.show_message(f"Помилка обміну вмісту файлів: {str(e)}", is_error=True)

    def clear_results(self):
        """Очищення результатів"""
        self.ui.label_status.clear()
        self.ui.label_first_file.clear()
        self.ui.label_second_file.clear()
        self.f1_path = ""
        self.f2_path = ""

    def process_files(self):
        """Обробка файлів"""
        if not self.f1_path:
            self.show_message("Помилка: Файл f1 не вибрано.", is_error=True)
            return
        if not self.f2_path:
            self.show_message("Помилка: Файл f2 не вибрано.", is_error=True)
            return

        self.swap_files_content()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSwapper()
    window.show()
    sys.exit(app.exec())
