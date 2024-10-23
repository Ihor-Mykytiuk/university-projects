import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem, \
    QHeaderView
from lab7.ui.task1_interface import Ui_MainWindow
from PySide6.QtCore import QFile, QIODevice, QTextStream


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Ініціалізація таблиці результатів
        self.init_results_table()

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

    def init_results_table(self):
        self.ui.tableResults.setColumnCount(2)
        self.ui.tableResults.setHorizontalHeaderLabels(["Група", "Максимальне значення"])
        self.ui.tableResults.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ui.tableResults.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

    def show_message(self, message, is_error=False):
        """Відображення повідомлення"""
        color = "red" if is_error else "green"
        self.ui.labelMessages.setStyleSheet(f"color: {color};")
        self.ui.labelMessages.setText(message)

    def select_input_file(self):
        """Вибір вхідного файлу через QFileDialog"""
        file_name, _ = QFileDialog.getOpenFileName(self, "Вибрати вхідний файл", "",
                                                   "Text Files (*.txt);;All Files (*)")
        if file_name:  # Якщо користувач вибрав файл
            self.input_file_path = file_name  # Зберігаємо шлях до вибраного файлу
            self.ui.labelInputFile.setText(f"Вхідний файл: {os.path.basename(file_name)}")
        else:
            self.show_message("Помилка: вхідний файл не вибрано.", is_error=True)

    def select_output_file(self):
        """Вибір вихідного файлу через QFileDialog"""
        file_name, _ = QFileDialog.getSaveFileName(self, "Вибрати вихідний файл", "",
                                                   "Text Files (*.txt);;All Files (*)")
        if file_name:
            self.output_file_path = file_name  # Зберігаємо шлях до вибраного файлу
            self.ui.labelOutputFile.setText(f"Вихідний файл: {os.path.basename(file_name)}")
        else:
            self.show_message("Помилка: вихідний файл не вибрано.", is_error=True)

    def select_standard_files(self):
        """Автоматичний вибір стандартних файлів з директорії проєкту"""
        base_path = os.path.dirname(os.path.abspath(__file__)) # Шлях до поточної директорії
        self.input_file_path = os.path.join(base_path, "files", 'f.txt')
        self.output_file_path = os.path.join(base_path, "files", 'g.txt')

        self.ui.labelInputFile.setText(f"Вхідний файл: f.txt")
        self.ui.labelOutputFile.setText(f"Вихідний файл: g.txt")
        self.show_message("Стандартні файли вибрано успішно.")

    def read_input_file(self):
        """Зчитування даних з вхідного файлу за допомогою QFile."""
        file = QFile(self.input_file_path)
        if not file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):  # Спробуємо відкрити файл
            self.show_message(f"Не вдалося відкрити вхідний файл: {file.errorString()}", is_error=True)
            return []
        try:
            stream = QTextStream(file)
            data = stream.readAll()
            numbers = list(map(int, data.split()))
            return numbers

        except Exception as e:  # Обробка помилок
            self.show_message(f"Помилка при зчитуванні даних: {str(e)}", is_error=True)
            return []
        finally:
            file.close()

    def write_output_file(self, results):
        """Запис даних у вихідний файл"""
        file = QFile(self.output_file_path)
        if not file.open(QFile.OpenModeFlag.WriteOnly | QFile.OpenModeFlag.Text):
            self.show_message(f"Не вдалося відкрити вихідний файл: {file.errorString()}", is_error=True)
            return
        try:
            stream = QTextStream(file)
            stream << ' '.join(map(str, results))  # Записуємо всі значення через пробіл
        except Exception as e:
            self.show_message(f"Помилка при записі даних: {str(e)}", is_error=True)
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
                self.update_result_table(i // 5, group, max_in_group)

            return results  # Повертаємо список максимальних значень

        except Exception as e:
            self.show_message(f"Помилка при обробці даних: {str(e)}", is_error=True)
            return []

    def update_result_table(self, index, group, max_value):
        """Оновлення таблиці результатів"""
        self.ui.tableResults.setRowCount(index + 1)
        self.ui.tableResults.setItem(index, 0, QTableWidgetItem(str(group)))
        self.ui.tableResults.setItem(index, 1, QTableWidgetItem(str(max_value)))

    def clear_results(self):
        """Очищення результатів"""
        self.ui.tableResults.setRowCount(0)
        self.ui.labelMessages.clear()
        self.input_file_path = ""
        self.output_file_path = ""
        self.ui.labelInputFile.clear()
        self.ui.labelOutputFile.clear()

    def process_file(self):
        """Обробка файлів"""
        if not self.input_file_path:
            self.show_message("Помилка: виберіть вхідний файл.", is_error=True)
            return
        if not self.output_file_path:
            self.show_message("Помилка: виберіть вихідний файл.", is_error=True)
            return
        results = self.process_numbers()
        if results:
            self.write_output_file(results)
            self.show_message("Дані успішно оброблено та записано.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
