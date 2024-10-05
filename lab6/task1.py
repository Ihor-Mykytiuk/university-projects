import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from task1_interface import Ui_Form  # Імпортуй тут свій інтерфейс

class ListManipulator(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Ініціалізуємо інтерфейс
        self.ui.setupUi(self)
        self.apply_styles()

        # Список для роботи
        self.array = []

        # Підключення сигналів до функцій
        self.ui.create_array_button.clicked.connect(self.generate_list)
        self.ui.delete_button.clicked.connect(self.delete_elements)

    def apply_styles(self):
        """Застосування стилів з файлу CSS"""
        with open("../static/styles/styles.qss", "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def generate_list(self):
        """Генеруємо випадковий список на основі введеної кількості елементів"""
        try:
            size = int(self.ui.size_input.text())
            if size <= 0:
                raise ValueError
            self.array = [random.randint(1, 100) for _ in range(size)]
            self.display_array(self.array)
            self.display_message("Масив згенеровано!")
        except ValueError:
            self.display_message("Будь ласка, введіть дійсну кількість елементів!", error=True)

    def delete_elements(self):
        """Видалення елементів з позицій N по K"""
        try:
            n = int(self.ui.n_input.text())
            k = int(self.ui.k_input.text())

            if n < 0 or k >= len(self.array) or n > k:
                raise ValueError

            # Видаляємо елементи з N по K
            del self.array[n:k+1]

            # Оновлюємо відображення масиву
            self.display_array(self.array)
            self.display_message(f"Елементи з позицій {n} по {k} видалено!")
        except ValueError:
            self.display_message("Будь ласка, введіть коректні значення для N і K!", error=True)

    def display_array(self, array):
        """Відображає масив у QLabel"""
        self.ui.array_result.setText(", ".join(map(str, array)))

    def display_message(self, message, error=False):
        """Виводить повідомлення у QLabel для статусу. Якщо помилка - виділяємо червоним"""
        if error:
            self.ui.status_label.setStyleSheet("color: red;")
        else:
            self.ui.status_label.setStyleSheet("color: green;")
        self.ui.status_label.setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListManipulator()
    window.show()
    sys.exit(app.exec())
