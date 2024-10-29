from PySide6.QtWidgets import QMainWindow


class BaseWidget(QMainWindow):
    def __init__(self, Ui_MainWindow):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.apply_styles("static/styles/styles.qss")

    def apply_styles(self, style_file_path):
        """Застосування стилів з файлу CSS"""
        with open(style_file_path, "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def display_array(self, array):
        """Відображає масив у QLabel"""
        self.ui.label_result_array.setText(" ".join(map(str, array)))

    def display_matrix(self, matrix):
        """Відображає матрицю у QLabel"""
        self.ui.label_result_matrix.setText("\n".join(" ".join(map(str, row)) for row in matrix))

    def display_message(self, message, is_error=False):
        """Виводить повідомлення у QLabel для статусу."""
        color = "red" if is_error else "green"
        self.ui.label_status.setStyleSheet(f"color: {color};")
        self.ui.label_status.setText(message)

    def input_changed(self):
        """Блокує одне поле, якщо введено дані в інше."""
        size_text = self.ui.input_size.text()
        array_text = self.ui.input_array.text()

        # Якщо є текст в одному з полів, блокуємо інше
        self.ui.input_array.setDisabled(bool(size_text))
        self.ui.input_size.setDisabled(bool(array_text))