from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QListWidget,
                               QPushButton, QLineEdit, QLabel, QComboBox, QHBoxLayout)
from lab9.ui.task3_interface import Ui_MainWindow

class PhoneBookApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def apply_styles(self, style_file_path):
        """Застосування стилів з файлу CSS"""
        with open(style_file_path, "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def show_message(self, message, is_error=False):
        """Відображення повідомлення"""
        color = "red" if is_error else "green"
        self.ui.label_status.setStyleSheet(f"color: {color};")
        self.ui.label_status.setText(message)

    def setup_connections(self):
        """Налаштування зв'язків кнопок"""
        self.ui.pushButton_add_contact.clicked.connect(self.add_contact)
        self.ui.pushButton_edit_contact.clicked.connect(self.edit_contact)

    def add_contact(self):
        """Додавання контакту"""
        pass

    def edit_contact(self):
        """Редагування контакту"""
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = PhoneBookApp()
    window.show()
    app.exec()
