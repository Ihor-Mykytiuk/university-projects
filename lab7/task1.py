import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem
from ui.task1_interface import Ui_MainWindow
from PySide6.QtCore import QFile, QIODevice

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Ініціалізація атрибутів для збереження шляхів до файлів
        self.input_file_path = ""
        self.output_file_path = ""

        # Налаштування зв'язків кнопок
        self.setup_connections()

    def setup_connections(self):
        """Налаштування зв'язків кнопок"""
        self.ui.btnSelectInputFile.clicked.connect(self.select_input_file)
        self.ui.btnSelectOutputFile.clicked.connect(self.select_output_file)
        self.ui.btnSelectStandardFiles.clicked.connect(self.select_standard_files)
        self.ui.btnRunProcessing.clicked.connect(self.process_file)
        self.ui.btnClearResults.clicked.connect(self.clear_results)

    def select_input_file(self):
        """Вибір вхідного файлу через QFileDialog"""
        file_name, _ = QFileDialog.getOpenFileName(self, "Вибрати вхідний файл", "",
                                                   "Text Files (*.txt);;All Files (*)")
        if file_name:  # Якщо користувач вибрав файл
            self.input_file_path = file_name  # Зберігаємо шлях до вибраного файлу
            self.ui.labelInputFile.setText(f"Вхідний файл: {os.path.basename(file_name)}")
        else:
            self.ui.labelMessages.setText("Вхідний файл не вибрано.")

    def select_output_file(self):
        """Вибір вихідного файлу через QFileDialog"""
        file_name, _ = QFileDialog.getSaveFileName(self, "Вибрати вихідний файл", "",
                                                   "Text Files (*.txt);;All Files (*)")
        if file_name:
            self.output_file_path = file_name  # Зберігаємо шлях до вибраного файлу
            self.ui.labelOutputFile.setText(f"Вихідний файл: {os.path.basename(file_name)}")
        else:
            self.ui.labelMessages.setText("Вихідний файл не вибрано.")

    def select_standard_files(self):
        """Автоматичний вибір стандартних файлів з директорії проєкту"""
        base_path = os.path.dirname(os.path.abspath(__file__)) # Шлях до поточної директорії
        self.input_file_path = os.path.join(base_path, 'f.txt')
        self.output_file_path = os.path.join(base_path, 'g.txt')

        self.ui.labelInputFile.setText(f"Вхідний файл: f.txt")
        self.ui.labelOutputFile.setText(f"Вихідний файл: g.txt")

    def process_file(self):
        """Обробка файлу"""
        pass

    def clear_results(self):
        """Очищення результатів"""
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
