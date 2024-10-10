import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem
from ui.task1_interface import Ui_MainWindow
from PySide6.QtCore import QFile, QIODevice, QTextStream


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

    def read_input_file(self):
        """Зчитування даних з вхідного файлу за допомогою QFile."""
        if not self.input_file_path:
            self.ui.labelMessages.setText("Спочатку виберіть вхідний файл.")
            return []

        file = QFile(self.input_file_path)
        if not file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):  # Спробуємо відкрити файл
            self.ui.labelMessages.setText(f"Не вдалося відкрити файл: {file.errorString()}")
            return []

        try:
            stream = QTextStream(file)
            data = stream.readAll()
            numbers = list(map(int, data.split()))
            return numbers

        except Exception as e:  # Обробка помилок
            self.ui.labelMessages.setText(f"Виникла помилка під час зчитування файлу: {str(e)}")
            return []
        finally:
            file.close()

    def write_output_file(self, results):
        """Запис даних у вихідний файл"""
        if not self.output_file_path:
            self.ui.labelMessages.setText("Вихідний файл не вказано.")
            return

        file = QFile(self.output_file_path)
        if not file.open(QFile.OpenModeFlag.WriteOnly | QFile.OpenModeFlag.Text):
            self.ui.labelMessages.setText("Не вдалося відкрити файл для запису.")
            return
        try:
            stream = QTextStream(file)
            stream << ' '.join(map(str, results))  # Записуємо всі значення через пробіл
        except Exception as e:
            self.ui.labelMessages.setText(f"Помилка при запису у файл: {str(e)}")
        finally:
            file.close()

    def process_numbers(self):
        """Обробка чисел"""
        try:
            numbers = self.read_input_file()
            results = []
            for i in range(0, len(numbers), 5):
                group = numbers[i:i + 5]
                max_in_group = max(group)
                results.append(max_in_group)

            return results  # Повертаємо список максимальних значень

        except Exception as e:
            self.ui.labelMessages.setText(f"Помилка обробки чисел: {str(e)}")
            return []

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
