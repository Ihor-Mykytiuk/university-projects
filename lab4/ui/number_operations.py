# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'number_operations.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 670)
        font = QFont()
        font.setPointSize(22)
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 30, 401, 61))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI Semilight"])
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 200, 401, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.lineEditX = QLineEdit(self.verticalLayoutWidget)
        self.lineEditX.setObjectName(u"lineEditX")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.lineEditX.setFont(font2)
        self.lineEditX.setStyleSheet(u"border-radius: 10px;\n"
"padding: 10px")

        self.verticalLayout.addWidget(self.lineEditX)

        self.lineEditY = QLineEdit(self.verticalLayoutWidget)
        self.lineEditY.setObjectName(u"lineEditY")
        self.lineEditY.setFont(font2)
        self.lineEditY.setStyleSheet(u"border-radius: 10px;\n"
"padding: 10px")

        self.verticalLayout.addWidget(self.lineEditY)

        self.lineEditZ = QLineEdit(self.verticalLayoutWidget)
        self.lineEditZ.setObjectName(u"lineEditZ")
        self.lineEditZ.setFont(font2)
        self.lineEditZ.setStyleSheet(u"border-radius: 10px;\n"
"padding: 10px")

        self.verticalLayout.addWidget(self.lineEditZ)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 550, 340, 50))
        font3 = QFont()
        font3.setFamilies([u"Miriam CLM"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: rgb(96, 122, 251);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 90, 401, 20))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sequence Operations", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sequence Operation", None))
        self.lineEditX.setText("")
        self.lineEditX.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEditY.setText("")
        self.lineEditY.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.lineEditZ.setText("")
        self.lineEditZ.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter a sequence of three numbers", None))
    # retranslateUi

