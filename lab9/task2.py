from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit,
                             QPushButton, QLineEdit, QHBoxLayout, QGridLayout, QMessageBox)


class ShopInventory(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shop Inventory")

        # Список товарів для кожного магазину
        self.shop_goods = {
            "Магазин 1": set(),
            "Магазин 2": set(),
            "Магазин 3": set()
        }

        # Всі можливі товари
        self.all_goods = {"яблука", "банани", "апельсини", "груші", "виноград", "огірки", "помідори", "морква"}

        self.layout = QVBoxLayout()

        # Поля для введення товарів у кожен магазин
        self.shop_inputs = {}
        for shop in self.shop_goods:
            self.create_shop_input(shop)

        # Кнопки для виконання завдань
        self.create_buttons()

        # Текстове поле для відображення результатів
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        self.layout.addWidget(self.result_text)

        self.setLayout(self.layout)

    def create_shop_input(self, shop_name):
        """Створює поле для введення товарів для конкретного магазину"""
        label = QLabel(f"{shop_name}:", self)
        input_field = QLineEdit(self)
        input_field.setPlaceholderText(f"Введіть товари через кому для {shop_name}")

        self.shop_inputs[shop_name] = input_field

        self.layout.addWidget(label)
        self.layout.addWidget(input_field)

    def create_buttons(self):
        """Створює кнопки для різних завдань"""
        btn_layout = QHBoxLayout()

        btn_all_shops = QPushButton("Товари в кожному магазині", self)
        btn_any_shop = QPushButton("Товари в хоча б одному магазині", self)
        btn_missing = QPushButton("Товари, яких немає в жодному магазині", self)

        btn_all_shops.clicked.connect(self.find_common_goods)
        btn_any_shop.clicked.connect(self.find_any_goods)
        btn_missing.clicked.connect(self.find_missing_goods)

        btn_layout.addWidget(btn_all_shops)
        btn_layout.addWidget(btn_any_shop)
        btn_layout.addWidget(btn_missing)

        self.layout.addLayout(btn_layout)

    def find_common_goods(self):
        """Знаходить товари, що є у кожному магазині"""
        self.update_shop_data()

        # Знаходимо спільні товари
        common_goods = set.intersection(*self.shop_goods.values())
        self.show_result("Товари, які є в кожному магазині:", common_goods)

    def find_any_goods(self):
        """Знаходить товари, які є хоча б в одному магазині"""
        self.update_shop_data()

        # Знаходимо товари, що є хоча б в одному магазині
        any_goods = set.union(*self.shop_goods.values())
        self.show_result("Товари, які є хоча б в одному магазині:", any_goods)

    def find_missing_goods(self):
        """Знаходить товари, яких немає в жодному магазині"""
        self.update_shop_data()

        # Товари, яких немає в жодному магазині
        any_goods = set.union(*self.shop_goods.values())
        missing_goods = self.all_goods.difference(any_goods)
        self.show_result("Товари, яких немає в жодному магазині:", missing_goods)

    def update_shop_data(self):
        """Оновлює дані про товари в кожному магазині на основі введених користувачем даних"""
        for shop, input_field in self.shop_inputs.items():
            goods = input_field.text().replace(' ', '').split(',')
            self.shop_goods[shop] = set(goods) if goods != [''] else set()

    def show_result(self, title, goods_set):
        """Відображає результат у QTextEdit"""
        if goods_set:
            result_text = ", ".join(goods_set)
        else:
            result_text = "Нічого не знайдено."

        self.result_text.setText(f"{title}\n{result_text}")


if __name__ == "__main__":
    app = QApplication([])

    window = ShopInventory()
    window.show()

    app.exec()
