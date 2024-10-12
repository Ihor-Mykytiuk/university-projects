import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from calculator_interface import Ui_Form  # Імпорт згенерованого файлу

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу з файлу calculator_interface.py
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(430, 520)  # Фіксуємо розмір вікна
        # Оголошення стека (аналог QStack)
        self.__stack = []  # Приватна змінна для стека значень

        # Підключення кнопок до одного методу через sender()
        self.connect_buttons()

        # Змінна для контролю видимості додаткових кнопок
        self.additional_buttons_visible = False

    def connect_buttons(self):
        # Підключаємо всі кнопки до одного слота, який використовує sender()
        for i in range(10):
            getattr(self.ui, f"pushButton_{i}").clicked.connect(self.button_clicked)

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

        # Підключення кнопки для додаткових функцій
        self.ui.pushButton_additional.clicked.connect(self.toggle_additional_buttons)

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

    def calculate_cos(self):
        # Логіка для косинуса
        pass

    def calculate_log10(self):
        # Логіка для логарифму
        pass

    def calculate_x_squared(self):
        # Логіка для x^2
        pass

    def calculate_sqrt(self):
        # Логіка для кореня
        pass

    def calculate_sin(self):
        # Логіка для синуса
        pass

    def calculate_ln(self):
        # Логіка для натурального логарифму
        pass

    def calculate_inverse(self):
        # Логіка для 1/x
        pass

    def calculate_tg(self):
        # Логіка для тангенса
        pass

    def calculate_10_power(self):
        # Логіка для 10^x
        pass

    def calculate_x_cubed(self):
        # Логіка для x^3
        pass

    def calculate_x_y(self):
        # Логіка для x^y
        pass

    def calculate_factorial(self):
        # Логіка для факторіалу
        pass

    def toggle_additional_buttons(self):
        # Додаємо або прибираємо додаткові кнопки
        if self.additional_buttons_visible:
            self.setFixedSize(430, 520)
            self.remove_additional_buttons()
        else:
            self.setFixedSize(700, 520)
            self.add_additional_buttons()

    def add_additional_buttons(self):
        # Створюємо нові кнопки для додаткових функцій
        self.additional_buttons = []

        # Список назв функцій та їх відповідних методів
        functions = [
            ("sin", self.calculate_sin),
            ("cos", self.calculate_cos),
            ("tg", self.calculate_tg),
            ("lg", self.calculate_log10),
            ("ln", self.calculate_ln),
            ("sqrt", self.calculate_sqrt),
            ("x^2", self.calculate_x_squared),
            ("x^3", self.calculate_x_cubed),
            ("x^y", self.calculate_x_y),
            ("1/x", self.calculate_inverse),
            ("10^x", self.calculate_10_power),
            ("x!", self.calculate_factorial)
        ]

        # Додаємо кнопки до грід-сітки
        for i, (name, method) in enumerate(functions):
            button = QPushButton(name)
            button.setMinimumSize(75, 75)
            button.setMaximumSize(75, 75)
            button.clicked.connect(method)
            # Додаємо кнопку в грід-сітку
            self.ui.gridLayout_2.addWidget(button, i // 3, i % 3)  # i // 3 — рядок, i % 3 — стовпець
            self.additional_buttons.append(button)

        self.additional_buttons_visible = True

    def remove_additional_buttons(self):
        # Прибираємо додаткові кнопки
        for button in self.additional_buttons:
            button.deleteLater()  # Видаляємо кнопку з пам'яті
        self.additional_buttons.clear()

        self.additional_buttons_visible = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.setWindowTitle("Calculator")
    window.show()
    sys.exit(app.exec())
