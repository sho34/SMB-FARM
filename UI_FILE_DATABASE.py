# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database_server_setup_page.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_DatabaseLogin(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"*{\n"
"	background:rgb(58, 58, 89) ;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"QLineEdit, QLabel{\n"
"	padding: 10px;\n"
"	color: #fff;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(74, 0))

        self.horizontalLayout.addWidget(self.label_3)

        self.host = QLineEdit(self.frame1)
        self.host.setObjectName(u"host")

        self.horizontalLayout.addWidget(self.host)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(74, 0))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.username = QLineEdit(self.frame1)
        self.username.setObjectName(u"username")

        self.horizontalLayout_2.addWidget(self.username)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.frame1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(74, 0))

        self.horizontalLayout_3.addWidget(self.label_5)

        self.password = QLineEdit(self.frame1)
        self.password.setObjectName(u"password")
        self.password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.password)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addWidget(self.frame1, 3, 0, 1, 4)

        self.frame2 = QFrame(self.frame)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setMinimumSize(QSize(331, 41))
        self.frame2.setStyleSheet(u"QPushButton{\n"
"background: #2c2c2c;\n"
"color: #fff;\n"
"font-family: sans;\n"
"font-size: 15px;\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #eee;\n"
"color: #2c2c2c;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.frame2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.frame2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.label_2 = QLabel(self.frame2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #ff6666;")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.gridLayout_3.addWidget(self.frame2, 5, 1, 1, 2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #fff;")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(19, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 42, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 43, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 6, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(19, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 5, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 43, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 43, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Login To Local Database Server</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#92c881;\">Welcome just a few steps to setup the database on your machine for the Software</span></p></body></html>", None))
    # retranslateUi

