import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem, \
    QHeaderView
from PySide6.QtCore import QFile, QIODevice, QTextStream
from ui.task2_interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Ініціалізація атрибутів для збереження шляхів до файлів
        self.f1_path = ""
        self.f2_path = ""

    def show_message(self, message, is_error=False):
        """Відображення повідомлення у labelMessages"""
        color = "red" if is_error else "green"
        self.ui.labelMessages.setStyleSheet(f"color: {color};")  # Задаємо колір тексту
        self.ui.labelMessages.setText(message)  # Встановлюємо текст повідомлення

    def setup_connections(self):
        """Налаштування зв'язків кнопок"""
        self.ui.btnSelectFirstFile.clicked.connect(lambda: self.select_file("f1"))
        self.ui.btnSelectSecondFile.clicked.connect(lambda: self.select_file("f2"))
        self.ui.btnSelectStandardFiles.clicked.connect(self.select_standard_files)

        self.ui.btnRunProcessing.clicked.connect(self.process_files)
        self.ui.btnClearResults.clicked.connect(self.clear_results)

    def select_file(self, file_type):
        """Вибір файлу через QFileDialog"""
        pass

    def select_standard_files(self):
        """Вибір стандартних файлів"""
        base_path = os.path.dirname(os.path.abspath(__file__))  # Отримуємо шлях до поточної директорії
        first_file_name = "f1.txt"
        second_file_name = "f2.txt"
        self.f1_path = os.path.join(base_path, "files", first_file_name)
        self.f2_path = os.path.join(base_path, "files", second_file_name)

        # Оновлення тексту на мітках
        self.ui.labelFirstFile.setText(f"Файл f1: {first_file_name}")
        self.ui.labelSecondFile.setText(f"Файл f2: {second_file_name}")

        self.show_message("Стандартні файли вибрано успішно.")

    def create_help_file(self):
        """Створення доопоміжного файлу"""
        pass

    def delete_help_file(self):
        """Видалення допоміжного файлу"""
        pass

    def swap_files_content(self):
        """Обмін вмісту файлів"""
        pass

    def clear_results(self):
        """Очищення"""
        pass

    def process_files(self):
        """Обробка файлів"""
        pass

# Запускаємо застосунок
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
