import sys
from PySide6.QtWidgets import QApplication
from lab5.utils.matrix_handler import MatrixHandler
from lab5.utils.base_widget import BaseWidget
from lab5.ui.task4_interface import Ui_Form


class MatrixTransform(BaseWidget):
    def __init__(self):
        super().__init__(Ui_Form)
        self.matrix_handler = MatrixHandler()

        # Налаштування зв'язків кнопок
        self.setup_connections()

    def setup_connections(self):
        """Налаштування зв'язків кнопок"""
        self.ui.pushButton_create_matrix.clicked.connect(self.create_matrix)
        self.ui.pushButton_transform_matrix.clicked.connect(self.transform_matrix)

    def create_matrix(self):
        """Генерує випадкову матрицю та відображає її"""
        try:
            m = int(self.ui.m_input.text())
            n = int(self.ui.n_input.text())
            self.matrix_handler.generate_matrix(m, n)
            self.display_matrix(self.matrix_handler.matrix)
            self.display_message("Матрицю згенеровано!")
        except ValueError as e:
            self.display_message(str(e), error=True)

    def transform_matrix(self):
        """Перетворює матрицю: міняє місцями мінімальний і максимальний елементи"""
        try:
            transformed_matrix = self.matrix_handler.swap_min_max_in_rows()
            self.display_matrix(transformed_matrix)
            self.display_message("Матриця перетворена!")
        except ValueError as e:
            self.display_message(str(e), error=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixTransform()
    window.show()
    sys.exit(app.exec())
