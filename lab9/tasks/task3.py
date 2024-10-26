from PySide6.QtWidgets import (QApplication, QMainWindow)

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
        # Оновлення списку контактів
        self.update_lists()

        # Налаштування зв'язків кнопок
        self.setup_connections()

        # Застосування стилів
        self.apply_styles("static/styles/styles.qss")


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
        self.ui.pushButton_swap_phone_books.clicked.connect(self.swap_phone_books)
        self.ui.pushButton_clear_phone_books.clicked.connect(self.clear_phone_books)

    def update_lists(self):
        """Оновлення списку контактів"""
        phone_book1 = "\n".join([f"{name}: {group}" for name, group in self.phone_book1.items()])
        phone_book2 = "\n".join([f"{name}: {group}" for name, group in self.phone_book2.items()])

        self.ui.list_phone_book1.setText(phone_book1)
        self.ui.list_phone_book2.setText(phone_book2)

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

    def swap_phone_books(self):
        """Обмін контактів між телефонними книгами"""
        self.phone_book1, self.phone_book2 = self.phone_book2, self.phone_book1
        self.update_lists()
        self.show_message("Контакти обмінено")

    def clear_phone_books(self):
        """Очищення телефонних книг"""
        self.phone_book1.clear()
        self.phone_book2.clear()
        self.update_lists()
        self.show_message("Телефонні книги очищено")


if __name__ == "__main__":
    app = QApplication([])
    window = PhoneBookApp()
    window.show()
    app.exec()
