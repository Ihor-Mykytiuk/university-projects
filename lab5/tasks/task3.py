#task3.py
import sys
from PySide6.QtWidgets import QApplication
from lab5.ui.task3_interface import Ui_Form
from lab5.utils.base_widget import BaseWidget
from lab5.utils.matrix_handler import MatrixHandler


class MatrixSum(BaseWidget):
    def __init__(self):
        super().__init__(Ui_Form)
        self.matrix_handler = MatrixHandler()

        # Підключення сигналів
        self.ui.generate_matrix_button.clicked.connect(self.create_matrix)
        self.ui.calculate_sum_button.clicked.connect(self.calculate_sum)

    def create_matrix(self):
        """Генерує випадкову матрицю та відображає її"""
        try:
            m = int(self.ui.m_input.text())
            n = int(self.ui.n_input.text())
            self.matrix_handler.generate_matrix(m, n)
            self.display_matrix(self.matrix_handler.matrix)
            self.display_message("Матрицю згенеровано!")
        except ValueError:
            self.display_message("Помилка: введіть коректні розміри матриці.", error=True)

    def calculate_sum(self):
        """Обчислює суму елементів парних або непарних стовпців"""
        try:
            even = self.ui.comboBox.currentText() == "Парні стовпці"
            total_sum = self.matrix_handler.sum_columns(even=even)
            self.display_message(f"Сума: {total_sum}")
        except ValueError as e:
            self.display_message(str(e), error=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixSum()
    window.show()
    sys.exit(app.exec())
