import sys
import numpy as np
from PySide6.QtWidgets import QApplication
from lab5.ui.task4_interface import Ui_Form
from base_widget import BaseWidget  # Імпортуємо базовий клас

class MatrixTransform(BaseWidget):
    def __init__(self):
        super().__init__(Ui_Form)  # Викликаємо конструктор базового класу

        # Підключення сигналів до функцій
        self.ui.generate_matrix_button.clicked.connect(self.generate_matrix)
        self.ui.transform_matrix_button.clicked.connect(self.transform_matrix)

        self.matrix = None  # Зберігає згенеровану матрицю

    def generate_matrix(self):
        """Генерує випадкову матрицю розміру m x n"""
        try:
            m = int(self.ui.m_input.text())
            n = int(self.ui.n_input.text())
            if m < 1 or n < 1:
                raise ValueError

            # Генеруємо матрицю розміру m x n з випадковими числами від 1 до 100
            self.matrix = np.random.randint(1, 101, size=(m, n))
            self.display_matrix()
            self.display_message("Матрицю згенеровано!")
        except ValueError:
            self.display_message("Помилка: введіть коректні розміри матриці.", error=True)

    def display_matrix(self):
        """Виводить матрицю у вигляді рядків у QLabel"""
        matrix_str = '\n'.join(', '.join(map(str, row)) for row in self.matrix)
        self.ui.array_result.setText(matrix_str)

    def transform_matrix(self):
        """Перетворює матрицю: міняє місцями мінімальний і максимальний елементи в кожному рядку"""
        if self.matrix is None:
            self.display_message("Помилка: спочатку згенеруйте матрицю.", error=True)
            return

        transformed_matrix = self.matrix.copy()  # Створюємо копію матриці для перетворення

        for i, row in enumerate(transformed_matrix):
            min_index = np.argmin(row)  # Індекс мінімального елемента
            max_index = np.argmax(row)  # Індекс максимального елемента

            # Міняємо місцями мінімальний і максимальний елементи
            transformed_matrix[i][min_index], transformed_matrix[i][max_index] = (
                transformed_matrix[i][max_index],
                transformed_matrix[i][min_index],
            )

        self.display_matrix()  # Відображаємо перетворену матрицю
        self.display_message("Матриця перетворена!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixTransform()
    window.show()
    sys.exit(app.exec())
