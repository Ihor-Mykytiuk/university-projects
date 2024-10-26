# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task2_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.title)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_store_name = QLabel(self.centralwidget)
        self.label_store_name.setObjectName(u"label_store_name")

        self.verticalLayout_3.addWidget(self.label_store_name)

        self.input_store_name = QLineEdit(self.centralwidget)
        self.input_store_name.setObjectName(u"input_store_name")

        self.verticalLayout_3.addWidget(self.input_store_name)

        self.pushButton_add_store = QPushButton(self.centralwidget)
        self.pushButton_add_store.setObjectName(u"pushButton_add_store")

        self.verticalLayout_3.addWidget(self.pushButton_add_store)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea_content = QWidget()
        self.scrollArea_content.setObjectName(u"scrollArea_content")
        self.scrollArea_content.setGeometry(QRect(0, 0, 830, 476))
        self.scrollArea.setWidget(self.scrollArea_content)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.pushButton_process_products = QPushButton(self.centralwidget)
        self.pushButton_process_products.setObjectName(u"pushButton_process_products")

        self.verticalLayout_5.addWidget(self.pushButton_process_products)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_products_in_all_stores = QLabel(self.centralwidget)
        self.label_products_in_all_stores.setObjectName(u"label_products_in_all_stores")

        self.horizontalLayout.addWidget(self.label_products_in_all_stores)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_products_in_at_least_one_shop = QLabel(self.centralwidget)
        self.label_products_in_at_least_one_shop.setObjectName(u"label_products_in_at_least_one_shop")

        self.horizontalLayout_2.addWidget(self.label_products_in_at_least_one_shop)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_products_in_no_shop = QLabel(self.centralwidget)
        self.label_products_in_no_shop.setObjectName(u"label_products_in_no_shop")

        self.horizontalLayout_3.addWidget(self.label_products_in_no_shop)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout_5.addWidget(self.label_status)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0456\u0437 \u0442\u043e\u0432\u0430\u0440\u0456\u0432 \u0443 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430\u0445", None))
        self.label_store_name.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u0430\u0437\u0432\u0443 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0443:", None))
        self.pushButton_add_store.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043c\u0430\u0433\u0430\u0437\u0438\u043d", None))
        self.pushButton_process_products.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0430\u043d\u0430\u043b\u0456\u0437\u0443\u0432\u0430\u0442\u0438 \u0442\u043e\u0432\u0430\u0440\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0438:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u0438 \u0432 \u043a\u043e\u0436\u043d\u043e\u043c\u0443 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0456:", None))
        self.label_products_in_all_stores.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u0438 \u0445\u043e\u0447\u0430 \u0431 \u0432 \u043e\u0434\u043d\u043e\u043c\u0443 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0456:", None))
        self.label_products_in_at_least_one_shop.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u0438, \u044f\u043a\u0438\u0445 \u043d\u0435\u043c\u0430\u0454 \u043d\u0456 \u0432 \u043e\u0434\u043d\u043e\u043c\u0443 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0456:", None))
        self.label_products_in_no_shop.setText("")
        self.label_status.setText("")
    # retranslateUi

