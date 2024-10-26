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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 700)
        Form.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(14, -1, 14, -1)
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 140))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"font-size:24px")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.title)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(13)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.array_input = QLineEdit(Form)
        self.array_input.setObjectName(u"array_input")
        self.array_input.setStyleSheet(u"")
        self.array_input.setReadOnly(False)
        self.array_input.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.array_input)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.size_input = QLineEdit(Form)
        self.size_input.setObjectName(u"size_input")
        self.size_input.setStyleSheet(u"")
        self.size_input.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.size_input)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton_create_array = QPushButton(Form)
        self.pushButton_create_array.setObjectName(u"pushButton_create_array")
        self.pushButton_create_array.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_create_array.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.pushButton_create_array)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.array_result = QLabel(Form)
        self.array_result.setObjectName(u"array_result")
        self.array_result.setMaximumSize(QSize(16777215, 140))
        self.array_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.array_result)

        self.pushButton_transform_array = QPushButton(Form)
        self.pushButton_transform_array.setObjectName(u"pushButton_transform_array")
        self.pushButton_transform_array.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_transform_array.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_transform_array)

        self.label_status = QLabel(Form)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_status)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f \u043c\u0430\u0441\u0438\u0432\u0443", None))
        self.array_input.setText("")
        self.array_input.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043c\u0430\u0441\u0438\u0432 \u0447\u0438\u0441\u0435\u043b \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0456\u043b", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0430\u0431\u043e", None))
        self.size_input.setText("")
        self.size_input.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u043c\u0430\u0441\u0438\u0432\u0443 N", None))
        self.pushButton_create_array.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u043c\u0430\u0441\u0438\u0432", None))
        self.array_result.setText("")
        self.pushButton_transform_array.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u043c\u0430\u0441\u0438\u0432", None))
        self.label_status.setText("")
    # retranslateUi

