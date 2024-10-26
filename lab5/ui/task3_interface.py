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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 700)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 0))
        self.title.setMaximumSize(QSize(16777215, 140))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.title)

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

        self.pushButton_create_matrix = QPushButton(Form)
        self.pushButton_create_matrix.setObjectName(u"pushButton_create_matrix")

        self.verticalLayout_2.addWidget(self.pushButton_create_matrix)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.matrix_result = QLabel(Form)
        self.matrix_result.setObjectName(u"matrix_result")
        self.matrix_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.matrix_result)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.pushButton_calculate_sum = QPushButton(Form)
        self.pushButton_calculate_sum.setObjectName(u"pushButton_calculate_sum")

        self.verticalLayout_3.addWidget(self.pushButton_calculate_sum)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.label_status = QLabel(Form)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_status)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"\u0421\u0443\u043c\u0430 \u0441\u0442\u043e\u0432\u043f\u0446\u0456\u0432 \u043c\u0430\u0442\u0440\u0438\u0446\u0456", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u043c\u0430\u0442\u0440\u0438\u0446\u0456", None))
        self.m_input.setPlaceholderText(QCoreApplication.translate("Form", u"m", None))
        self.label.setText(QCoreApplication.translate("Form", u"x", None))
        self.n_input.setPlaceholderText(QCoreApplication.translate("Form", u"n", None))
        self.pushButton_create_matrix.setText(QCoreApplication.translate("Form", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438 \u043c\u0430\u0442\u0440\u0438\u0446\u044e", None))
        self.matrix_result.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043d\u0456 \u0441\u0442\u043e\u0432\u043f\u0446\u0456", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u041d\u0435\u043f\u0430\u0440\u043d\u0456 \u0441\u0442\u043e\u0432\u043f\u0446\u0456", None))

        self.pushButton_calculate_sum.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438 \u0441\u0443\u043c\u0443", None))
        self.label_status.setText("")
    # retranslateUi

