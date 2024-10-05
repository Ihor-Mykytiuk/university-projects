# base_widget.py
from PySide6.QtWidgets import QWidget

class BaseWidget(QWidget):
    def __init__(self, Ui_Form):
        super().__init__()

        # Ініціалізація інтерфейсу
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.apply_styles("../static/styles/styles.qss")


    def apply_styles(self, style_file_path):
        """Застосування стилів з файлу CSS"""
        with open(style_file_path, "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

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
