import math
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from lab10.ui.calculator_interface import Ui_MainWindow  # Імпорт згенерованого файлу

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу з файлу calculator_interface.py
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(420, 520)  # Фіксуємо розмір вікна
        # Оголошення стека (аналог QStack)
        self.__stack = []  # Приватна змінна для стека значень

        self.memory_value = None

        # Підключення кнопок до одного методу через sender()
        self.connect_buttons()

        # Змінна для контролю видимості додаткових кнопок
        self.additional_buttons_visible = False

        self.add_memory_buttons()

    def add_memory_buttons(self):
        # Створюємо кнопки для роботи з пам'яттю
        self.button_MS = QPushButton("MS")
        self.button_MR = QPushButton("MR")
        self.button_MC = QPushButton("MC")
        self.button_M_plus = QPushButton("M+")
        self.button_M_minus = QPushButton("M-")

        # Додаємо кнопки до gridLayout
        self.ui.gridLayout_3.addWidget(self.button_MS, 4, 0)
        self.ui.gridLayout_3.addWidget(self.button_MR, 4, 1)
        self.ui.gridLayout_3.addWidget(self.button_MC, 4, 2)
        self.ui.gridLayout_3.addWidget(self.button_M_plus, 4, 3)
        self.ui.gridLayout_3.addWidget(self.button_M_minus, 4, 4)

        self.button_MS.clicked.connect(self.memory_store)
        self.button_MR.clicked.connect(self.memory_recall)
        self.button_MC.clicked.connect(self.memory_clear)
        self.button_M_plus.clicked.connect(self.memory_plus)
        self.button_M_minus.clicked.connect(self.memory_minus)

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
            if self.ui.lineEdit.text() == "Error":
                self.ui.lineEdit.clear()
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
            elif sign == "^":
                self.__stack.append(str(val1 ** val2))

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
        elif sign == "^":
            self.__stack.append(str(val1 ** val2))

        # Оновлюємо поля вводу
        self.ui.lineEdit.setText(self.__stack.pop())  # Виводимо результат у перше поле
        self.ui.lineEdit_2.setText("".join(self.__stack))  # Виводимо значення у друге поле

    def toggle_additional_buttons(self):
        # Додаємо або прибираємо додаткові кнопки
        if self.additional_buttons_visible:
            self.setFixedSize(430, 520)
            self.remove_additional_buttons()
        else:
            self.setFixedSize(650, 520)
            self.add_additional_buttons()

    def add_additional_buttons(self):
        # Створюємо нові кнопки для додаткових функцій
        self.additional_buttons = []

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
    def additional_operation(self, operation):
        # Отримуємо поточний текст з поля вводу
        current_text = self.ui.lineEdit.text()

        # Перевірка, чи щось введено
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
        # Прибираємо додаткові кнопки
        for button in self.additional_buttons:
            button.deleteLater()  # Видаляємо кнопку з пам'яті
        self.additional_buttons.clear()

        self.additional_buttons_visible = False

    def memory_store(self):
        current_text = self.ui.lineEdit.text()
        if current_text:
            self.memory_value = float(current_text)

    def memory_recall(self):
        if self.memory_value is not None:
            self.ui.lineEdit.setText(str(self.memory_value))

    def memory_clear(self):
        self.memory_value = None

    def memory_plus(self):
        current_text = self.ui.lineEdit.text()
        if current_text:
            if self.memory_value is None:
                self.memory_value = 0
            self.memory_value += float(current_text)

    def memory_minus(self):
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
