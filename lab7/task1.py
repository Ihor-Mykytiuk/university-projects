import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox)
from PySide6.QtCore import QFile, QIODevice

class FileProcessorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("File Processor")
        self.setGeometry(100, 100, 400, 200)

        # Створюємо основні елементи
        self.layout = QVBoxLayout()

        self.input_label = QLabel("Виберіть вхідний файл (f.txt):")
        self.output_label = QLabel("Виберіть вихідний файл (g.txt):")
        self.result_label = QLabel("Результат: ")

        self.input_button = QPushButton("Вибрати вхідний файл")
        self.output_button = QPushButton("Вибрати вихідний файл")
        self.process_button = QPushButton("Запустити обробку")

        # Додаємо елементи на форму
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_button)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_button)
        self.layout.addWidget(self.process_button)
        self.layout.addWidget(self.result_label)

        # Прив'язуємо події до кнопок
        self.input_button.clicked.connect(self.choose_input_file)
        self.output_button.clicked.connect(self.choose_output_file)
        self.process_button.clicked.connect(self.process_files)

        # Налаштовуємо загальний макет
        self.setLayout(self.layout)

        # Змінні для збереження вибраних файлів
        self.input_filename = ""
        self.output_filename = ""

    def choose_input_file(self):
        # Відкриваємо діалог вибору файлу для вхідного файлу
        filename, _ = QFileDialog.getOpenFileName(self, "Виберіть вхідний файл", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            self.input_filename = filename
            self.input_label.setText(f"Вибрано вхідний файл: {filename}")

    def choose_output_file(self):
        # Відкриваємо діалог вибору файлу для вихідного файлу
        filename, _ = QFileDialog.getSaveFileName(self, "Виберіть вихідний файл", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            self.output_filename = filename
            self.output_label.setText(f"Вибрано вихідний файл: {filename}")

    def process_files(self):
        # Перевірка, чи вибрані файли
        if not self.input_filename or not self.output_filename:
            QMessageBox.warning(self, "Помилка", "Будь ласка, виберіть обидва файли.")
            return

        # Викликаємо функцію для обробки файлів
        try:
            self.process_file_logic(self.input_filename, self.output_filename)
            self.result_label.setText("Файл успішно оброблено!")
        except Exception as e:
            QMessageBox.critical(self, "Помилка", f"Сталася помилка: {str(e)}")

    def process_file_logic(self, input_filename: str, output_filename: str):
        # Відкриваємо файл f для читання
        input_file = QFile(input_filename)
        if not input_file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            raise IOError(f"Неможливо відкрити файл {input_filename}")

        # Відкриваємо файл g для запису
        output_file = QFile(output_filename)
        if not output_file.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Text):
            raise IOError(f"Неможливо відкрити файл {output_filename}")

        # Зчитуємо вміст файлу f
        data = input_file.readAll().data().decode('utf-8')
        numbers = list(map(int, data.split()))  # Перетворюємо на список цілих чисел

        input_file.close()  # Закриваємо вхідний файл

        # Обробка по 5 елементів
        result = []
        for i in range(0, len(numbers), 5):
            group = numbers[i:i+5]  # Вибираємо групи по 5 елементів
            max_value = max(group)  # Знаходимо максимум у групі
            result.append(max_value)

        # Записуємо результат у файл g
        output_file.write(" ".join(map(str, result)).encode('utf-8'))
        output_file.close()

# Основний код для запуску додатку
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = FileProcessorApp()
    window.show()

    sys.exit(app.exec())
