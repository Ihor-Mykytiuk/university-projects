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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.title)

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


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.label_result_list = QLabel(self.centralwidget)
        self.label_result_list.setObjectName(u"label_result_list")
        self.label_result_list.setMaximumSize(QSize(16777215, 16777215))
        self.label_result_list.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_result_list)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.select_operation = QLabel(self.centralwidget)
        self.select_operation.setObjectName(u"select_operation")

        self.verticalLayout.addWidget(self.select_operation)

        self.comboBox_select_operation = QComboBox(self.centralwidget)
        self.comboBox_select_operation.addItem("")
        self.comboBox_select_operation.addItem("")
        self.comboBox_select_operation.addItem("")
        self.comboBox_select_operation.setObjectName(u"comboBox_select_operation")

        self.verticalLayout.addWidget(self.comboBox_select_operation)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_inputs = QHBoxLayout()
        self.horizontalLayout_inputs.setObjectName(u"horizontalLayout_inputs")
        self.input_first = QLineEdit(self.centralwidget)
        self.input_first.setObjectName(u"input_first")

        self.horizontalLayout_inputs.addWidget(self.input_first)

        self.input_last = QLineEdit(self.centralwidget)
        self.input_last.setObjectName(u"input_last")

        self.horizontalLayout_inputs.addWidget(self.input_last)

        self.input_value = QLineEdit(self.centralwidget)
        self.input_value.setObjectName(u"input_value")

        self.horizontalLayout_inputs.addWidget(self.input_value)


        self.verticalLayout_2.addLayout(self.horizontalLayout_inputs)

        self.pushButton_execute_operation = QPushButton(self.centralwidget)
        self.pushButton_execute_operation.setObjectName(u"pushButton_execute_operation")

        self.verticalLayout_2.addWidget(self.pushButton_execute_operation)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout_4.addWidget(self.label_status)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 3)
        self.verticalLayout_4.setStretch(3, 2)
        self.verticalLayout_4.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0431\u043e\u0442\u0430 \u0437 \u0434\u0432\u043e\u0437\u0432'\u044f\u0437\u043d\u0438\u043c \u0441\u043f\u0438\u0441\u043a\u043e\u043c", None))
        self.input_size.setText("")
        self.input_size.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u0441\u043f\u0438\u0441\u043a\u0443 N", None))
        self.pushButton_create_list.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.label_result_list.setText("")
        self.select_operation.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0456\u0457 \u043d\u0430\u0434 \u0441\u043f\u0438\u0441\u043e\u043a\u043c:", None))
        self.comboBox_select_operation.setItemText(0, QCoreApplication.translate("MainWindow", u"count", None))
        self.comboBox_select_operation.setItemText(1, QCoreApplication.translate("MainWindow", u"reverse", None))
        self.comboBox_select_operation.setItemText(2, QCoreApplication.translate("MainWindow", u"iter_swap", None))

        self.input_first.setText("")
        self.input_first.setPlaceholderText(QCoreApplication.translate("MainWindow", u"first", None))
        self.input_last.setPlaceholderText(QCoreApplication.translate("MainWindow", u"last", None))
        self.input_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.pushButton_execute_operation.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043a\u043e\u043d\u0430\u0442\u0438 \u043e\u043f\u0435\u0440\u0430\u0446\u0456\u044e", None))
        self.label_status.setText("")
    # retranslateUi

