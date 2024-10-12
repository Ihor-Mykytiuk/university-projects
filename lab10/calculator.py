import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from calculator_interface import Ui_Form  # Імпорт згенерованого файлу

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу з файлу ui_calculator.py
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Підключення кнопок до одного методу через sender()
        self.connect_buttons()

    def connect_buttons(self):
        # Підключаємо всі кнопки до одного слота, який використовує sender()
        self.ui.pushButton_0.clicked.connect(self.button_clicked)
        self.ui.pushButton_1.clicked.connect(self.button_clicked)
        self.ui.pushButton_2.clicked.connect(self.button_clicked)
        self.ui.pushButton_3.clicked.connect(self.button_clicked)
        self.ui.pushButton_4.clicked.connect(self.button_clicked)
        self.ui.pushButton_5.clicked.connect(self.button_clicked)
        self.ui.pushButton_6.clicked.connect(self.button_clicked)
        self.ui.pushButton_7.clicked.connect(self.button_clicked)
        self.ui.pushButton_8.clicked.connect(self.button_clicked)
        self.ui.pushButton_9.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # Отримуємо кнопку, яка надіслала сигнал
        button = self.sender()
        if button:
            # Вставляємо текст кнопки (цифру) в поле введення
            self.ui.lineEdit.insert(button.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.setWindowTitle("Calculator")
    window.show()
    sys.exit(app.exec())