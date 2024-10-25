# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student-login.ui'
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
        MainWindow.resize(400, 671)
        font = QFont()
        font.setPointSize(22)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
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
        self.verticalLayoutWidget.setGeometry(QRect(0, 210, 401, 171))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.lineEditLogin = QLineEdit(self.verticalLayoutWidget)
        self.lineEditLogin.setObjectName(u"lineEditLogin")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.lineEditLogin.setFont(font2)
        self.lineEditLogin.setStyleSheet(u"border-radius: 10px;\n"
"padding: 15px")

        self.verticalLayout.addWidget(self.lineEditLogin)

        self.lineEditPassword = QLineEdit(self.verticalLayoutWidget)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setFont(font2)
        self.lineEditPassword.setStyleSheet(u"border-radius: 10px;\n"
"padding: 15px")
        self.lineEditPassword.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEditPassword)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 550, 340, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Miriam CLM"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
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
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 380, 171, 16))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setUnderline(True)
        self.label_3.setFont(font5)
        self.label_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_3.setStyleSheet(u"color: rgb(231, 238, 242);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome back!", None))
        self.lineEditLogin.setText("")
        self.lineEditLogin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEditPassword.setText("")
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter your login and password to sign in", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Forgot your password?", None))
    # retranslateUi

