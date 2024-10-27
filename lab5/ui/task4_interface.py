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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.input_m = QLineEdit(self.frame)
        self.input_m.setObjectName(u"input_m")

        self.horizontalLayout.addWidget(self.input_m)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.input_n = QLineEdit(self.frame)
        self.input_n.setObjectName(u"input_n")

        self.horizontalLayout.addWidget(self.input_n)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton_create_matrix = QPushButton(self.centralwidget)
        self.pushButton_create_matrix.setObjectName(u"pushButton_create_matrix")

        self.verticalLayout_2.addWidget(self.pushButton_create_matrix)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.label_result_matrix = QLabel(self.centralwidget)
        self.label_result_matrix.setObjectName(u"label_result_matrix")
        self.label_result_matrix.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_result_matrix)

        self.pushButton_transform_matrix = QPushButton(self.centralwidget)
        self.pushButton_transform_matrix.setObjectName(u"pushButton_transform_matrix")

        self.verticalLayout_3.addWidget(self.pushButton_transform_matrix)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

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
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0456\u043d\u0456\u043c\u0430\u043b\u044c\u043d\u0438\u0439 \u0456 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0438\u0439 \u0435\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u043e\u0437\u043c\u0456\u0440 \u043c\u0430\u0442\u0440\u0438\u0446\u0456", None))
        self.input_m.setPlaceholderText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.input_n.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n", None))
        self.pushButton_create_matrix.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0433\u0435\u043d\u0435\u0440\u0443\u0432\u0430\u0442\u0438 \u043c\u0430\u0442\u0440\u0438\u0446\u044e", None))
        self.label_result_matrix.setText("")
        self.pushButton_transform_matrix.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u043c\u0430\u0442\u0440\u0438\u0446\u044e", None))
        self.label_status.setText("")
    # retranslateUi

