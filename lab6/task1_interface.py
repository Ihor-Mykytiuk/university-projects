# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task1_interface.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 691)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.title)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.size_input = QLineEdit(Form)
        self.size_input.setObjectName(u"size_input")
        self.size_input.setStyleSheet(u"")
        self.size_input.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.size_input)

        self.create_array_button = QPushButton(Form)
        self.create_array_button.setObjectName(u"create_array_button")

        self.verticalLayout_3.addWidget(self.create_array_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.array_result = QLabel(Form)
        self.array_result.setObjectName(u"array_result")
        self.array_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.array_result)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.n_input = QLineEdit(Form)
        self.n_input.setObjectName(u"n_input")

        self.horizontalLayout.addWidget(self.n_input)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.k_input = QLineEdit(Form)
        self.k_input.setObjectName(u"k_input")

        self.horizontalLayout.addWidget(self.k_input)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.delete_button = QPushButton(Form)
        self.delete_button.setObjectName(u"delete_button")

        self.verticalLayout_2.addWidget(self.delete_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.status_label = QLabel(Form)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.status_label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0434\u0430\u043b\u0435\u043d\u043d\u044f \u0435\u043b\u0435\u043c\u0435\u043d\u0442\u0456\u0432 \u0441\u043f\u0438\u0441\u043a\u0443", None))
        self.size_input.setText("")
        self.size_input.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u043c\u0430\u0441\u0438\u0432\u0443 N", None))
        self.create_array_button.setText(QCoreApplication.translate("Form", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438 \u043c\u0430\u0441\u0438\u0432", None))
        self.array_result.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0456\u044e \u0434\u043b\u044f \u0432\u0438\u0434\u0430\u043b\u0435\u043d\u043d\u044f", None))
        self.n_input.setText("")
        self.n_input.setPlaceholderText(QCoreApplication.translate("Form", u"N", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u043f\u043e", None))
        self.k_input.setPlaceholderText(QCoreApplication.translate("Form", u"K", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0435\u043b\u0435\u043c\u0435\u043d\u0442\u0438", None))
        self.status_label.setText("")
    # retranslateUi

