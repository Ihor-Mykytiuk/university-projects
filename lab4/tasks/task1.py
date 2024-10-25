import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from lab4.ui.number_description import Ui_MainWindow


class NumberDescriptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.describe_number)

    def describe_number(self):
        text = self.ui.lineEdit.text()

        try:
            number = int(text)
            description = self.get_number_description(number)
            self.show_message(description)
        except ValueError:
            self.show_message("Будь ласка, введіть коректне число.")

    @staticmethod
    def get_number_description(number):
        if number == 0:
            return "Нульове число"

        # Опис позитивного або негативного числа
        sign_description = "Позитивне" if number > 0 else "Негативне"

        # Опис однозначного, двозначного чи тризначного числа
        abs_number = abs(number)
        if abs_number < 10:
            digit_description = "однозначне число"
        elif abs_number < 100:
            digit_description = "двозначне число"
        else:
            digit_description = "тризначне число"

        return f"{sign_description} {digit_description}"

    def show_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setText(message)
        msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumberDescriptionApp()
    window.show()
    sys.exit(app.exec())
