# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task3_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_phone_book1 = QLabel(self.centralwidget)
        self.label_phone_book1.setObjectName(u"label_phone_book1")

        self.verticalLayout.addWidget(self.label_phone_book1)

        self.list_phone_book1 = QTextEdit(self.centralwidget)
        self.list_phone_book1.setObjectName(u"list_phone_book1")
        self.list_phone_book1.setEnabled(False)

        self.verticalLayout.addWidget(self.list_phone_book1)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_phone_book2 = QLabel(self.centralwidget)
        self.label_phone_book2.setObjectName(u"label_phone_book2")

        self.verticalLayout_2.addWidget(self.label_phone_book2)

        self.list_phone_book2 = QTextEdit(self.centralwidget)
        self.list_phone_book2.setObjectName(u"list_phone_book2")
        self.list_phone_book2.setEnabled(False)

        self.verticalLayout_2.addWidget(self.list_phone_book2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_phone_book1 = QRadioButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_phone_book1)
        self.radioButton_phone_book1.setObjectName(u"radioButton_phone_book1")
        self.radioButton_phone_book1.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_phone_book1)

        self.radioButton_phone_book2 = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.radioButton_phone_book2)
        self.radioButton_phone_book2.setObjectName(u"radioButton_phone_book2")

        self.horizontalLayout_3.addWidget(self.radioButton_phone_book2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.input_name = QLineEdit(self.centralwidget)
        self.input_name.setObjectName(u"input_name")

        self.verticalLayout_3.addWidget(self.input_name)

        self.input_phone_number = QLineEdit(self.centralwidget)
        self.input_phone_number.setObjectName(u"input_phone_number")

        self.verticalLayout_3.addWidget(self.input_phone_number)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_add_contact = QPushButton(self.centralwidget)
        self.pushButton_add_contact.setObjectName(u"pushButton_add_contact")

        self.horizontalLayout_2.addWidget(self.pushButton_add_contact)

        self.pushButton_edit_contact = QPushButton(self.centralwidget)
        self.pushButton_edit_contact.setObjectName(u"pushButton_edit_contact")

        self.horizontalLayout_2.addWidget(self.pushButton_edit_contact)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_swap_phone_books = QPushButton(self.centralwidget)
        self.pushButton_swap_phone_books.setObjectName(u"pushButton_swap_phone_books")

        self.verticalLayout_5.addWidget(self.pushButton_swap_phone_books)

        self.pushButton_clear_phone_books = QPushButton(self.centralwidget)
        self.pushButton_clear_phone_books.setObjectName(u"pushButton_clear_phone_books")

        self.verticalLayout_5.addWidget(self.pushButton_clear_phone_books)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout_6.addWidget(self.label_status)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 10)
        self.verticalLayout_6.setStretch(2, 3)
        self.verticalLayout_6.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u0438\u0439 \u0434\u043e\u0432\u0456\u0434\u043d\u0438\u043a", None))
        self.label_phone_book1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u0430 \u043a\u043d\u0438\u0433\u0430 1", None))
        self.label_phone_book2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u0430 \u043a\u043d\u0438\u0433\u0430 2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0430\u0431\u043e \u0440\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.radioButton_phone_book1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u0430 \u043a\u043d\u0438\u0433\u0430 1", None))
        self.radioButton_phone_book2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u0430 \u043a\u043d\u0438\u0433\u0430 2", None))
        self.input_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0406\u043c'\u044f", None))
        self.input_phone_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0443", None))
        self.pushButton_add_contact.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.pushButton_edit_contact.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.pushButton_swap_phone_books.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043c\u0456\u043d \u0432\u043c\u0456\u0441\u0442\u0443 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u0438\u0445 \u043a\u043d\u0438\u0433", None))
        self.pushButton_clear_phone_books.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u0438 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u0456 \u043a\u043d\u0438\u0433\u0438", None))
        self.label_status.setText("")
    # retranslateUi

