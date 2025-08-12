# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 410)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(58, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.Title = QLabel(self.dropShadowFrame)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(10, 60, 771, 81))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(40)
        self.Title.setFont(font)
        self.Title.setStyleSheet(u"color: #FF7F50;")
        self.Title.setAlignment(Qt.AlignCenter)
        self.Description = QLabel(self.dropShadowFrame)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(10, 130, 761, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.Description.setFont(font1)
        self.Description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.Description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 260, 641, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: #32324e;\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:0.511364, stop:0 rgba(174, 166, 200, 255), stop:1 rgba(200, 199, 199, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.loading = QLabel(self.dropShadowFrame)
        self.loading.setObjectName(u"loading")
        self.loading.setGeometry(QRect(10, 300, 761, 51))
        self.loading.setFont(font1)
        self.loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.loading.setAlignment(Qt.AlignCenter)
        self.Version = QLabel(self.dropShadowFrame)
        self.Version.setObjectName(u"Version")
        self.Version.setGeometry(QRect(570, 350, 181, 31))
        self.Version.setFont(font1)
        self.Version.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.Version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Credit = QLabel(self.dropShadowFrame)
        self.Credit.setObjectName(u"Credit")
        self.Credit.setGeometry(QRect(20, 350, 351, 31))
        self.Credit.setFont(font1)
        self.Credit.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.Credit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Simbanai Brahmans</span> FARM</p></body></html>", None))
        self.Description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">MANAGE YOUR<span style=\" font-weight:600;\"> CATTLE</span> THE RIGHT WAY </p></body></html>", None))
        self.loading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Loading...</p></body></html>", None))
        self.Version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">VERSION:</span> 1.0.0</p></body></html>", None))
        self.Credit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Created By AGRO IQ</p></body></html>", None))
    # retranslateUi

