from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit,
                               QRadioButton, QPushButton, QButtonGroup, QMessageBox)
import sys

class PhoneBook(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Product Checker")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhoneBook()
    window.show()
    sys.exit(app.exec())
