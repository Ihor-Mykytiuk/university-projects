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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnSelectStandardFiles = QPushButton(self.centralwidget)
        self.btnSelectStandardFiles.setObjectName(u"btnSelectStandardFiles")

        self.verticalLayout_2.addWidget(self.btnSelectStandardFiles)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSelectInputFile = QPushButton(self.centralwidget)
        self.btnSelectInputFile.setObjectName(u"btnSelectInputFile")

        self.horizontalLayout.addWidget(self.btnSelectInputFile)

        self.btnSelectOutputFile = QPushButton(self.centralwidget)
        self.btnSelectOutputFile.setObjectName(u"btnSelectOutputFile")

        self.horizontalLayout.addWidget(self.btnSelectOutputFile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelInputFile = QLabel(self.centralwidget)
        self.labelInputFile.setObjectName(u"labelInputFile")

        self.horizontalLayout_3.addWidget(self.labelInputFile)

        self.labelOutputFile = QLabel(self.centralwidget)
        self.labelOutputFile.setObjectName(u"labelOutputFile")

        self.horizontalLayout_3.addWidget(self.labelOutputFile)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tableResults = QTableWidget(self.centralwidget)
        self.tableResults.setObjectName(u"tableResults")

        self.verticalLayout_3.addWidget(self.tableResults)

        self.labelMessages = QLabel(self.centralwidget)
        self.labelMessages.setObjectName(u"labelMessages")

        self.verticalLayout_3.addWidget(self.labelMessages)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnRunProcessing = QPushButton(self.centralwidget)
        self.btnRunProcessing.setObjectName(u"btnRunProcessing")

        self.horizontalLayout_2.addWidget(self.btnRunProcessing)

        self.btnClearResults = QPushButton(self.centralwidget)
        self.btnClearResults.setObjectName(u"btnClearResults")

        self.horizontalLayout_2.addWidget(self.btnClearResults)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u043e\u0431\u043a\u0430 \u0444\u0430\u0439\u043b\u0456\u0432", None))
        self.btnSelectStandardFiles.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0456 \u0444\u0430\u0439\u043b\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0431\u043e", None))
        self.btnSelectInputFile.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0432\u0445\u0456\u0434\u043d\u0438\u0439 \u0444\u0430\u0439\u043b", None))
        self.btnSelectOutputFile.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0432\u0438\u0445\u0456\u0434\u043d\u0438\u0439 \u0444\u0430\u0439\u043b", None))
        self.labelInputFile.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelOutputFile.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelMessages.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0432\u0456\u0434\u043e\u043c\u043b\u0435\u043d\u043d\u044f", None))
        self.btnRunProcessing.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0438 \u043e\u0431\u0440\u043e\u0431\u043a\u0443", None))
        self.btnClearResults.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u044c\u0442\u0430\u0442", None))
    # retranslateUi

