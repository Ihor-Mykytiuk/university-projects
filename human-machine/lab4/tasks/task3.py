import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from lab4.ui.student_login import Ui_MainWindow


class StudentLoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.authenticate_user)

    def authenticate_user(self):
        username = self.ui.lineEditLogin.text()
        password = self.ui.lineEditPassword.text()

        # Простий приклад перевірки
        if username == "student" and password == "password":
            self.show_message("Авторизація успішна!")
        else:
            self.show_message("Неправильний логін або пароль.")

    def show_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setText(message)
        msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentLoginApp()
    window.show()
    sys.exit(app.exec())