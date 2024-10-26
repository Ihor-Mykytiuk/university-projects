from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QListWidget,
                               QPushButton, QLineEdit, QLabel, QComboBox, QHBoxLayout)
from lab9.ui.task3_interface import Ui_MainWindow

class PhoneBookApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.phone_book1 = {
            "Василь": "123456789",
            "Петро": "987654321",
            "Іван": "456789123"
        }
        self.phone_book2 = {
            "Марія": "987654321",
            "Олена": "123456789",
            "Ірина": "456789123"
        }

        self.update_lists()
        self.setup_connections()


    def apply_styles(self, style_file_path):
        """Застосування стилів з файлу CSS"""
        with open(style_file_path, "r") as style_file:
            style = style_file.read()
            self.setStyleSheet(style)

    def show_message(self, message, is_error=False):
        """Відображення повідомлення"""
        color = "red" if is_error else "green"
        self.ui.label_status.setStyleSheet(f"color: {color};")
        self.ui.label_status.setText(message)

    def setup_connections(self):
        """Налаштування зв'язків кнопок"""
        self.ui.pushButton_add_contact.clicked.connect(self.add_contact)
        self.ui.pushButton_edit_contact.clicked.connect(self.edit_contact)

    def update_lists(self):
        """Оновлення списку контактів"""
        self.ui.listWidget_phone_book1.clear()
        self.ui.listWidget_phone_book2.clear()

        for name, phone in self.phone_book1.items():
            self.ui.listWidget_phone_book1.addItem(f"{name}: {phone}")

        for name, phone in self.phone_book2.items():
            self.ui.listWidget_phone_book2.addItem(f"{name}: {phone}")



    def add_contact(self):
        """Додавання контакту"""
        name = self.ui.input_name.text().strip()
        phone = self.ui.input_phone_number.text().strip()

        if not name or not phone:
            self.show_message("Заповніть всі поля", is_error=True)
            return

        if self.ui.radioButton_phone_book1.isChecked():
            self.phone_book1[name] = phone
        else:
            self.phone_book2[name] = phone

        self.update_lists()
        self.show_message("Контакт успішно додано")

    def edit_contact(self):
        """Редагування контакту"""
        name = self.ui.input_name.text().strip()
        phone = self.ui.input_phone_number.text().strip()

        if not name or not phone:
            self.show_message("Заповніть всі поля", is_error=True)
            return

        if self.ui.radioButton_phone_book1.isChecked():
            if name in self.phone_book1:
                self.phone_book1[name] = phone
                self.show_message("Контакт успішно відредаговано")
            else:
                self.show_message("Контакт не знайдено", is_error=True)
        else:
            if name in self.phone_book2:
                self.phone_book2[name] = phone
                self.show_message("Контакт успішно відредаговано")
            else:
                self.show_message("Контакт не знайдено", is_error=True)

        self.update_lists()



if __name__ == "__main__":
    app = QApplication([])
    window = PhoneBookApp()
    window.show()
    app.exec()
