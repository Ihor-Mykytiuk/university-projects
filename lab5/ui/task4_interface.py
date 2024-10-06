# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task4_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(398, 698)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 0))
        self.title.setMaximumSize(QSize(16777215, 140))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.title)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.m_input = QLineEdit(self.frame)
        self.m_input.setObjectName(u"m_input")

        self.horizontalLayout.addWidget(self.m_input)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.n_input = QLineEdit(self.frame)
        self.n_input.setObjectName(u"n_input")

        self.horizontalLayout.addWidget(self.n_input)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.generate_matrix_button = QPushButton(Form)
        self.generate_matrix_button.setObjectName(u"generate_matrix_button")

        self.verticalLayout_2.addWidget(self.generate_matrix_button)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.array_result = QLabel(Form)
        self.array_result.setObjectName(u"array_result")
        self.array_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.array_result)

        self.transform_matrix_button = QPushButton(Form)
        self.transform_matrix_button.setObjectName(u"transform_matrix_button")

        self.verticalLayout_3.addWidget(self.transform_matrix_button)

        self.status_label = QLabel(Form)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout_3.addWidget(self.status_label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u041c\u0456\u043d\u0456\u043c\u0430\u043b\u044c\u043d\u0438\u0439 \u0456 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0438\u0439 \u0435\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u043c\u0430\u0442\u0440\u0438\u0446\u0456", None))
        self.m_input.setPlaceholderText(QCoreApplication.translate("Form", u"m", None))
        self.label.setText(QCoreApplication.translate("Form", u"x", None))
        self.n_input.setPlaceholderText(QCoreApplication.translate("Form", u"n", None))
        self.generate_matrix_button.setText(QCoreApplication.translate("Form", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438 \u043c\u0430\u0442\u0440\u0438\u0446\u044e", None))
        self.array_result.setText("")
        self.transform_matrix_button.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u043c\u0430\u0442\u0440\u0438\u0446\u044e", None))
        self.status_label.setText("")
    # retranslateUi

