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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 603)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.title)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_search = QLabel(self.centralwidget)
        self.label_search.setObjectName(u"label_search")

        self.verticalLayout.addWidget(self.label_search)

        self.input_search = QLineEdit(self.centralwidget)
        self.input_search.setObjectName(u"input_search")

        self.verticalLayout.addWidget(self.input_search)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_search_by_name = QRadioButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_search_by_name)
        self.radioButton_search_by_name.setObjectName(u"radioButton_search_by_name")
        self.radioButton_search_by_name.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_search_by_name)

        self.radioButton_search_by_group = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.radioButton_search_by_group)
        self.radioButton_search_by_group.setObjectName(u"radioButton_search_by_group")

        self.horizontalLayout.addWidget(self.radioButton_search_by_group)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.list_students = QTextEdit(self.centralwidget)
        self.list_students.setObjectName(u"list_students")
        self.list_students.setEnabled(False)

        self.verticalLayout_3.addWidget(self.list_students)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_add_or_delete = QLabel(self.centralwidget)
        self.label_add_or_delete.setObjectName(u"label_add_or_delete")

        self.verticalLayout_2.addWidget(self.label_add_or_delete)

        self.input_name = QLineEdit(self.centralwidget)
        self.input_name.setObjectName(u"input_name")

        self.verticalLayout_2.addWidget(self.input_name)

        self.input_group = QLineEdit(self.centralwidget)
        self.input_group.setObjectName(u"input_group")

        self.verticalLayout_2.addWidget(self.input_group)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_add_student = QPushButton(self.centralwidget)
        self.pushButton_add_student.setObjectName(u"pushButton_add_student")

        self.horizontalLayout_2.addWidget(self.pushButton_add_student)

        self.pushButton_delete_student = QPushButton(self.centralwidget)
        self.pushButton_delete_student.setObjectName(u"pushButton_delete_student")

        self.horizontalLayout_2.addWidget(self.pushButton_delete_student)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout_3.addWidget(self.label_status)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 10)
        self.verticalLayout_3.setStretch(3, 4)
        self.verticalLayout_3.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Map Student", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0432\u0456\u0434\u043d\u0438\u043a \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0456\u0432", None))
        self.label_search.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0456\u043c'\u044f \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430 \u0430\u0431\u043e \u0433\u0440\u0443\u043f\u0443:", None))
        self.radioButton_search_by_name.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a \u043f\u043e \u0456\u043c\u0435\u043d\u0456", None))
        self.radioButton_search_by_group.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a \u043f\u043e \u0433\u0440\u0443\u043f\u0456", None))
        self.label_add_or_delete.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0430\u0431\u043e \u0432\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
        self.input_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435 \u0442\u0430 \u0456\u043c'\u044f", None))
        self.input_group.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.pushButton_add_student.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
        self.pushButton_delete_student.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
        self.label_status.setText("")
    # retranslateUi

