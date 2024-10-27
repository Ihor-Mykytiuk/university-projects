import sys
from PySide6.QtWidgets import QApplication
from lab5.utils.matrix_handler import MatrixHandler
from lab5.utils.base_widget import BaseWidget
from lab5.ui.task3_interface import Ui_MainWindow


class MatrixSumApp(BaseWidget):
    def __init__(self):
        super().__init__(Ui_MainWindow)
        self.matrix_handler = MatrixHandler()

        # Налаштування зв'язків кнопок
        self.setup_connections()

    def setup_connections(self):
        """Налаштування зв'язків кнопок"""
        self.ui.pushButton_create_matrix.clicked.connect(self.create_matrix)
        self.ui.pushButton_calculate_sum.clicked.connect(self.calculate_sum)

    def create_matrix(self):
        """Генерування випадкової матриці"""
        try:
            m = int(self.ui.input_m.text())
            n = int(self.ui.input_n.text())
            self.matrix_handler.generate_matrix(m, n)
            self.display_matrix(self.matrix_handler.matrix)
            self.display_message("Матрицю згенеровано!")
        except ValueError:
            self.display_message("Помилка: Введіть коректні розміри матриці.", is_error=True)

    def calculate_sum(self):
        """Обчислення суми елементів парних або непарних стовпців"""
        try:
            even = self.ui.comboBox.currentText() == "Парні стовпці"
            total_sum = self.matrix_handler.sum_columns(even=even)
            self.display_message(f"Сума: {total_sum}")
        except ValueError as e:
            self.display_message(f"Помилка обчислення суми: {str(e)}", is_error=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixSumApp()
    window.show()
    sys.exit(app.exec())
