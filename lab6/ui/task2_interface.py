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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 140))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.input_size = QLineEdit(self.centralwidget)
        self.input_size.setObjectName(u"input_size")
        self.input_size.setStyleSheet(u"")
        self.input_size.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.input_size)

        self.pushButton_create_list = QPushButton(self.centralwidget)
        self.pushButton_create_list.setObjectName(u"pushButton_create_list")

        self.verticalLayout_3.addWidget(self.pushButton_create_list)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.label_result_list = QLabel(self.centralwidget)
        self.label_result_list.setObjectName(u"label_result_list")
        self.label_result_list.setMaximumSize(QSize(16777215, 16777215))
        self.label_result_list.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_result_list)

        self.pushButton_sort_list = QPushButton(self.centralwidget)
        self.pushButton_sort_list.setObjectName(u"pushButton_sort_list")

        self.verticalLayout.addWidget(self.pushButton_sort_list)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout.addWidget(self.label_status)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u043e\u0440\u044f\u0434\u043a\u0443\u0432\u0430\u043d\u043d\u044f \u0435\u043b\u0435\u043c\u0435\u043d\u0442\u0456\u0432 \u0441\u043f\u0438\u0441\u043a\u0443", None))
        self.input_size.setText("")
        self.input_size.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u0441\u043f\u0438\u0441\u043a\u0443 N", None))
        self.pushButton_create_list.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.label_result_list.setText("")
        self.pushButton_sort_list.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u0442\u0438", None))
        self.label_status.setText("")
    # retranslateUi

