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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.title)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(13)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_array = QLineEdit(self.centralwidget)
        self.input_array.setObjectName(u"input_array")
        self.input_array.setStyleSheet(u"")
        self.input_array.setReadOnly(False)
        self.input_array.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.input_array)

        self.label_or = QLabel(self.centralwidget)
        self.label_or.setObjectName(u"label_or")
        self.label_or.setMaximumSize(QSize(16777215, 20))
        self.label_or.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_or)

        self.input_size = QLineEdit(self.centralwidget)
        self.input_size.setObjectName(u"input_size")
        self.input_size.setStyleSheet(u"")
        self.input_size.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.input_size)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton_create_array = QPushButton(self.centralwidget)
        self.pushButton_create_array.setObjectName(u"pushButton_create_array")
        self.pushButton_create_array.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_create_array.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.pushButton_create_array)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.label_result_array = QLabel(self.centralwidget)
        self.label_result_array.setObjectName(u"label_result_array")
        self.label_result_array.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_result_array)

        self.pushButton_transform_array = QPushButton(self.centralwidget)
        self.pushButton_transform_array.setObjectName(u"pushButton_transform_array")
        self.pushButton_transform_array.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_transform_array.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton_transform_array)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_status)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 4)
        self.verticalLayout_3.setStretch(3, 2)
        self.verticalLayout_3.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f \u043c\u0430\u0441\u0438\u0432\u0443", None))
        self.input_array.setText("")
        self.input_array.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043c\u0430\u0441\u0438\u0432 \u0447\u0438\u0441\u0435\u043b \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0456\u043b", None))
        self.label_or.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0431\u043e", None))
        self.input_size.setText("")
        self.input_size.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u043c\u0430\u0441\u0438\u0432\u0443 N", None))
        self.pushButton_create_array.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u043c\u0430\u0441\u0438\u0432", None))
        self.label_result_array.setText("")
        self.pushButton_transform_array.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u043c\u0430\u0441\u0438\u0432", None))
        self.label_status.setText("")
    # retranslateUi

