from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication

app = QApplication([])

# Створюємо об'єкт QFile
file = QFile("example.txt")

# Відкриваємо файл у режимі читання
if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):  # Використовуємо OpenModeFlag
    # Читаємо вміст файлу
    # file.readAll() повертає QByteArray, який містить вміст файлу
    # data() повертає байтовий масив, який містить вміст QByteArray
    # decode() перетворює байтовий масив у рядок str
    content = file.readAll().data().decode()
    print(content)
    # Закриваємо файл
    file.close()
else:
    print("Не вдалося відкрити файл.")

app.exec()
