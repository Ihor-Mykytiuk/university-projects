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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, -1, -1)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.title)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_select_standard_files = QPushButton(self.centralwidget)
        self.pushButton_select_standard_files.setObjectName(u"pushButton_select_standard_files")

        self.verticalLayout_2.addWidget(self.pushButton_select_standard_files)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_select_input_file = QPushButton(self.centralwidget)
        self.pushButton_select_input_file.setObjectName(u"pushButton_select_input_file")

        self.horizontalLayout.addWidget(self.pushButton_select_input_file)

        self.pushButton_select_output_file = QPushButton(self.centralwidget)
        self.pushButton_select_output_file.setObjectName(u"pushButton_select_output_file")

        self.horizontalLayout.addWidget(self.pushButton_select_output_file)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_input_file = QLabel(self.centralwidget)
        self.label_input_file.setObjectName(u"label_input_file")

        self.horizontalLayout_3.addWidget(self.label_input_file)

        self.label_output_file = QLabel(self.centralwidget)
        self.label_output_file.setObjectName(u"label_output_file")

        self.horizontalLayout_3.addWidget(self.label_output_file)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.table_results = QTableWidget(self.centralwidget)
        self.table_results.setObjectName(u"table_results")

        self.verticalLayout_3.addWidget(self.table_results)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_run_processing = QPushButton(self.centralwidget)
        self.pushButton_run_processing.setObjectName(u"pushButton_run_processing")

        self.horizontalLayout_2.addWidget(self.pushButton_run_processing)

        self.pushButton_clear_results = QPushButton(self.centralwidget)
        self.pushButton_clear_results.setObjectName(u"pushButton_clear_results")

        self.horizontalLayout_2.addWidget(self.pushButton_clear_results)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout_3.addWidget(self.label_status)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u043e\u0431\u043a\u0430 \u0444\u0430\u0439\u043b\u0456\u0432", None))
        self.pushButton_select_standard_files.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0456 \u0444\u0430\u0439\u043b\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0431\u043e", None))
        self.pushButton_select_input_file.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0432\u0445\u0456\u0434\u043d\u0438\u0439 \u0444\u0430\u0439\u043b", None))
        self.pushButton_select_output_file.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0432\u0438\u0445\u0456\u0434\u043d\u0438\u0439 \u0444\u0430\u0439\u043b", None))
        self.label_input_file.setText("")
        self.label_output_file.setText("")
        self.pushButton_run_processing.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0438 \u043e\u0431\u0440\u043e\u0431\u043a\u0443", None))
        self.pushButton_clear_results.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u044c\u0442\u0430\u0442", None))
        self.label_status.setText("")
    # retranslateUi

