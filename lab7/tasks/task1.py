import os, sys
from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView
from lab7.ui.task1_interface import Ui_MainWindow


class FileProcessorApp(QMainWindow):
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
        self.ui.pushButton_select_input_file.clicked.connect(self.select_input_file)
        self.ui.pushButton_select_output_file.clicked.connect(self.select_output_file)
        self.ui.pushButton_select_standard_files.clicked.connect(self.select_standard_files)
        self.ui.pushButton_run_processing.clicked.connect(self.process_file)
        self.ui.pushButton_clear_results.clicked.connect(self.clear_all)

    def init_results_table(self):
        """Ініціалізація таблиці результатів"""
        self.ui.table_results.setColumnCount(2)
        self.ui.table_results.setHorizontalHeaderLabels(["Група", "Максимальне значення"])
        self.ui.table_results.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ui.table_results.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

    def select_input_file(self):
        """Вибір вхідного файлу через QFileDialog"""
        file_name, _ = QFileDialog.getOpenFileName(self, "Вибрати вхідний файл", "",
                                                   "Text Files (*.txt);;All Files (*)")
        if file_name:
            self.input_file_path = file_name
            self.ui.label_input_file.setText(f"Вхідний файл: {os.path.basename(file_name)}")
        else:
            self.show_message("Помилка: Вхідний файл не вибрано.", is_error=True)

    def select_output_file(self):
        """Вибір вихідного файлу через QFileDialog"""
        file_name, _ = QFileDialog.getSaveFileName(self, "Вибрати вихідний файл", "",
                                                   "Text Files (*.txt);;All Files (*)")
        if file_name:
            self.output_file_path = file_name
            self.ui.label_output_file.setText(f"Вихідний файл: {os.path.basename(file_name)}")
        else:
            self.show_message("Помилка: Вихідний файл не вибрано.", is_error=True)

    def select_standard_files(self):
        """Вибір стандартних файлів з директорії проєкту"""
        base_path = os.path.dirname(os.path.abspath(__file__)) # Шлях до поточної директорії
        self.input_file_path = os.path.join(base_path, "../",  "files", 'f.txt')
        self.output_file_path = os.path.join(base_path, "../", "files", 'g.txt')

        self.ui.label_input_file.setText(f"Вхідний файл: f.txt")
        self.ui.label_output_file.setText(f"Вихідний файл: g.txt")
        self.show_message("Стандартні файли вибрано успішно.")

    def read_input_file(self):
        """Зчитування даних з вхідного файлу"""
        file = QFile(self.input_file_path)
        if not file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            self.show_message(f"Не вдалося відкрити вхідний файл: {file.errorString()}", is_error=True)
            return []
        try:
            stream = QTextStream(file)
            data = stream.readAll()
            numbers = list(map(int, data.split()))
            return numbers

        except Exception as e:
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
            stream << ' '.join(map(str, results))
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
            return results
        except Exception as e:
            self.show_message(f"Помилка при обробці даних: {str(e)}", is_error=True)
            return []

    def update_result_table(self, index, group, max_value):
        """Оновлення таблиці результатів"""
        self.ui.table_results.setRowCount(index + 1)
        self.ui.table_results.setItem(index, 0, QTableWidgetItem(str(group)))
        self.ui.table_results.setItem(index, 1, QTableWidgetItem(str(max_value)))

    def clear_all(self):
        """Очищення всіх даних"""
        self.ui.table_results.setRowCount(0)
        self.ui.label_status.clear()
        self.input_file_path = ""
        self.output_file_path = ""
        self.ui.label_input_file.clear()
        self.ui.label_output_file.clear()
        self.ui.table_results.clear()
        self.ui.table_results.clear()
        self.ui.table_results.setHorizontalHeaderLabels(["Група", "Максимальне значення"])

    def process_file(self):
        """Обробка файлів"""
        if not self.input_file_path or not self.output_file_path:
            self.show_message("Помилка: Необхідні файли не вибрано.", is_error=True)

        results = self.process_numbers()
        if results:
            self.write_output_file(results)
            self.show_message("Дані успішно оброблено та записано.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileProcessorApp()
    window.show()
    sys.exit(app.exec())
