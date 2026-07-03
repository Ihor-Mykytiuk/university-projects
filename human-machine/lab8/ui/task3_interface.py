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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.label_patient_name = QLabel(self.centralwidget)
        self.label_patient_name.setObjectName(u"label_patient_name")

        self.verticalLayout.addWidget(self.label_patient_name)

        self.input_patient_name = QLineEdit(self.centralwidget)
        self.input_patient_name.setObjectName(u"input_patient_name")

        self.verticalLayout.addWidget(self.input_patient_name)

        self.comboBox_doctor_select = QComboBox(self.centralwidget)
        self.comboBox_doctor_select.setObjectName(u"comboBox_doctor_select")

        self.verticalLayout.addWidget(self.comboBox_doctor_select)

        self.pushButton_add_patient = QPushButton(self.centralwidget)
        self.pushButton_add_patient.setObjectName(u"pushButton_add_patient")

        self.verticalLayout.addWidget(self.pushButton_add_patient)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea_content = QWidget()
        self.scrollArea_content.setObjectName(u"scrollArea_content")
        self.scrollArea_content.setGeometry(QRect(0, 0, 830, 528))
        self.scrollArea.setWidget(self.scrollArea_content)

        self.verticalLayout.addWidget(self.scrollArea)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout.addWidget(self.label_status)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0443\u043b\u044f\u0446\u0456\u044f \u0447\u0435\u0440\u0433\u0438 \u0432 \u043f\u043e\u043b\u0456\u043a\u043b\u0456\u043d\u0456\u0446\u0456", None))
        self.label_patient_name.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0456\u043c'\u044f \u043f\u0430\u0446\u0456\u0454\u043d\u0442\u0430:", None))
        self.pushButton_add_patient.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u0438\u0441\u044f", None))
        self.label_status.setText("")
    # retranslateUi

