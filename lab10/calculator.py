import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from calculator_interface import Ui_Form  # Імпорт згенерованого файлу

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу з файлу calculator_interface.py
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Оголошення стека (аналог QStack)
        self.__stack = []  # Приватна змінна для стека значень

        # Підключення кнопок до одного методу через sender()
        self.connect_buttons()

    def connect_buttons(self):
        # Підключаємо всі кнопки до одного слота, який використовує sender()
        self.ui.pushButton_1.clicked.connect(self.button_clicked)
        self.ui.pushButton_2.clicked.connect(self.button_clicked)
        self.ui.pushButton_3.clicked.connect(self.button_clicked)
        self.ui.pushButton_4.clicked.connect(self.button_clicked)
        self.ui.pushButton_5.clicked.connect(self.button_clicked)
        self.ui.pushButton_6.clicked.connect(self.button_clicked)
        self.ui.pushButton_7.clicked.connect(self.button_clicked)
        self.ui.pushButton_8.clicked.connect(self.button_clicked)
        self.ui.pushButton_9.clicked.connect(self.button_clicked)

        # Підключення кнопки для додавання десяткової точки
        self.ui.pushButton_decimal.clicked.connect(self.add_decimal_point)

        # Підключення кнопки для зміни знака
        self.ui.pushButton_change_sign.clicked.connect(self.change_sign)

        # Підключення кнопки скидання до методу reset_values
        self.ui.pushButton_clear.clicked.connect(self.reset_values)

    def button_clicked(self):
        # Отримуємо кнопку, яка надіслала сигнал
        button = self.sender()
        if button:
            # Вставляємо текст кнопки (цифру) в поле введення
            self.ui.lineEdit.insert(button.text())

    # Слот для скидання значень
    def reset_values(self):
        # Очищуємо обидва поля введення
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

        # Очищуємо стек
        self.__stack.clear()

    # Слот для додавання десяткової точки
    def add_decimal_point(self):
        # Отримуємо поточний текст з поля вводу
        current_text = self.ui.lineEdit.text()

        # Перевірка умов:
        if (len(current_text) == 0 or
            current_text[-1] == '-' or
            '.' in current_text):
            return

        # Якщо умови виконані, додаємо десяткову точку
        self.ui.lineEdit.setText(current_text + '.')

    # Слот для зміни знака числа
    def change_sign(self):
        current_text = self.ui.lineEdit.text()

        # Перевірка умов для зміни знака
        if len(current_text) == 0 or current_text[0] != '-':
            self.ui.lineEdit.setText('-' + current_text)
        else:
            self.ui.lineEdit.setText(current_text[1:])  # Видаляємо знак '-'

    # Оголошення методу для обробки арифметичних дій
    def calculate(self, sgn):
        pass  # Пізніше цей метод буде реалізований

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.setWindowTitle("Calculator")
    window.show()
    sys.exit(app.exec())
