# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator_interface2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(429, 507)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setMinimumSize(QSize(0, 75))
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton_additional = QPushButton(self.centralwidget)
        self.pushButton_additional.setObjectName(u"pushButton_additional")
        self.pushButton_additional.setMaximumSize(QSize(85, 16777215))

        self.verticalLayout.addWidget(self.pushButton_additional)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(75, 75))
        self.pushButton_1.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(75, 75))
        self.pushButton_2.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(75, 75))
        self.pushButton_3.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_plus = QPushButton(self.centralwidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setMinimumSize(QSize(75, 75))
        self.pushButton_plus.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_plus, 0, 3, 1, 1)

        self.pushButton_minus = QPushButton(self.centralwidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setMinimumSize(QSize(75, 75))
        self.pushButton_minus.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_minus, 0, 4, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(75, 75))
        self.pushButton_4.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(75, 75))
        self.pushButton_5.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(75, 75))
        self.pushButton_6.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_multiply = QPushButton(self.centralwidget)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        self.pushButton_multiply.setMinimumSize(QSize(75, 75))
        self.pushButton_multiply.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_multiply, 1, 3, 1, 1)

        self.pushButton_divide = QPushButton(self.centralwidget)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        self.pushButton_divide.setMinimumSize(QSize(75, 75))
        self.pushButton_divide.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_divide, 1, 4, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(75, 75))
        self.pushButton_7.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(75, 75))
        self.pushButton_8.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(75, 75))
        self.pushButton_9.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_change_sign = QPushButton(self.centralwidget)
        self.pushButton_change_sign.setObjectName(u"pushButton_change_sign")
        self.pushButton_change_sign.setMinimumSize(QSize(75, 75))
        self.pushButton_change_sign.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_change_sign, 2, 3, 1, 1)

        self.pushButton_equal = QPushButton(self.centralwidget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        self.pushButton_equal.setMinimumSize(QSize(0, 156))

        self.gridLayout_3.addWidget(self.pushButton_equal, 2, 4, 2, 1)

        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(0, 75))
        self.pushButton_0.setMaximumSize(QSize(16777215, 75))

        self.gridLayout_3.addWidget(self.pushButton_0, 3, 0, 1, 2)

        self.pushButton_decimal = QPushButton(self.centralwidget)
        self.pushButton_decimal.setObjectName(u"pushButton_decimal")
        self.pushButton_decimal.setMinimumSize(QSize(75, 75))
        self.pushButton_decimal.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_decimal, 3, 2, 1, 1)

        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(75, 75))
        self.pushButton_clear.setMaximumSize(QSize(75, 75))

        self.gridLayout_3.addWidget(self.pushButton_clear, 3, 3, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_additional.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0437\u0448\u0438\u0440\u0435\u043d\u0438\u0439", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_change_sign.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.pushButton_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_decimal.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
    # retranslateUi

