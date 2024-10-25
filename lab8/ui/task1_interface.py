# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task1_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.pushButton_create_stack = QPushButton(self.centralwidget)
        self.pushButton_create_stack.setObjectName(u"pushButton_create_stack")

        self.verticalLayout.addWidget(self.pushButton_create_stack)

        self.label_stack_result = QLabel(self.centralwidget)
        self.label_stack_result.setObjectName(u"label_stack_result")

        self.verticalLayout.addWidget(self.label_stack_result)

        self.pushButton_process_stack = QPushButton(self.centralwidget)
        self.pushButton_process_stack.setObjectName(u"pushButton_process_stack")

        self.verticalLayout.addWidget(self.pushButton_process_stack)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout.addWidget(self.label_status)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0431\u043e\u0442\u0430 \u0437\u0456 \u0441\u0442\u0435\u043a\u043e\u043c", None))
        self.pushButton_create_stack.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u0441\u0442\u0435\u043a \u0437 10 \u0447\u0438\u0441\u0435\u043b", None))
        self.label_stack_result.setText("")
        self.pushButton_process_stack.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0443\u0432\u0430\u0442\u0438 \u0441\u0442\u0435\u043a", None))
        self.label_status.setText("")
    # retranslateUi

