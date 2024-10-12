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

        # Підключення кнопки для додавання десяткової точки
        self.ui.pushButton_decimal.clicked.connect(self.add_decimal_point)

        # Підключення кнопки для зміни знака
        self.ui.pushButton_change_sign.clicked.connect(self.change_sign)

        # Підключення кнопки скидання до методу reset_values
        self.ui.pushButton_clear.clicked.connect(self.reset_values)

        # Підключення кнопок для арифметичних дій
        self.ui.pushButton_plus.clicked.connect(lambda: self.calculate("+"))
        self.ui.pushButton_minus.clicked.connect(lambda: self.calculate("-"))
        self.ui.pushButton_multiply.clicked.connect(lambda: self.calculate("*"))
        self.ui.pushButton_divide.clicked.connect(lambda: self.calculate("/"))

        # Підключення кнопки для рівності
        self.ui.pushButton_equal.clicked.connect(self.calculate_equal)

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
        current_text = self.ui.lineEdit.text()

        # Перевірка, чи щось введено
        if len(current_text) == 0:
            return  # Виходимо, якщо нічого не введено

        # Якщо в стеку не менше двох елементів
        if len(self.__stack) >= 2:
            val2 = float(current_text)  # Перетворюємо текст у число
            sign = self.__stack.pop()  # Витягуємо знак
            val1 = float(self.__stack.pop())  # Витягуємо перший операнд

            # Виконуємо обчислення
            if sign == "+":
                self.__stack.append(str(val1 + val2))
            elif sign == "-":
                self.__stack.append(str(val1 - val2))
            elif sign == "*":
                self.__stack.append(str(val1 * val2))
            elif sign == "/":
                if val2 == 0:
                    self.__stack.append(str(val1))  # Додаємо перший операнд, якщо ділимо на 0
                else:
                    self.__stack.append(str(val1 / val2))

            self.__stack.append(sgn)  # Додаємо натиснутий знак

        else:
            self.__stack.append(current_text)  # Якщо стек порожній, додаємо значення
            self.__stack.append(sgn)  # Додаємо знак

        self.ui.lineEdit.clear()  # Очищуємо перше поле
        self.ui.lineEdit_2.setText("".join(self.__stack))  # Виводимо значення у друге поле

    # Слот для обробки рівності
    def calculate_equal(self):
        # Якщо введено число та в стеку два елементи
        if len(self.ui.lineEdit.text()) != 0 and len(self.__stack) == 2:
            self.__stack.append(self.ui.lineEdit.text())

        if len(self.__stack) < 3:
            return  # Якщо в стеку менш як три елементи, виходимо

        # Витягуємо з стека числа і знак операції
        val2 = float(self.__stack.pop())  # Другий операнд
        sign = self.__stack.pop()          # Знак
        val1 = float(self.__stack.pop())   # Перший операнд

        # Виконуємо обчислення та додаємо результат у стек
        if sign == "+":
            self.__stack.append(str(val1 + val2))
        elif sign == "-":
            self.__stack.append(str(val1 - val2))
        elif sign == "*":
            self.__stack.append(str(val1 * val2))
        elif sign == "/":
            if val2 == 0:
                self.__stack.append(str(val1))  # Додаємо перший операнд, якщо ділимо на 0
                self.__stack.append(sign)         # Додаємо знак
                self.ui.lineEdit.clear()
                return
            self.__stack.append(str(val1 / val2))

        # Оновлюємо поля вводу
        self.ui.lineEdit.setText(self.__stack.pop())  # Виводимо результат у перше поле
        self.ui.lineEdit_2.setText("".join(self.__stack))  # Виводимо значення у друге поле


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.setWindowTitle("Calculator")
    window.show()
    sys.exit(app.exec())
