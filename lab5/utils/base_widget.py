#base_widget.py
from PySide6.QtWidgets import QWidget


class BaseWidget(QWidget):
    def __init__(self, Ui_Form):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.apply_styles("../../static/styles/styles.qss")

    def apply_styles(self, style_file_path):
        """Застосування стилів з файлу CSS"""
        with open(style_file_path, "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def display_array(self, array):
        """Відображає масив у QLabel"""
        self.ui.array_result.setText(", ".join(map(str, array)))

    def display_matrix(self, matrix):
        """Відображає матрицю у QLabel"""
        self.ui.array_result.setText("\n".join(" ".join(map(str, row)) for row in matrix))

    def display_message(self, message, error=False):
        """Виводить повідомлення у QLabel для статусу."""
        color = "red" if error else "green"
        self.ui.status_label.setStyleSheet(f"color: {color};")
        self.ui.status_label.setText(message)

    def input_changed(self):
        """Блокує одне поле, якщо введено дані в інше."""
        size_text = self.ui.size_input.text()
        array_text = self.ui.array_input.text()

        # Якщо є текст в одному з полів, блокуємо інше
        self.ui.array_input.setDisabled(bool(size_text))
        self.ui.size_input.setDisabled(bool(array_text))