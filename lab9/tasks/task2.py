import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QButtonGroup, QGroupBox, QMainWindow, QGridLayout,
                               QCheckBox)
from lab9.ui.task2_interface import Ui_MainWindow


class ProductCheckerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ініціалізація інтерфейсу
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Набір товарів
        self.products = {
            "Хліб", "Кефір", "Молоко", "Цукор", "Сіль", "Картопля", "Морква", "Цибуля", "Капуста", "Помідори", "Яблука",
        }
        self.stores = {}
        self.stores_buttons = {}

        # Створення контейнера для контенту в QScrollArea
        self.scroll_content = QWidget()
        self.grid_layout = QGridLayout(self.scroll_content)
        self.scroll_content.setLayout(self.grid_layout)

        self.ui.scrollArea.setWidget(self.scroll_content)

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
        self.ui.pushButton_add_store.clicked.connect(self.add_store)
        self.ui.pushButton_process_products.clicked.connect(self.process_products)

    @staticmethod
    def clear_layout(layout):
        """Очищення всіх віджетів з layout"""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def update_stores_list(self):
        """Оновлення списку магазинів"""
        self.clear_layout(self.grid_layout)
        # Рядок і колонка для сітки
        row = 0
        col = 0

        for (store_name, products) in self.stores.items():
            # Група для кожного магазину
            store_group = QGroupBox(store_name)
            store_layout = QVBoxLayout()

            # Група радіокнопок для цього магазину
            store_buttons = QButtonGroup()
            store_buttons.setExclusive(False)
            self.stores_buttons[store_name] = store_buttons
            for product in self.products:
                checkbox = QCheckBox(product)
                store_buttons.addButton(checkbox)
                store_layout.addWidget(checkbox)
            store_group.setLayout(store_layout)
            self.grid_layout.addWidget(store_group, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

    def add_store(self):
        """Додавання магазину"""
        store_name = self.ui.input_store_name.text().strip()
        if not store_name:
            self.show_message("Помилка: Будь ласка, введіть назву магазину.", is_error=True)
            return
        if store_name in self.stores:
            self.show_message(f"Помилка: Магазин {store_name} вже є у списку.", is_error=True)
        else:
            self.stores[store_name] = set()
            self.update_stores_list()
            self.show_message(f"Магазин {store_name} був успішно доданий.")
            self.ui.input_store_name.clear()

    def process_buttons_group(self):
        """Обробка вибраних товарів у магазинах"""
        for store_name, store_buttons in self.stores_buttons.items():
            store_products = set()
            for checkbox in store_buttons.buttons():
                if checkbox.isChecked():
                    store_products.add(checkbox.text())
            self.stores[store_name] = store_products
        self.show_message("Товари в магазинах успішно оброблено.")
        print(self.stores)

    def process_products(self):
        """Обробка товарів"""
        self.process_buttons_group()
        products_in_all_stores = set.intersection(*self.stores.values())
        products_in_at_least_one_shop = set.union(*self.stores.values())
        products_in_no_shop = self.products.difference(products_in_at_least_one_shop)

        self.ui.label_products_in_all_stores.setText(", ".join(products_in_all_stores))
        self.ui.label_products_in_at_least_one_shop.setText(", ".join(products_in_at_least_one_shop))
        self.ui.label_products_in_no_shop.setText(", ".join(products_in_no_shop))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductCheckerApp()
    window.show()
    sys.exit(app.exec())
