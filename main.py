import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from simple_ui import Ui_MainWindow  # Імпортуйте згенерований інтерфейс

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Зберігайте групи кнопок у словнику
        self.button_groups = {
            self.ui.buttonGroup1: None,
            self.ui.buttonGroup2: None,
            # Додайте інші групи кнопок тут, наприклад:
            # self.ui.buttonGroup3: None,
            # self.ui.buttonGroup4: None,
        }

        # Підключення сигналу для кнопки результату
        self.ui.resultButton.clicked.connect(self.show_selected_radio_buttons)

    def save_selected_radio_buttons(self):
        # Зберігаємо вибрані кнопки в словник
        for button_group in self.button_groups:
            selected_button = button_group.checkedButton()
            self.button_groups[button_group] = selected_button.text() if selected_button else None

    def show_selected_radio_buttons(self):
        self.save_selected_radio_buttons()  # Зберігаємо значення перед виводом
        for i, (button_group, selected_value) in enumerate(self.button_groups.items()):
            if selected_value:
                print(f"Вибрано з групи {i + 1}: {selected_value}")
            else:
                print(f"Не вибрано жодної кнопки з групи {i + 1}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
