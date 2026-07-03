import sys, math
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from lab10.ui.calculator_interface import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(420, 520)

        self.__stack = []
        self.additional_buttons = []

        self.memory_value = None

        # Підключення кнопок до одного методу через sender()
        self.connect_buttons()

        # Змінна для контролю видимості додаткових кнопок
        self.additional_buttons_visible = False

        # Додавання кнопок для роботи з пам'яттю
        self.add_memory_buttons()

    def add_memory_buttons(self):
        """Створення кнопок для роботи з пам'яттю"""
        button_MS = QPushButton("MS")
        button_MR = QPushButton("MR")
        button_MC = QPushButton("MC")
        button_M_plus = QPushButton("M+")
        button_M_minus = QPushButton("M-")

        self.ui.gridLayout_3.addWidget(button_MS, 4, 0)
        self.ui.gridLayout_3.addWidget(button_MR, 4, 1)
        self.ui.gridLayout_3.addWidget(button_MC, 4, 2)
        self.ui.gridLayout_3.addWidget(button_M_plus, 4, 3)
        self.ui.gridLayout_3.addWidget(button_M_minus, 4, 4)

        button_MS.clicked.connect(self.memory_store)
        button_MR.clicked.connect(self.memory_recall)
        button_MC.clicked.connect(self.memory_clear)
        button_M_plus.clicked.connect(self.memory_plus)
        button_M_minus.clicked.connect(self.memory_minus)

    def connect_buttons(self):
        """Підключення кнопок до методу button_clicked"""
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
        """Метод для обробки натискання кнопок"""
        button = self.sender()
        if button:
            # Вставлення тексту кнопки у поле вводу
            if self.ui.lineEdit.text() == "Error":
                self.ui.lineEdit.clear()
            self.ui.lineEdit.insert(button.text())

    def reset_values(self):
        """Метод для скидання всіх значень"""
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

        self.__stack.clear()

    def add_decimal_point(self):
        """Метод для додавання десяткової точки"""
        current_text = self.ui.lineEdit.text()

        if (len(current_text) == 0 or
            current_text[-1] == '-' or
            '.' in current_text):
            return

        self.ui.lineEdit.setText(current_text + '.')

    def change_sign(self):
        """Метод для зміни знака числа"""
        current_text = self.ui.lineEdit.text()

        if len(current_text) == 0 or current_text[0] != '-':
            self.ui.lineEdit.setText('-' + current_text)
        else:
            self.ui.lineEdit.setText(current_text[1:])  # Видалення знаку мінус

    def calculate(self, sgn):
        """Метод для обчислення арифметичних операцій"""
        current_text = self.ui.lineEdit.text()

        # Перевірка, чи щось введено
        if len(current_text) == 0:
            return

        # Якщо в стеку не менше двох елементів
        if len(self.__stack) >= 2:
            val2 = float(current_text)  # Другий операнд
            sign = self.__stack.pop()  # Отримання зі стека знаку
            val1 = float(self.__stack.pop())  # Отримання зі стека першого операнду

            if sign == "+":
                self.__stack.append(str(val1 + val2))
            elif sign == "-":
                self.__stack.append(str(val1 - val2))
            elif sign == "*":
                self.__stack.append(str(val1 * val2))
            elif sign == "/":
                if val2 == 0:
                    self.__stack.append(str(val1))
                else:
                    self.__stack.append(str(val1 / val2))
            elif sign == "^":
                self.__stack.append(str(val1 ** val2))

            self.__stack.append(sgn)
        else:
            self.__stack.append(current_text)
            self.__stack.append(sgn)

        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.setText("".join(self.__stack))

    def calculate_equal(self):
        """Метод для обчислення виразу"""
        if len(self.ui.lineEdit.text()) != 0 and len(self.__stack) == 2:
            self.__stack.append(self.ui.lineEdit.text())

        if len(self.__stack) < 3:
            return  # Якщо немає достатньо елементів для обчислення

        # Зчитування значень зі стека
        val2 = float(self.__stack.pop())  # Другий операнд
        sign = self.__stack.pop()          # Знак
        val1 = float(self.__stack.pop())   # Перший операнд

        # Виконання обчислення та додавання результату до стека
        if sign == "+":
            self.__stack.append(str(val1 + val2))
        elif sign == "-":
            self.__stack.append(str(val1 - val2))
        elif sign == "*":
            self.__stack.append(str(val1 * val2))
        elif sign == "/":
            if val2 == 0:
                self.__stack.append(str(val1))
                self.__stack.append(sign)
                self.ui.lineEdit.clear()
                return
            self.__stack.append(str(val1 / val2))
        elif sign == "^":
            self.__stack.append(str(val1 ** val2))

        # Оновлення поля вводу
        self.ui.lineEdit.setText(self.__stack.pop())
        self.ui.lineEdit_2.setText("".join(self.__stack))

    def toggle_additional_buttons(self):
        """Метод для перемикання видимості додаткових кнопок"""
        if self.additional_buttons_visible:
            self.setFixedSize(430, 520)
            self.remove_additional_buttons()
        else:
            self.setFixedSize(650, 520)
            self.add_additional_buttons()

    def add_additional_buttons(self):
        """Створення додаткових кнопок для функцій"""

        # Список назв функцій та їх відповідних методів
        functions = [
            ("sin", lambda : self.additional_operation(math.sin)),
            ("cos", lambda : self.additional_operation(math.cos)),
            ("tg", lambda : self.additional_operation(math.tan)),
            ("lg", lambda : self.additional_operation(math.log10)),
            ("ln", lambda : self.additional_operation(math.log)),
            ("sqrt", lambda : self.additional_operation(math.sqrt)),
            ("x^2", lambda : self.additional_operation(lambda x: x ** 2)),
            ("x^3", lambda : self.additional_operation(lambda x: x ** 3)),
            ("x^y", lambda : self.calculate("^")),
            ("1/x", lambda : self.additional_operation(lambda x: 1 / x)),
            ("10^x", lambda : self.additional_operation(lambda x: 10 ** x)),
            ("x!", lambda : self.additional_operation(math.factorial)),
        ]

        for i, (name, method) in enumerate(functions):
            button = QPushButton(name)
            button.setMinimumSize(75, 75)
            button.setMaximumSize(75, 75)
            button.clicked.connect(method)
            self.ui.gridLayout_2.addWidget(button, i // 3, i % 3)  # i // 3 — рядок, i % 3 — стовпець
            self.additional_buttons.append(button)

        self.additional_buttons_visible = True

    def additional_operation(self, operation):
        """Метод для виконання додаткових операцій"""
        current_text = self.ui.lineEdit.text()

        if not len(current_text):
            return
        try:
            number = int(current_text) if operation == math.factorial else float(current_text)
            result = operation(number)
            self.ui.lineEdit.setText(str(result))
        except Exception as e:
            self.ui.lineEdit.setText("Error")
            print(f"Error: {str(e)}")

    def remove_additional_buttons(self):
        """Видалення додаткових кнопок"""
        for button in self.additional_buttons:
            button.deleteLater()
        self.additional_buttons.clear()

        self.additional_buttons_visible = False

    def memory_store(self):
        """Збереження значення у пам'ять"""
        current_text = self.ui.lineEdit.text()
        if current_text:
            self.memory_value = float(current_text)

    def memory_recall(self):
        """Відображення значення з пам'яті"""
        if self.memory_value is not None:
            self.ui.lineEdit.setText(str(self.memory_value))

    def memory_clear(self):
        """Очищення пам'яті"""
        self.memory_value = None

    def memory_plus(self):
        """Додавання значення до пам'яті"""
        current_text = self.ui.lineEdit.text()
        if current_text:
            if self.memory_value is None:
                self.memory_value = 0
            self.memory_value += float(current_text)

    def memory_minus(self):
        """Віднімання значення від пам'яті"""
        current_text = self.ui.lineEdit.text()
        if current_text:
            if self.memory_value is None:
                self.memory_value = 0
            self.memory_value -= float(current_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.setWindowTitle("Calculator")
    window.show()
    sys.exit(app.exec())
