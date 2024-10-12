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
        """Відображення повідомлення"""
        pass

    def setup_connections(self):
        """Налаштування зв'язків кнопок"""
        pass

    def select_file(self, label):
        """Вибір файлу через QFileDialog"""
        pass

    def select_standard_files(self):
        """Вибір стандартних файлів"""
        pass

    def create_help_file(self):
        """Створення доопоміжного файлу"""
        pass

    def delete_help_file(self):
        """Видалення допоміжного файлу"""
        pass

    def swap_files_content(self):
        """Обмін вмісту файлів"""
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
