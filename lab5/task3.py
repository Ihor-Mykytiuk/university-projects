import sys
import numpy as np
from PySide6.QtWidgets import QApplication
from lab5.ui.task3_interface import Ui_Form
from base_widget import BaseWidget  # Імпортуємо базовий клас

class MatrixSum(BaseWidget):
    def __init__(self):
        super().__init__(Ui_Form)  # Викликаємо конструктор базового класу

        # Підключення сигналів до функцій
        self.ui.generate_matrix_button.clicked.connect(self.generate_matrix)
        self.ui.calculate_sum_button.clicked.connect(self.calculate_sum)

        self.matrix = None  # Зберігає матрицю

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

    def calculate_sum(self):
        """Обчислює суму елементів парних або непарних стовпців"""
        if self.matrix is None:
            self.display_message("Помилка: спочатку згенеруйте матрицю.", error=True)
            return

        selected_option = self.ui.comboBox.currentText()
        if selected_option == "Парні стовпці":
            column_indices = range(0, self.matrix.shape[1], 2)  # Індекси парних стовпців (0, 2, 4, ...)
        else:
            column_indices = range(1, self.matrix.shape[1], 2)  # Індекси непарних стовпців (1, 3, 5, ...)

        column_sums = np.sum(self.matrix[:, column_indices], axis=0)
        total_sum = np.sum(column_sums)

        self.display_message(f"Сума: {total_sum}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixSum()
    window.show()
    sys.exit(app.exec())
