# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(432, 491)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 411, 133))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setMinimumSize(QSize(0, 75))
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 148, 415, 334))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_1 = QPushButton(self.widget1)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.widget1)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_13, 0, 3, 1, 1)

        self.pushButton_14 = QPushButton(self.widget1)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_14, 0, 4, 1, 1)

        self.pushButton_4 = QPushButton(self.widget1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget1)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.widget1)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.widget1)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_15, 1, 3, 1, 1)

        self.pushButton_16 = QPushButton(self.widget1)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_16, 1, 4, 1, 1)

        self.pushButton_7 = QPushButton(self.widget1)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.widget1)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget1)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.widget1)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_17, 2, 3, 1, 1)

        self.pushButton_18 = QPushButton(self.widget1)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(75, 170))

        self.gridLayout.addWidget(self.pushButton_18, 2, 4, 2, 1)

        self.pushButton_0 = QPushButton(self.widget1)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(170, 75))

        self.gridLayout.addWidget(self.pushButton_0, 3, 0, 1, 2)

        self.pushButton_11 = QPushButton(self.widget1)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_11, 3, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.widget1)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(75, 75))

        self.gridLayout.addWidget(self.pushButton_12, 3, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"*", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"+/-", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"C", None))
    # retranslateUi

