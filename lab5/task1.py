# task1.py
import sys
from PySide6.QtWidgets import QApplication
from lab5.ui.task1_interface import Ui_Form
from base_widget import BaseWidget
from array_handler import TransformArray
class ArrayTransform(BaseWidget):
    def __init__(self):
        super().__init__(Ui_Form)
        self.array_handler = TransformArray()

        # Підключення сигналів до функцій
        self.ui.create_array_button.clicked.connect(self.create_array)
        self.ui.transform_array_button.clicked.connect(self.perform_transformation)

        # Обробка змін в полях введення
        self.ui.size_input.textChanged.connect(self.input_changed)
        self.ui.array_input.textChanged.connect(self.input_changed)

    def create_array(self):
        """Обробка натискання кнопки створення масиву"""
        try:
            size_text = self.ui.size_input.text()
            array_text = self.ui.array_input.text()
            if not size_text and not array_text:
                raise ValueError("Введіть розмір масиву або сам масив.")
            if not self.is_valid_number(size_text):
                raise ValueError("Введене значення не є натуральним числом")
            size = int(size_text) if size_text else None
            if size is not None:
                self.array_handler.create_random_array(size)
            elif array_text:
                self.array_handler.create_array_from_input(array_text)
            self.display_array(self.array_handler.array)
            self.display_message("Масив успішно створено.")
        except ValueError as e:
            self.display_message(str(e), error=True)

    def perform_transformation(self):
        """Виконання перетворення масиву"""
        try:
            transformed_array = self.array_handler.transform()
            self.display_array(transformed_array)
            self.display_message("Масив успішно перетворено.")
        except ValueError as e:
            self.display_message(str(e), error=True)

    def input_changed(self):
        """Блокує одне поле, якщо введено дані в інше."""
        size_text = self.ui.size_input.text()
        array_text = self.ui.array_input.text()

        # Якщо є текст в одному з полів, блокуємо інше
        self.ui.array_input.setDisabled(bool(size_text))
        self.ui.size_input.setDisabled(bool(array_text))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArrayTransform()
    window.show()
    sys.exit(app.exec())
