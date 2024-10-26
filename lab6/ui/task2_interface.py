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
        self.size_input = QLineEdit(Form)
        self.size_input.setObjectName(u"size_input")
        self.size_input.setStyleSheet(u"")
        self.size_input.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.size_input)

        self.create_list_button = QPushButton(Form)
        self.create_list_button.setObjectName(u"create_list_button")

        self.verticalLayout_3.addWidget(self.create_list_button)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.list_result = QLabel(Form)
        self.list_result.setObjectName(u"list_result")
        self.list_result.setMaximumSize(QSize(16777215, 140))

        self.verticalLayout.addWidget(self.list_result)

        self.sort_button = QPushButton(Form)
        self.sort_button.setObjectName(u"sort_button")

        self.verticalLayout.addWidget(self.sort_button)

        self.status_label = QLabel(Form)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout.addWidget(self.status_label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u0412\u043f\u043e\u0440\u044f\u0434\u043a\u0443\u0432\u0430\u043d\u043d\u044f \u0435\u043b\u0435\u043c\u0435\u043d\u0442\u0456\u0432 \u0441\u043f\u0438\u0441\u043a\u0443", None))
        self.size_input.setText("")
        self.size_input.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u0441\u043f\u0438\u0441\u043a\u0443 N", None))
        self.create_list_button.setText(QCoreApplication.translate("Form", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.list_result.setText("")
        self.sort_button.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u0442\u0438", None))
        self.status_label.setText("")
    # retranslateUi

