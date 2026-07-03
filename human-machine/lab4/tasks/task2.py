import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from lab4.ui.number_operations import Ui_MainWindow


class VariableCheckApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.process_values)

    def process_values(self):
        try:
            x = float(self.ui.lineEditX.text())
            y = float(self.ui.lineEditY.text())
            z = float(self.ui.lineEditZ.text())

            if (x < y < z) or (x > y > z):
                # Подвоїти значення
                x, y, z = x * 2, y * 2, z * 2
                result_message = f"Подвоєні значення: X = {x}, Y = {y}, Z = {z}"
            else:
                # Замінити значення на протилежні
                x, y, z = -x, -y, -z
                result_message = f"Протилежні значення: X = {x}, Y = {y}, Z = {z}"

            self.show_message(result_message)

        except ValueError:
            self.show_message("Будь ласка, введіть коректні числові значення.")

    def show_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setText(message)
        msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VariableCheckApp()
    window.show()
    sys.exit(app.exec())
