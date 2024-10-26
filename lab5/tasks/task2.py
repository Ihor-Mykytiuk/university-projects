import sys
from PySide6.QtWidgets import QApplication
from lab5.ui.task2_interface import Ui_Form
from lab5.utils.base_widget import BaseWidget
from lab5.utils.array_handler import SortArray


class ArraySort(BaseWidget):
    def __init__(self):
        super().__init__(Ui_Form)
        self.array_handler = SortArray()

        # Підключення сигналів до функцій
        self.ui.pushButton_create_array.clicked.connect(self.create_array)
        self.ui.pushButton_sort_array.clicked.connect(self.perform_transformation)

        # Обробка змін в полях введення
        self.ui.size_input.textChanged.connect(self.input_changed)
        self.ui.array_input.textChanged.connect(self.input_changed)

    def create_array(self):
        """Обробка натискання кнопки створення масиву"""
        try:
            size_text = self.ui.size_input.text()
            array_text = self.ui.array_input.text()
            if not size_text and not array_text:
                raise ValueError("Помилка: введіть розмір масиву або сам масив.")
            if size_text:
                self.array_handler.create_random_array(size_text)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArraySort()
    window.show()
    sys.exit(app.exec())
