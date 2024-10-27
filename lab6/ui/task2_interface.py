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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 700)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 140))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.input_size = QLineEdit(Form)
        self.input_size.setObjectName(u"input_size")
        self.input_size.setStyleSheet(u"")
        self.input_size.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.input_size)

        self.pushButton_create_list = QPushButton(Form)
        self.pushButton_create_list.setObjectName(u"pushButton_create_list")

        self.verticalLayout_3.addWidget(self.pushButton_create_list)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.label_result_list = QLabel(Form)
        self.label_result_list.setObjectName(u"label_result_list")
        self.label_result_list.setMaximumSize(QSize(16777215, 140))
        self.label_result_list.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_result_list)

        self.pushButton_sort_list = QPushButton(Form)
        self.pushButton_sort_list.setObjectName(u"pushButton_sort_list")

        self.verticalLayout.addWidget(self.pushButton_sort_list)

        self.label_status = QLabel(Form)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout.addWidget(self.label_status)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u0412\u043f\u043e\u0440\u044f\u0434\u043a\u0443\u0432\u0430\u043d\u043d\u044f \u0435\u043b\u0435\u043c\u0435\u043d\u0442\u0456\u0432 \u0441\u043f\u0438\u0441\u043a\u0443", None))
        self.input_size.setText("")
        self.input_size.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u0441\u043f\u0438\u0441\u043a\u0443 N", None))
        self.pushButton_create_list.setText(QCoreApplication.translate("Form", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.label_result_list.setText("")
        self.pushButton_sort_list.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u0442\u0438", None))
        self.label_status.setText("")
    # retranslateUi

