# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1341, 705)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1332, 705))
        MainWindow.setStyleSheet(u"background:rgb(58, 58, 89) ;")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color:#ff6666;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"\n"
"/*\n"
"	FOR THE SCROLLBARS\n"
"*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: no"
                        "ne;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"   \n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:#ccc;\n"
"    min-height: 25px;\n"
"	border-radius: 0px;\n"
"	border: none;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    /*background: rgb(55, 63, 77);*/\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical"
                        " {\n"
"	border: none;\n"
"   /* background: rgb(55, 63, 77);*/\n"
"     height: 20px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.title_bar = QFrame(self.styleSheet)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.title_bar.setStyleSheet(u"QFrame{\n"
"background:#32324e ;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background:#32324e ;\n"
"}\n"
"\n"
"")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_6 = QFrame(self.title_bar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(51, -6, 407, 31))
        self.label.setStyleSheet(u"color: #aeb7d0;\n"
"font-size: 20px;")

        self.horizontalLayout_2.addWidget(self.frame_6)

        self.settingsTopBtn_3 = QPushButton(self.title_bar)
        self.settingsTopBtn_3.setObjectName(u"settingsTopBtn_3")
        self.settingsTopBtn_3.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn_3.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingsTopBtn_3.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:#aeb7d0;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn_3.setIcon(icon)
        self.settingsTopBtn_3.setIconSize(QSize(20, 20))
        self.settingsTopBtn_3.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.settingsTopBtn_3)

        self.minimizeAppBtn_3 = QPushButton(self.title_bar)
        self.minimizeAppBtn_3.setObjectName(u"minimizeAppBtn_3")
        self.minimizeAppBtn_3.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn_3.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.minimizeAppBtn_3.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:#aeb7d0;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn_3.setIcon(icon1)
        self.minimizeAppBtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn_3)

        self.maximizeRestoreAppBtn_3 = QPushButton(self.title_bar)
        self.maximizeRestoreAppBtn_3.setObjectName(u"maximizeRestoreAppBtn_3")
        self.maximizeRestoreAppBtn_3.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn_3.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn_3.setFont(font1)
        self.maximizeRestoreAppBtn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.maximizeRestoreAppBtn_3.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:#aeb7d0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn_3.setIcon(icon2)
        self.maximizeRestoreAppBtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn_3)

        self.closeAppBtn_3 = QPushButton(self.title_bar)
        self.closeAppBtn_3.setObjectName(u"closeAppBtn_3")
        self.closeAppBtn_3.setMinimumSize(QSize(28, 28))
        self.closeAppBtn_3.setMaximumSize(QSize(28, 28))
        self.closeAppBtn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn_3.setStyleSheet(u"QPushButton:hover{\n"
"	background: #ff3333;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn_3.setIcon(icon3)
        self.closeAppBtn_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn_3)


        self.verticalLayout_20.addWidget(self.title_bar)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.styleSheet)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mainFrame = QStackedWidget(self.frame)
        self.mainFrame.setObjectName(u"mainFrame")
        self.getCredentials = QWidget()
        self.getCredentials.setObjectName(u"getCredentials")
        self.horizontalLayout = QHBoxLayout(self.getCredentials)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.uathenticationStack = QStackedWidget(self.getCredentials)
        self.uathenticationStack.setObjectName(u"uathenticationStack")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.uathenticationStack.sizePolicy().hasHeightForWidth())
        self.uathenticationStack.setSizePolicy(sizePolicy1)
        self.uathenticationStack.setStyleSheet(u"*{\n"
"	background:rgb(58, 58, 89) ;\n"
"	width: 800px;\n"
"}\n"
"\n"
"")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_5 = QGridLayout(self.page_10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.logInFrame = QFrame(self.page_10)
        self.logInFrame.setObjectName(u"logInFrame")
        sizePolicy.setHeightForWidth(self.logInFrame.sizePolicy().hasHeightForWidth())
        self.logInFrame.setSizePolicy(sizePolicy)
        self.logInFrame.setMaximumSize(QSize(601, 16777215))
        self.logInFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(58, 58, 89);\n"
"	color: #aeb7d0;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius: 10px;\n"
"background-color: rgb(98, 114, 164);\n"
"padding: 5px;\n"
"color: #fff;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #bbb;\n"
"}")
        self.logInFrame.setFrameShape(QFrame.StyledPanel)
        self.logInFrame.setFrameShadow(QFrame.Raised)
        self.loginFormContainer_3 = QFrame(self.logInFrame)
        self.loginFormContainer_3.setObjectName(u"loginFormContainer_3")
        self.loginFormContainer_3.setGeometry(QRect(70, 190, 451, 311))
        self.loginFormContainer_3.setFrameShape(QFrame.StyledPanel)
        self.loginFormContainer_3.setFrameShadow(QFrame.Raised)
        self.passwordInputLogIn = QLineEdit(self.loginFormContainer_3)
        self.passwordInputLogIn.setObjectName(u"passwordInputLogIn")
        self.passwordInputLogIn.setGeometry(QRect(80, 150, 281, 41))
        self.passwordInputLogIn.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"background-color: rgb(98, 114, 164);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #bbb;\n"
"}")
        self.passwordInputLogIn.setEchoMode(QLineEdit.Password)
        self.farmIdInput = QLineEdit(self.loginFormContainer_3)
        self.farmIdInput.setObjectName(u"farmIdInput")
        self.farmIdInput.setGeometry(QRect(80, 60, 281, 41))
        self.farmIdInput.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"background-color: rgb(98, 114, 164);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #bbb;\n"
"}")
        self.farmIdInput.setEchoMode(QLineEdit.Normal)
        self.registerButton = QPushButton(self.loginFormContainer_3)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(110, 220, 101, 41))
        self.registerButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.registerButton.setStyleSheet(u"QPushButton{\n"
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
        self.logInButton = QPushButton(self.loginFormContainer_3)
        self.logInButton.setObjectName(u"logInButton")
        self.logInButton.setGeometry(QRect(220, 220, 101, 41))
        self.logInButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logInButton.setStyleSheet(u"QPushButton{\n"
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
        self.passwordLabel_3 = QLabel(self.loginFormContainer_3)
        self.passwordLabel_3.setObjectName(u"passwordLabel_3")
        self.passwordLabel_3.setGeometry(QRect(90, 120, 101, 21))
        self.passwordLabel_3.setStyleSheet(u"font-family: sans;\n"
"font-size: 18px;")
        self.farmIdLabel_2 = QLabel(self.loginFormContainer_3)
        self.farmIdLabel_2.setObjectName(u"farmIdLabel_2")
        self.farmIdLabel_2.setGeometry(QRect(90, 30, 91, 16))
        self.farmIdLabel_2.setStyleSheet(u"font-family: sans;\n"
"font-size: 18px;")
        self.logInError = QLabel(self.loginFormContainer_3)
        self.logInError.setObjectName(u"logInError")
        self.logInError.setGeometry(QRect(90, 280, 261, 31))
        self.logInError.setStyleSheet(u"color: #ff6666;\n"
"")
        self.TitleLogin = QLabel(self.logInFrame)
        self.TitleLogin.setObjectName(u"TitleLogin")
        self.TitleLogin.setGeometry(QRect(120, 80, 321, 91))
        self.TitleLogin.setStyleSheet(u"font-size: 50px;\n"
"")

        self.gridLayout_5.addWidget(self.logInFrame, 0, 0, 1, 1)

        self.uathenticationStack.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.registerFrame = QFrame(self.page_11)
        self.registerFrame.setObjectName(u"registerFrame")
        self.registerFrame.setGeometry(QRect(130, 9, 1021, 531))
        sizePolicy.setHeightForWidth(self.registerFrame.sizePolicy().hasHeightForWidth())
        self.registerFrame.setSizePolicy(sizePolicy)
        self.registerFrame.setMaximumSize(QSize(1021, 16777215))
        self.registerFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(58, 58, 89);\n"
"	color: rgba(174, 183, 208, 1);\n"
"	border-radius: 10px;\n"
"	opacity: ;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius: 10px;\n"
"background-color: rgb(98, 114, 164);\n"
"padding: 5px;\n"
"color: #fff;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #bbb;\n"
"}")
        self.registerFrame.setFrameShape(QFrame.StyledPanel)
        self.registerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.registerFrame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_5 = QFrame(self.registerFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.RegistrationTitle = QLabel(self.frame_5)
        self.RegistrationTitle.setObjectName(u"RegistrationTitle")
        self.RegistrationTitle.setStyleSheet(u"font-size: 50px;\n"
"")

        self.horizontalLayout_3.addWidget(self.RegistrationTitle)


        self.verticalLayout_19.addWidget(self.frame_5)

        self.loginFormContainer_4 = QFrame(self.registerFrame)
        self.loginFormContainer_4.setObjectName(u"loginFormContainer_4")
        self.loginFormContainer_4.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"background-color: rgb(98, 114, 164);\n"
"padding: 5px;\n"
"color: #fff;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #bbb;\n"
"}")
        self.loginFormContainer_4.setFrameShape(QFrame.StyledPanel)
        self.loginFormContainer_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.loginFormContainer_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.loginFormContainer_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"justify-content: center")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.farmIdRegisterInput = QLineEdit(self.frame_2)
        self.farmIdRegisterInput.setObjectName(u"farmIdRegisterInput")
        self.farmIdRegisterInput.setGeometry(QRect(130, 220, 281, 41))
        self.farmIdRegisterInput.setStyleSheet(u"")
        self.farmIdRegisterInput.setEchoMode(QLineEdit.Normal)
        self.firstNameInput = QLineEdit(self.frame_2)
        self.firstNameInput.setObjectName(u"firstNameInput")
        self.firstNameInput.setGeometry(QRect(130, 40, 281, 41))
        self.firstNameInput.setFocusPolicy(Qt.NoFocus)
        self.firstNameInput.setStyleSheet(u"QLineEdit:focus{\n"
"	border: 2px solid #bbb;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgba(255, 255, 255, 0.4);\n"
"}")
        self.firstNameInput.setEchoMode(QLineEdit.Normal)
        self.firstNameInput.setReadOnly(True)
        self.firstNameInput.setClearButtonEnabled(False)
        self.lastNameLabel_2 = QLabel(self.frame_2)
        self.lastNameLabel_2.setObjectName(u"lastNameLabel_2")
        self.lastNameLabel_2.setGeometry(QRect(140, 100, 161, 21))
        self.lastNameLabel_2.setStyleSheet(u"font-family: sans;\n"
"font-size: 18px;\n"
"color: rgba(174, 183, 208, 0.4);")
        self.farmIdRegisterLabel_2 = QLabel(self.frame_2)
        self.farmIdRegisterLabel_2.setObjectName(u"farmIdRegisterLabel_2")
        self.farmIdRegisterLabel_2.setGeometry(QRect(140, 190, 111, 21))
        self.farmIdRegisterLabel_2.setStyleSheet(u"font-family: sans;\n"
"font-size: 18px;")
        self.lastNameInput = QLineEdit(self.frame_2)
        self.lastNameInput.setObjectName(u"lastNameInput")
        self.lastNameInput.setGeometry(QRect(130, 130, 281, 41))
        self.lastNameInput.setFocusPolicy(Qt.NoFocus)
        self.lastNameInput.setStyleSheet(u"QLineEdit:focus{\n"
"	border: 2px solid #bbb;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgba(255, 255, 255, 0.4);\n"
"}")
        self.lastNameInput.setEchoMode(QLineEdit.Normal)
        self.lastNameInput.setReadOnly(True)
        self.firstNameLabel_2 = QLabel(self.frame_2)
        self.firstNameLabel_2.setObjectName(u"firstNameLabel_2")
        self.firstNameLabel_2.setGeometry(QRect(140, 10, 161, 21))
        self.firstNameLabel_2.setStyleSheet(u"font-family: sans;\n"
"font-size: 18px;\n"
"color: rgba(174, 183, 208, 0.4);")

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.verticalSpacer_3 = QSpacerItem(5, 288, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.horizontalLayout_4.addItem(self.verticalSpacer_3)

        self.frame_3 = QFrame(self.loginFormContainer_4)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.passwordLabel_4 = QLabel(self.frame_3)
        self.passwordLabel_4.setObjectName(u"passwordLabel_4")
        self.passwordLabel_4.setGeometry(QRect(90, 10, 101, 21))
        self.passwordLabel_4.setStyleSheet(u"font-family: sans;\n"
"font-size: 18px;")
        self.passwordLabelConfirm_2 = QLabel(self.frame_3)
        self.passwordLabelConfirm_2.setObjectName(u"passwordLabelConfirm_2")
        self.passwordLabelConfirm_2.setGeometry(QRect(90, 100, 181, 16))
        self.passwordLabelConfirm_2.setStyleSheet(u"font-family: sans;\n"
"font-size: 18px;")
        self.passwordInputReg = QLineEdit(self.frame_3)
        self.passwordInputReg.setObjectName(u"passwordInputReg")
        self.passwordInputReg.setGeometry(QRect(80, 40, 281, 41))
        self.passwordInputReg.setStyleSheet(u"")
        self.passwordInputReg.setEchoMode(QLineEdit.Password)
        self.passwordInputConfirm = QLineEdit(self.frame_3)
        self.passwordInputConfirm.setObjectName(u"passwordInputConfirm")
        self.passwordInputConfirm.setGeometry(QRect(80, 130, 281, 41))
        self.passwordInputConfirm.setStyleSheet(u"")
        self.passwordInputConfirm.setEchoMode(QLineEdit.Password)
        self.showPasswordChkBox = QCheckBox(self.frame_3)
        self.showPasswordChkBox.setObjectName(u"showPasswordChkBox")
        self.showPasswordChkBox.setEnabled(True)
        self.showPasswordChkBox.setGeometry(QRect(250, 210, 111, 21))
        self.showPasswordChkBox.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"\n"
"QCheckBox{\n"
"	color: #fff;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}")
        self.showPasswordChkBox.setTristate(False)

        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_19.addWidget(self.loginFormContainer_4)

        self.frame_4 = QFrame(self.registerFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.registrationErr = QLabel(self.frame_7)
        self.registrationErr.setObjectName(u"registrationErr")
        self.registrationErr.setGeometry(QRect(530, 20, 441, 21))
        self.registrationErr.setStyleSheet(u"color: #ff6666;")
        self.backToLogInBtn = QPushButton(self.frame_7)
        self.backToLogInBtn.setObjectName(u"backToLogInBtn")
        self.backToLogInBtn.setGeometry(QRect(130, 10, 171, 41))
        self.backToLogInBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backToLogInBtn.setStyleSheet(u"QPushButton{\n"
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
        self.registerAccountButton = QPushButton(self.frame_7)
        self.registerAccountButton.setObjectName(u"registerAccountButton")
        self.registerAccountButton.setGeometry(QRect(360, 10, 161, 41))
        self.registerAccountButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.registerAccountButton.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.frame_7)

        self.informationBox_2 = QLabel(self.frame_4)
        self.informationBox_2.setObjectName(u"informationBox_2")
        self.informationBox_2.setMaximumSize(QSize(16777215, 15))
        self.informationBox_2.setStyleSheet(u"color: rgb(98, 114, 164);\n"
"")

        self.verticalLayout_4.addWidget(self.informationBox_2)


        self.verticalLayout_19.addWidget(self.frame_4)

        self.uathenticationStack.addWidget(self.page_11)

        self.horizontalLayout.addWidget(self.uathenticationStack)

        self.mainFrame.addWidget(self.getCredentials)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.gridLayout_4 = QGridLayout(self.mainPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mainContent = QWidget(self.mainPage)
        self.mainContent.setObjectName(u"mainContent")
        self.mainContent.setStyleSheet(u"QTabWidget::pane {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	margin: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: #404040;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-co"
                        "lor: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.mainContent)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidgetMainContent = QStackedWidget(self.mainContent)
        self.stackedWidgetMainContent.setObjectName(u"stackedWidgetMainContent")
        self.stackedWidgetMainContent.setStyleSheet(u"background: #7474a4;")
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.gridLayout_10 = QGridLayout(self.HomePage)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_20 = QFrame(self.HomePage)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 150))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_20)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_24 = QLabel(self.frame_20)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_28.addWidget(self.label_24, 0, 0, 1, 1)

        self.line_2 = QFrame(self.frame_20)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"color: #fff;")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_28.addWidget(self.line_2, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_20, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.HomePage)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_21)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy3)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_22)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.widget_6 = QWidget(self.frame_22)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(421, 0))
        self.widget_6.setStyleSheet(u"#widget_6, *{\n"
"	background: #fff;\n"
"}\n"
"\n"
"/* style for  QWidget with check list group */\n"
"#list_widget {\n"
"	border:1px solid #dfdfdf;\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"/* Style for QFrame in QWidget: set the sapce line */\n"
"#list_widget QFrame  {\n"
"	border-top:1px solid #dfdfdf;\n"
"}\n"
"\n"
"/* Sytle for QCheckBox after checked  */\n"
"#list_widget QCheckBox:checked  {\n"
"	color: #797979;\n"
"}\n"
"\n"
"/* Style for disabled QFrame */\n"
"#frame_disabled {\n"
"	border:1px solid #dfdfdf;\n"
"	background: #f8f9fa;\n"
"	border-bottom-right-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"/* style for resetting the border style of QLabel  and the first QFrame */\n"
"#first_frame, #list_widget QLabel {	\n"
"	border: none;\n"
"}\n"
"")
        self.verticalLayout_39 = QVBoxLayout(self.widget_6)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.dateDisplay = QLabel(self.widget_6)
        self.dateDisplay.setObjectName(u"dateDisplay")
        self.dateDisplay.setStyleSheet(u"background: #006666;\n"
"border-radius-top-right: 10px;\n"
"border-radius-top-left: 10px;\n"
"padding: 5px;\n"
"color: #f2f2f2;")

        self.gridLayout_30.addWidget(self.dateDisplay, 1, 0, 1, 1)

        self.dateTitle = QLabel(self.widget_6)
        self.dateTitle.setObjectName(u"dateTitle")
        self.dateTitle.setStyleSheet(u"background: #003366;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"padding: 5px;")
        self.dateTitle.setPixmap(QPixmap(u":/icons_svg/images/icons-svg/icons8_calendar_1.svg"))

        self.gridLayout_30.addWidget(self.dateTitle, 0, 0, 1, 1)


        self.verticalLayout_39.addLayout(self.gridLayout_30)

        self.notificationsScrollArea = QScrollArea(self.widget_6)
        self.notificationsScrollArea.setObjectName(u"notificationsScrollArea")
        self.notificationsScrollArea.setStyleSheet(u"")
        self.notificationsScrollArea.setWidgetResizable(True)
        self.notificationsScrollAreaWidgetContents = QWidget()
        self.notificationsScrollAreaWidgetContents.setObjectName(u"notificationsScrollAreaWidgetContents")
        self.notificationsScrollAreaWidgetContents.setGeometry(QRect(0, 0, 715, 300))
        self.gridLayout_61 = QGridLayout(self.notificationsScrollAreaWidgetContents)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.widget_3 = QWidget(self.notificationsScrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_21 = QVBoxLayout(self.widget_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.first_frame = QFrame(self.widget_3)
        self.first_frame.setObjectName(u"first_frame")
        self.first_frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.first_frame.setFrameShape(QFrame.StyledPanel)
        self.first_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.first_frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.checkBox_12 = QCheckBox(self.first_frame)
        self.checkBox_12.setObjectName(u"checkBox_12")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.checkBox_12.setFont(font2)
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setTristate(False)

        self.verticalLayout_15.addWidget(self.checkBox_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(15, -1, -1, -1)
        self.label_51 = QLabel(self.first_frame)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(15, 15))
        self.label_51.setMaximumSize(QSize(15, 15))
        self.label_51.setPixmap(QPixmap(u":/icon/calendar.png"))
        self.label_51.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_51)

        self.task_1 = QLabel(self.first_frame)
        self.task_1.setObjectName(u"task_1")
        self.task_1.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.task_1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)


        self.verticalLayout_21.addWidget(self.first_frame)

        self.frame_28 = QFrame(self.widget_3)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_28)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.checkBox_13 = QCheckBox(self.frame_28)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setFont(font2)
        self.checkBox_13.setChecked(True)

        self.verticalLayout_40.addWidget(self.checkBox_13)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(15, -1, -1, -1)
        self.label_53 = QLabel(self.frame_28)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setEnabled(False)
        self.label_53.setMinimumSize(QSize(15, 15))
        self.label_53.setMaximumSize(QSize(15, 15))
        self.label_53.setPixmap(QPixmap(u":/icon/calendar.png"))
        self.label_53.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_53)

        self.task_2 = QLabel(self.frame_28)
        self.task_2.setObjectName(u"task_2")
        self.task_2.setEnabled(False)

        self.horizontalLayout_24.addWidget(self.task_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_12)


        self.verticalLayout_40.addLayout(self.horizontalLayout_24)


        self.verticalLayout_21.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.widget_3)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_29)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, -1, -1, 9)
        self.checkBox_14 = QCheckBox(self.frame_29)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setFont(font2)

        self.verticalLayout_41.addWidget(self.checkBox_14)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(15, -1, -1, -1)
        self.label_55 = QLabel(self.frame_29)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(15, 15))
        self.label_55.setMaximumSize(QSize(15, 15))
        self.label_55.setPixmap(QPixmap(u":/icon/alarm-clock.png"))
        self.label_55.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.label_55)

        self.task_3 = QLabel(self.frame_29)
        self.task_3.setObjectName(u"task_3")

        self.horizontalLayout_25.addWidget(self.task_3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_13)


        self.verticalLayout_41.addLayout(self.horizontalLayout_25)


        self.verticalLayout_21.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.widget_3)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_30)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.checkBox_15 = QCheckBox(self.frame_30)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setEnabled(False)
        font3 = QFont()
        font3.setPointSize(10)
        self.checkBox_15.setFont(font3)

        self.verticalLayout_42.addWidget(self.checkBox_15)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(6)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(15, -1, -1, -1)
        self.label_57 = QLabel(self.frame_30)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setEnabled(False)
        self.label_57.setMinimumSize(QSize(15, 15))
        self.label_57.setMaximumSize(QSize(15, 15))
        self.label_57.setPixmap(QPixmap(u":/icon/edit-list.png"))
        self.label_57.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_57)

        self.task_4 = QLabel(self.frame_30)
        self.task_4.setObjectName(u"task_4")
        self.task_4.setEnabled(False)

        self.horizontalLayout_26.addWidget(self.task_4)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_14)


        self.verticalLayout_42.addLayout(self.horizontalLayout_26)


        self.verticalLayout_21.addWidget(self.frame_30)


        self.gridLayout_61.addWidget(self.widget_3, 0, 0, 1, 1)

        self.notificationsScrollArea.setWidget(self.notificationsScrollAreaWidgetContents)

        self.verticalLayout_39.addWidget(self.notificationsScrollArea)

        self.list_widget = QWidget(self.widget_6)
        self.list_widget.setObjectName(u"list_widget")
        self.list_widget.setStyleSheet(u"#widget_6 QLabel {\n"
"}\n"
"\n"
"#frame_8  {\n"
"	border:1px solid #dfdfdf;\n"
"}\n"
"\n"
"#frame_10 {\n"
"	border:1px solid #dfdfdf;\n"
"	background: #f8f9fa;\n"
"	border-bottom-right-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"#widget_6 {\n"
"	border:1px solid #dfdfdf;\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"#widget_6 QCheckBox:checked  {\n"
"		color: #797979;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.list_widget)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_39.addWidget(self.list_widget)


        self.gridLayout_31.addWidget(self.widget_6, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.frame_22, 1, 0, 1, 1)

        self.wellComeTitle = QLabel(self.frame_21)
        self.wellComeTitle.setObjectName(u"wellComeTitle")
        self.wellComeTitle.setStyleSheet(u"color: #fff;")

        self.gridLayout_29.addWidget(self.wellComeTitle, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_21, 1, 0, 1, 1)

        self.stackedWidgetMainContent.addWidget(self.HomePage)
        self.trackCattleHealth = QWidget()
        self.trackCattleHealth.setObjectName(u"trackCattleHealth")
        self.gridLayout_20 = QGridLayout(self.trackCattleHealth)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.frame_16 = QFrame(self.trackCattleHealth)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_16)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 80))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_17)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: #fff;")

        self.gridLayout_23.addWidget(self.label_7, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.frame_17, 0, 0, 1, 1)

        self.tabWidget_5 = QTabWidget(self.frame_16)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.healthRecords = QWidget()
        self.healthRecords.setObjectName(u"healthRecords")
        self.gridLayout_32 = QGridLayout(self.healthRecords)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.searchBarHealthHist = QLineEdit(self.healthRecords)
        self.searchBarHealthHist.setObjectName(u"searchBarHealthHist")
        self.searchBarHealthHist.setStyleSheet(u"padding: 10px;\n"
"color: #fff;")

        self.horizontalLayout_30.addWidget(self.searchBarHealthHist)


        self.gridLayout_32.addLayout(self.horizontalLayout_30, 2, 0, 1, 1)

        self.frame_27 = QFrame(self.healthRecords)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 61))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_52 = QLabel(self.frame_27)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_29.addWidget(self.label_52)

        self.export_as_excel_1 = QPushButton(self.frame_27)
        self.export_as_excel_1.setObjectName(u"export_as_excel_1")
        self.export_as_excel_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.export_as_excel_1.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: #004d00;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #009900;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons_svg/images/icons-svg/icons8_microsoft_excel.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_as_excel_1.setIcon(icon4)
        self.export_as_excel_1.setIconSize(QSize(20, 20))

        self.horizontalLayout_29.addWidget(self.export_as_excel_1)


        self.gridLayout_32.addWidget(self.frame_27, 0, 0, 1, 1)

        self.tableContainer = QStackedWidget(self.healthRecords)
        self.tableContainer.setObjectName(u"tableContainer")
        self.tableContainer.setMinimumSize(QSize(745, 290))
        self.tableContainer.setFrameShape(QFrame.StyledPanel)
        self.tableContainer.setFrameShadow(QFrame.Raised)
        self.tableContainerPage1 = QWidget()
        self.tableContainerPage1.setObjectName(u"tableContainerPage1")
        self.gridLayout_68 = QGridLayout(self.tableContainerPage1)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.tableView = QTableView(self.tableContainerPage1)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGridStyle(Qt.DotLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(150)
        self.tableView.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_68.addWidget(self.tableView, 0, 0, 1, 1)

        self.tableContainer.addWidget(self.tableContainerPage1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_69 = QGridLayout(self.page)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.frame_36 = QFrame(self.page)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_36)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_7 = QWidget(self.frame_36)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_26 = QVBoxLayout(self.widget_7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_42 = QLabel(self.widget_7)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_26.addWidget(self.label_42)

        self.label_43 = QLabel(self.widget_7)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setPixmap(QPixmap(u":/icons_svg/images/icons-svg/icons8_update_left_rotation.svg"))
        self.label_43.setScaledContents(False)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_43)


        self.verticalLayout_25.addWidget(self.widget_7)


        self.gridLayout_69.addWidget(self.frame_36, 0, 0, 1, 1)

        self.tableContainer.addWidget(self.page)

        self.gridLayout_32.addWidget(self.tableContainer, 3, 0, 1, 1)

        self.frame_37 = QFrame(self.healthRecords)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_67 = QGridLayout(self.frame_37)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.dataViewOptionsHealthComboBox = QComboBox(self.frame_37)
        self.dataViewOptionsHealthComboBox.addItem("")
        self.dataViewOptionsHealthComboBox.addItem("")
        self.dataViewOptionsHealthComboBox.setObjectName(u"dataViewOptionsHealthComboBox")
        self.dataViewOptionsHealthComboBox.setStyleSheet(u"#dataViewOptionsHealthComboBox {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	background-color: #fff;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"#dataViewOptionsHealthComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#dataViewOptionsHealthComboBox::down-arrow {\n"
"	image: url(:/icons_svg/images/icons-svg/arrow-204-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"#dataViewOptionsHealthComboBox:on {\n"
" 	border: 4px solid #c2dbfe;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"	font-size: 12px;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding:5px;\n"
"	background-color: #fff;\n"
"	outline: 0px;  /*\u53bb\u865a\u7ebf*/\n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left:10px;\n"
"	background-color:#FFFFFF;\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"")

        self.gridLayout_67.addWidget(self.dataViewOptionsHealthComboBox, 0, 0, 1, 1)

        self.label_44 = QLabel(self.frame_37)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_67.addWidget(self.label_44, 0, 1, 1, 1)


        self.gridLayout_32.addWidget(self.frame_37, 1, 0, 1, 1)

        self.tabWidget_5.addTab(self.healthRecords, "")
        self.notificationsPanel = QWidget()
        self.notificationsPanel.setObjectName(u"notificationsPanel")
        self.gridLayout_34 = QGridLayout(self.notificationsPanel)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.notifications = QFrame(self.notificationsPanel)
        self.notifications.setObjectName(u"notifications")
        self.notifications.setStyleSheet(u"#notifications, QLabel, QFrame{\n"
"	background: #fff;\n"
"}")
        self.notifications.setFrameShape(QFrame.StyledPanel)
        self.notifications.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.notifications)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.frame_32 = QFrame(self.notifications)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"#frame_32{\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_32)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.frame1 = QFrame(self.frame_32)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(0, 81))
        self.verticalLayout_43 = QVBoxLayout(self.frame1)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_56 = QLabel(self.frame1)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"")

        self.horizontalLayout_28.addWidget(self.label_56)

        self.label_58 = QLabel(self.frame1)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_28.addWidget(self.label_58)


        self.verticalLayout_43.addLayout(self.horizontalLayout_28)

        self.line_3 = QFrame(self.frame1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_43.addWidget(self.line_3)

        self.frame2 = QFrame(self.frame1)
        self.frame2.setObjectName(u"frame2")
        self.horizontalLayout_27 = QHBoxLayout(self.frame2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.checkUpPurpose = QComboBox(self.frame2)
        self.checkUpPurpose.addItem("")
        self.checkUpPurpose.addItem("")
        self.checkUpPurpose.addItem("")
        self.checkUpPurpose.setObjectName(u"checkUpPurpose")
        self.checkUpPurpose.setStyleSheet(u"#comboBox {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	background-color: #fff;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"#comboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#comboBox::down-arrow {\n"
"image: url(:/icons_svg/images/icons-svg/arrow-204-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"#comboBox:on {\n"
" 	border: 4px solid #c2dbfe;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"	font-size: 12px;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding:5px;\n"
"	background-color: #fff;\n"
"	outline: 0px;  /*\u53bb\u865a\u7ebf*/\n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left:10px;\n"
"	background-color:#FFFFFF;\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_27.addWidget(self.checkUpPurpose)

        self.frame_33 = QFrame(self.frame2)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"#frame_33 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QDateTimeEdit,\n"
"QPushButton\n"
" {\n"
"	border: none;\n"
"	background: #fff;\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_33)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.checkUpDate = QDateTimeEdit(self.frame_33)
        self.checkUpDate.setObjectName(u"checkUpDate")
        self.checkUpDate.setMaximumSize(QSize(16777215, 34))
        self.checkUpDate.setStyleSheet(u"border-bottom: 1px solid #ccc;\n"
"padding: 5px;\n"
"")
        self.checkUpDate.setFrame(True)
        self.checkUpDate.setReadOnly(False)
        self.checkUpDate.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.checkUpDate.setKeyboardTracking(True)
        self.checkUpDate.setCalendarPopup(False)

        self.gridLayout_38.addWidget(self.checkUpDate, 0, 0, 1, 1)

        self.popupCalendar = QPushButton(self.frame_33)
        self.popupCalendar.setObjectName(u"popupCalendar")
        self.popupCalendar.setMinimumSize(QSize(34, 34))
        self.popupCalendar.setMaximumSize(QSize(34, 34))
        self.popupCalendar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.popupCalendar.setStyleSheet(u"background: #fff;")
        icon5 = QIcon()
        icon5.addFile(u":/icons_svg/images/icons-svg/icons8_schedule.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.popupCalendar.setIcon(icon5)
        self.popupCalendar.setIconSize(QSize(30, 30))
        self.popupCalendar.setCheckable(True)

        self.gridLayout_38.addWidget(self.popupCalendar, 0, 1, 1, 1)


        self.horizontalLayout_27.addWidget(self.frame_33)


        self.verticalLayout_43.addWidget(self.frame2)


        self.gridLayout_36.addWidget(self.frame1, 1, 0, 1, 3)

        self.horizontalSpacer_17 = QSpacerItem(169, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_17, 3, 0, 1, 1)

        self.btnSetAppointment = QPushButton(self.frame_32)
        self.btnSetAppointment.setObjectName(u"btnSetAppointment")
        self.btnSetAppointment.setMinimumSize(QSize(80, 0))
        self.btnSetAppointment.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnSetAppointment.setStyleSheet(u"QPushButton {\n"
"    min-width: 30px;\n"
"    padding: 10px 25px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    margin-bottom: 5px;\n"
"	background: #0047b3;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #003366;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-library-add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSetAppointment.setIcon(icon6)

        self.gridLayout_36.addWidget(self.btnSetAppointment, 3, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(172, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_18, 3, 2, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_36.addItem(self.verticalSpacer_13, 4, 1, 1, 1)

        self.frame_39 = QFrame(self.frame_32)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_39)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.line_4 = QFrame(self.frame_39)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_44.addWidget(self.line_4)

        self.label_61 = QLabel(self.frame_39)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"padding: 3px;")

        self.verticalLayout_44.addWidget(self.label_61)

        self.vetOrgName = QLineEdit(self.frame_39)
        self.vetOrgName.setObjectName(u"vetOrgName")
        self.vetOrgName.setStyleSheet(u"QLineEdit{\n"
"	background-color: #fff;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #004d00;\n"
"}")

        self.verticalLayout_44.addWidget(self.vetOrgName)


        self.gridLayout_36.addWidget(self.frame_39, 2, 0, 1, 3)


        self.gridLayout_37.addWidget(self.frame_32, 1, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_37.addItem(self.verticalSpacer_16, 0, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 23, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_37.addItem(self.verticalSpacer_15, 2, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(93, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_19, 1, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(93, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_20, 1, 2, 1, 1)


        self.gridLayout_34.addWidget(self.notifications, 1, 0, 1, 1)

        self.frame_31 = QFrame(self.notificationsPanel)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 38))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_31)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_54 = QLabel(self.frame_31)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_35.addWidget(self.label_54, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.frame_31, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.notificationsPanel, "")
        self.diseaseTracking = QWidget()
        self.diseaseTracking.setObjectName(u"diseaseTracking")
        self.gridLayout_39 = QGridLayout(self.diseaseTracking)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.frame_34 = QFrame(self.diseaseTracking)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_34)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.plotCard = QVBoxLayout()
        self.plotCard.setObjectName(u"plotCard")

        self.gridLayout_41.addLayout(self.plotCard, 2, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_34, 1, 0, 1, 1)

        self.frame_35 = QFrame(self.diseaseTracking)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 61))
        self.frame_35.setMaximumSize(QSize(16777215, 33))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_35)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.label_59 = QLabel(self.frame_35)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: rgb(170, 255, 255)")

        self.gridLayout_40.addWidget(self.label_59, 0, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_35)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: #004d00;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #009900;\n"
"}")
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setIconSize(QSize(20, 20))

        self.gridLayout_40.addWidget(self.pushButton_10, 0, 1, 1, 1)


        self.gridLayout_39.addWidget(self.frame_35, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.diseaseTracking, "")

        self.gridLayout_22.addWidget(self.tabWidget_5, 1, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_16, 0, 0, 1, 1)

        self.stackedWidgetMainContent.addWidget(self.trackCattleHealth)
        self.manageBreeding = QWidget()
        self.manageBreeding.setObjectName(u"manageBreeding")
        self.gridLayout_12 = QGridLayout(self.manageBreeding)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.widget_4 = QWidget(self.manageBreeding)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_16 = QVBoxLayout(self.widget_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 50))
        self.widget_5.setMaximumSize(QSize(16777215, 141))
        self.gridLayout_18 = QGridLayout(self.widget_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: #fff;")

        self.gridLayout_18.addWidget(self.label_6, 0, 0, 1, 1)


        self.verticalLayout_16.addWidget(self.widget_5)

        self.tabWidget_2 = QTabWidget(self.widget_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"QLineEdit{\n"
"	padding: 10px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #fff;\n"
"}\n"
"\n"
"QDateEdit {\n"
"                border: 2px solid #5A5A5A;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                min-width: 150px;\n"
"            }\n"
"            QDateEdit::drop-down {\n"
"                subcontrol-origin: padding;\n"
"                subcontrol-position: top right;\n"
"                width: 15px;\n"
"                border-left-width: 1px;\n"
"                border-left-color: darkgray;\n"
"                border-left-style: solid; \n"
"                border-top-right-radius: 3px;\n"
"                border-bottom-right-radius: 3px;\n"
"            }\n"
"            QDateEdit::down-arrow {\n"
"                image: url(down_arrow.png);\n"
"                width: 10px;\n"
"                height: 10px;\n"
"            }")
        self.breedingTracking = QWidget()
        self.breedingTracking.setObjectName(u"breedingTracking")
        self.gridLayout_19 = QGridLayout(self.breedingTracking)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.frame_26 = QFrame(self.breedingTracking)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"*{\n"
"	background-color: #fff;\n"
"	color: #000;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_26)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_34 = QLabel(self.frame_26)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(727, 13))

        self.gridLayout_44.addWidget(self.label_34, 0, 0, 1, 1)

        self.frame_40 = QFrame(self.frame_26)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(727, 56))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_40)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.pushButton_11 = QPushButton(self.frame_40)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: #004d00;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #009900;\n"
"}")
        self.pushButton_11.setIcon(icon4)

        self.gridLayout_45.addWidget(self.pushButton_11, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_40)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"padding: 10px;\n"
"color: #fff;\n"
"background: #404040;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background: #102030\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons_svg/images/icons-svg/icons8_plus_math.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon7)

        self.gridLayout_45.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_40)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"padding: 10px;\n"
"color: #fff;\n"
"background: #404040;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background: #102030\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-view-module.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon8)

        self.gridLayout_45.addWidget(self.pushButton_12, 0, 2, 1, 1)


        self.gridLayout_44.addWidget(self.frame_40, 1, 0, 1, 1)

        self.frame_41 = QFrame(self.frame_26)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_41)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.trackBreedingCyclesTable = QVBoxLayout()
        self.trackBreedingCyclesTable.setObjectName(u"trackBreedingCyclesTable")

        self.gridLayout_46.addLayout(self.trackBreedingCyclesTable, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.frame_41, 2, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_26, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.breedingTracking, "")
        self.pregnancyMonitoring = QWidget()
        self.pregnancyMonitoring.setObjectName(u"pregnancyMonitoring")
        self.gridLayout_47 = QGridLayout(self.pregnancyMonitoring)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.frame_42 = QFrame(self.pregnancyMonitoring)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"\n"
"#frame_43, #frame_44, #frame_45, #frame_46{\n"
"	border: 1px solid  #ccccff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    min-width: 30px;\n"
"    padding: 10px 25px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    margin-bottom: 5px;\n"
"	background:  #80aaff;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #003366;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #ccccff;\n"
"	font-weight: 500;\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_42)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.frame_47 = QFrame(self.frame_42)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(721, 320))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_47)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.frame_46 = QFrame(self.frame_47)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.frame_46)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.label_38 = QLabel(self.frame_46)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"")

        self.gridLayout_53.addWidget(self.label_38, 0, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_46)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(80, 0))
        self.pushButton_17.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_53.addWidget(self.pushButton_17, 2, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_9, 2, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_53.addItem(self.verticalSpacer_21, 3, 1, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_53.addItem(self.verticalSpacer_20, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_10, 2, 2, 1, 1)


        self.gridLayout_48.addWidget(self.frame_46, 0, 3, 1, 1)

        self.frame_45 = QFrame(self.frame_47)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.frame_45)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_52.addItem(self.horizontalSpacer_8, 2, 2, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_52.addItem(self.verticalSpacer_18, 3, 1, 1, 1)

        self.label_37 = QLabel(self.frame_45)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"")

        self.gridLayout_52.addWidget(self.label_37, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_52.addItem(self.horizontalSpacer_7, 2, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_45)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(80, 0))
        self.pushButton_16.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_52.addWidget(self.pushButton_16, 2, 1, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_52.addItem(self.verticalSpacer_19, 1, 1, 1, 1)


        self.gridLayout_48.addWidget(self.frame_45, 0, 2, 1, 1)

        self.frame_44 = QFrame(self.frame_47)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.frame_44)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.pushButton_15 = QPushButton(self.frame_44)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(80, 0))
        self.pushButton_15.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_51.addWidget(self.pushButton_15, 2, 1, 1, 1)

        self.label_36 = QLabel(self.frame_44)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"")

        self.gridLayout_51.addWidget(self.label_36, 0, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_51.addItem(self.verticalSpacer_14, 3, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_51.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_51.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_51.addItem(self.verticalSpacer_17, 1, 1, 1, 1)


        self.gridLayout_48.addWidget(self.frame_44, 0, 1, 2, 1)

        self.frame_43 = QFrame(self.frame_47)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.frame_43)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.label_35 = QLabel(self.frame_43)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"")

        self.gridLayout_50.addWidget(self.label_35, 0, 0, 1, 3)

        self.verticalSpacer_9 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_50.addItem(self.verticalSpacer_9, 1, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_43)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(80, 0))
        self.pushButton_13.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_50.addWidget(self.pushButton_13, 2, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_50.addItem(self.verticalSpacer_10, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_50.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_50.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)


        self.gridLayout_48.addWidget(self.frame_43, 1, 2, 1, 2)


        self.gridLayout_49.addWidget(self.frame_47, 1, 0, 1, 1)


        self.gridLayout_47.addWidget(self.frame_42, 1, 0, 1, 1)

        self.frame_56 = QFrame(self.pregnancyMonitoring)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"#frame_56{\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.gridLayout_60 = QGridLayout(self.frame_56)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.label_22 = QLabel(self.frame_56)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_60.addWidget(self.label_22, 0, 0, 1, 1)


        self.gridLayout_47.addWidget(self.frame_56, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.pregnancyMonitoring, "")
        self.notificationsBreeding = QWidget()
        self.notificationsBreeding.setObjectName(u"notificationsBreeding")
        self.gridLayout_57 = QGridLayout(self.notificationsBreeding)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.notifications_2 = QFrame(self.notificationsBreeding)
        self.notifications_2.setObjectName(u"notifications_2")
        self.notifications_2.setStyleSheet(u"#notifications, QLabel, QFrame{\n"
"	background: #fff;\n"
"}")
        self.notifications_2.setFrameShape(QFrame.StyledPanel)
        self.notifications_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_54 = QGridLayout(self.notifications_2)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.verticalSpacer_22 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_54.addItem(self.verticalSpacer_22, 0, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(93, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_21, 1, 0, 1, 1)

        self.frame_48 = QFrame(self.notifications_2)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"#frame_48{\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_55 = QGridLayout(self.frame_48)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.horizontalSpacer_22 = QSpacerItem(169, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_22, 3, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_48)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(80, 0))
        self.pushButton_18.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"    min-width: 30px;\n"
"    padding: 10px 25px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    margin-bottom: 5px;\n"
"	background: #0047b3;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #003366;\n"
"}")
        self.pushButton_18.setIcon(icon6)

        self.gridLayout_55.addWidget(self.pushButton_18, 3, 1, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(172, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_23, 3, 2, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_55.addItem(self.verticalSpacer_23, 4, 1, 1, 1)

        self.frame_52 = QFrame(self.frame_48)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_52)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.line_7 = QFrame(self.frame_52)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_46.addWidget(self.line_7)

        self.label_64 = QLabel(self.frame_52)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"padding: 3px;\n"
"color: #000;")

        self.verticalLayout_46.addWidget(self.label_64)

        self.vetOrgName_2 = QLineEdit(self.frame_52)
        self.vetOrgName_2.setObjectName(u"vetOrgName_2")
        self.vetOrgName_2.setStyleSheet(u"QLineEdit{\n"
"	background-color: #fff;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #004d00;\n"
"}")

        self.verticalLayout_46.addWidget(self.vetOrgName_2)


        self.gridLayout_55.addWidget(self.frame_52, 2, 0, 1, 3)

        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 81))
        self.verticalLayout_45 = QVBoxLayout(self.frame_49)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_54 = QFrame(self.frame_49)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"color: black;")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_40 = QLabel(self.frame_54)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_33.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_54)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_33.addWidget(self.label_41)


        self.verticalLayout_45.addWidget(self.frame_54)

        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.horizontalLayout_34 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.comboBox_2 = QComboBox(self.frame_50)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"#comboBox_2 {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	background-color: #fff;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"#comboBox_2::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#comboBox_2::down-arrow {\n"
"   image: url(images/icons-svg/arrow-204-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"#comboBox_2:on {\n"
" 	border: 4px solid #c2dbfe;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"	font-size: 12px;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding:5px;\n"
"	background-color: #fff;\n"
"	outline: 0px;  \n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left:10px;\n"
"	background-color:#FFFFFF;\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_34.addWidget(self.comboBox_2)

        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"#frame_33 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QDateTimeEdit,\n"
"QPushButton\n"
" {\n"
"	border: none;\n"
"	background: #fff;\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_56 = QGridLayout(self.frame_51)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.dateTimeEdit_2 = QDateTimeEdit(self.frame_51)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setMaximumSize(QSize(16777215, 34))
        self.dateTimeEdit_2.setStyleSheet(u"border-bottom: 1px solid #ccc;\n"
"padding: 5px;\n"
"")
        self.dateTimeEdit_2.setFrame(True)
        self.dateTimeEdit_2.setReadOnly(False)
        self.dateTimeEdit_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEdit_2.setKeyboardTracking(True)
        self.dateTimeEdit_2.setCalendarPopup(False)

        self.gridLayout_56.addWidget(self.dateTimeEdit_2, 0, 0, 1, 1)

        self.popupCalendar_2 = QPushButton(self.frame_51)
        self.popupCalendar_2.setObjectName(u"popupCalendar_2")
        self.popupCalendar_2.setMinimumSize(QSize(34, 34))
        self.popupCalendar_2.setMaximumSize(QSize(34, 34))
        self.popupCalendar_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.popupCalendar_2.setStyleSheet(u"background: #fff;")
        self.popupCalendar_2.setIcon(icon5)
        self.popupCalendar_2.setIconSize(QSize(30, 30))
        self.popupCalendar_2.setCheckable(True)

        self.gridLayout_56.addWidget(self.popupCalendar_2, 0, 1, 1, 1)


        self.horizontalLayout_34.addWidget(self.frame_51)


        self.verticalLayout_45.addWidget(self.frame_50)


        self.gridLayout_55.addWidget(self.frame_49, 1, 0, 1, 3)


        self.gridLayout_54.addWidget(self.frame_48, 1, 1, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(93, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_24, 1, 2, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 23, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_54.addItem(self.verticalSpacer_24, 2, 1, 1, 1)


        self.gridLayout_57.addWidget(self.notifications_2, 1, 0, 1, 1)

        self.frame_53 = QFrame(self.notificationsBreeding)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.gridLayout_58 = QGridLayout(self.frame_53)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.label_39 = QLabel(self.frame_53)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_58.addWidget(self.label_39, 0, 0, 1, 1)


        self.gridLayout_57.addWidget(self.frame_53, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.notificationsBreeding, "")
        self.geneticTracking = QWidget()
        self.geneticTracking.setObjectName(u"geneticTracking")
        self.gridLayout_17 = QGridLayout(self.geneticTracking)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tabWidget_2.addTab(self.geneticTracking, "")

        self.verticalLayout_16.addWidget(self.tabWidget_2)


        self.gridLayout_12.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stackedWidgetMainContent.addWidget(self.manageBreeding)
        self.manageFinancials = QWidget()
        self.manageFinancials.setObjectName(u"manageFinancials")
        self.gridLayout_6 = QGridLayout(self.manageFinancials)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_11 = QFrame(self.manageFinancials)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_11)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 71))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_13)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #fff;")

        self.gridLayout_14.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_13, 0, 0, 1, 1)

        self.tabWidget_3 = QTabWidget(self.frame_11)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.profitAnalysis = QWidget()
        self.profitAnalysis.setObjectName(u"profitAnalysis")
        self.tabWidget_3.addTab(self.profitAnalysis, "")
        self.trackFarmExpenses = QWidget()
        self.trackFarmExpenses.setObjectName(u"trackFarmExpenses")
        self.tabWidget_3.addTab(self.trackFarmExpenses, "")
        self.reportsAndAnalytics = QWidget()
        self.reportsAndAnalytics.setObjectName(u"reportsAndAnalytics")
        self.tabWidget_3.addTab(self.reportsAndAnalytics, "")

        self.gridLayout_13.addWidget(self.tabWidget_3, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_11, 0, 0, 1, 1)

        self.stackedWidgetMainContent.addWidget(self.manageFinancials)
        self.manageInventory = QWidget()
        self.manageInventory.setObjectName(u"manageInventory")
        self.gridLayout_15 = QGridLayout(self.manageInventory)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_14 = QFrame(self.manageInventory)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_14)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_15)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: #fff;")

        self.gridLayout_21.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_15, 0, 0, 1, 1)

        self.tabWidget_4 = QTabWidget(self.frame_14)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.feedAndSupplies = QWidget()
        self.feedAndSupplies.setObjectName(u"feedAndSupplies")
        self.gridLayout_33 = QGridLayout(self.feedAndSupplies)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.frame_23 = QFrame(self.feedAndSupplies)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"#frame_23, *{\n"
"	background-color: #fff;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_23)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_25 = QLabel(self.frame_23)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_18.addWidget(self.label_25)

        self.addInventoryBtn = QPushButton(self.frame_23)
        self.addInventoryBtn.setObjectName(u"addInventoryBtn")
        self.addInventoryBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addInventoryBtn.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"padding: 10px;\n"
"color: #fff;\n"
"background: #404040;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background: #102030\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons-svg/icons8_plus_math.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addInventoryBtn.setIcon(icon9)

        self.horizontalLayout_18.addWidget(self.addInventoryBtn)

        self.exportExcelBtn = QPushButton(self.frame_23)
        self.exportExcelBtn.setObjectName(u"exportExcelBtn")
        self.exportExcelBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exportExcelBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: #004d00;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #009900;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons-svg/icons8_microsoft_excel.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportExcelBtn.setIcon(icon10)

        self.horizontalLayout_18.addWidget(self.exportExcelBtn)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.searchBarFeedSupplies = QLineEdit(self.frame_23)
        self.searchBarFeedSupplies.setObjectName(u"searchBarFeedSupplies")
        self.searchBarFeedSupplies.setStyleSheet(u"padding: 10px;\n"
"color: #000;")

        self.horizontalLayout_13.addWidget(self.searchBarFeedSupplies)

        self.searchInventoryBtn = QPushButton(self.frame_23)
        self.searchInventoryBtn.setObjectName(u"searchInventoryBtn")
        self.searchInventoryBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchInventoryBtn.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"padding: 10px;\n"
"color: #fff;\n"
"background: #404040;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background: #102030\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchInventoryBtn.setIcon(icon11)

        self.horizontalLayout_13.addWidget(self.searchInventoryBtn)


        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.tableWidget_3 = QTableWidget(self.frame_23)
        if (self.tableWidget_3.columnCount() < 4):
            self.tableWidget_3.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.tableWidget_3)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_26 = QLabel(self.frame_23)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_17.addWidget(self.label_26)

        self.radioButton_7 = QRadioButton(self.frame_23)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_17.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.frame_23)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.horizontalLayout_17.addWidget(self.radioButton_8)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)


        self.gridLayout_33.addWidget(self.frame_23, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.feedAndSupplies, "")
        self.medicationRecords = QWidget()
        self.medicationRecords.setObjectName(u"medicationRecords")
        self.gridLayout_42 = QGridLayout(self.medicationRecords)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.frame_24 = QFrame(self.medicationRecords)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"#frame_24, *{\n"
"	background-color: #fff;\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_24)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_31 = QLabel(self.frame_24)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_19.addWidget(self.label_31)

        self.addMedicationBtn = QPushButton(self.frame_24)
        self.addMedicationBtn.setObjectName(u"addMedicationBtn")
        self.addMedicationBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addMedicationBtn.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"padding: 10px;\n"
"color: #fff;\n"
"background: #404040;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background: #102030\n"
"}\n"
"")
        self.addMedicationBtn.setIcon(icon9)

        self.horizontalLayout_19.addWidget(self.addMedicationBtn)

        self.exportExcelMedicationBtn = QPushButton(self.frame_24)
        self.exportExcelMedicationBtn.setObjectName(u"exportExcelMedicationBtn")
        self.exportExcelMedicationBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exportExcelMedicationBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: #004d00;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #009900;\n"
"}")
        self.exportExcelMedicationBtn.setIcon(icon10)

        self.horizontalLayout_19.addWidget(self.exportExcelMedicationBtn)


        self.verticalLayout_23.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.searchBarMedication = QLineEdit(self.frame_24)
        self.searchBarMedication.setObjectName(u"searchBarMedication")
        self.searchBarMedication.setStyleSheet(u"padding: 10px;\n"
"color: #000;")

        self.horizontalLayout_20.addWidget(self.searchBarMedication)

        self.searchMedicationBtn = QPushButton(self.frame_24)
        self.searchMedicationBtn.setObjectName(u"searchMedicationBtn")
        self.searchMedicationBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchMedicationBtn.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"padding: 10px;\n"
"color: #fff;\n"
"background: #404040;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background: #102030\n"
"}\n"
"")
        self.searchMedicationBtn.setIcon(icon11)

        self.horizontalLayout_20.addWidget(self.searchMedicationBtn)


        self.verticalLayout_23.addLayout(self.horizontalLayout_20)

        self.tableWidget_4 = QTableWidget(self.frame_24)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_23.addWidget(self.tableWidget_4)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_30 = QLabel(self.frame_24)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_21.addWidget(self.label_30)

        self.radioButton_10 = QRadioButton(self.frame_24)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.horizontalLayout_21.addWidget(self.radioButton_10)

        self.radioButton_11 = QRadioButton(self.frame_24)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.horizontalLayout_21.addWidget(self.radioButton_11)


        self.verticalLayout_23.addLayout(self.horizontalLayout_21)


        self.gridLayout_42.addWidget(self.frame_24, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.medicationRecords, "")
        self.resourceAllocation = QWidget()
        self.resourceAllocation.setObjectName(u"resourceAllocation")
        self.gridLayout_43 = QGridLayout(self.resourceAllocation)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.frame_25 = QFrame(self.resourceAllocation)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"#frame_25, *{\n"
"	background: #fff;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_25)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_32 = QLabel(self.frame_25)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_22.addWidget(self.label_32)

        self.pushButton_3 = QPushButton(self.frame_25)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"padding: 10px;\n"
"color: #fff;\n"
"background: #404040;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background: #102030\n"
"}\n"
"")
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_22.addWidget(self.pushButton_3)

        self.pushButton_7 = QPushButton(self.frame_25)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background-color: #004d00;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #009900;\n"
"}")
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setIconSize(QSize(20, 20))

        self.horizontalLayout_22.addWidget(self.pushButton_7)


        self.verticalLayout_24.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lineEdit = QLineEdit(self.frame_25)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"padding: 10px;\n"
"color: #000;")

        self.horizontalLayout_23.addWidget(self.lineEdit)

        self.pushButton_4 = QPushButton(self.frame_25)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"padding: 10px;\n"
"color: #fff;\n"
"background: #404040;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background: #102030\n"
"}\n"
"")
        self.pushButton_4.setIcon(icon11)

        self.horizontalLayout_23.addWidget(self.pushButton_4)


        self.verticalLayout_24.addLayout(self.horizontalLayout_23)

        self.tableWidget_5 = QTableWidget(self.frame_25)
        if (self.tableWidget_5.columnCount() < 6):
            self.tableWidget_5.setColumnCount(6)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_24.addWidget(self.tableWidget_5)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_33 = QLabel(self.frame_25)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_32.addWidget(self.label_33)

        self.radioButton_12 = QRadioButton(self.frame_25)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.horizontalLayout_32.addWidget(self.radioButton_12)

        self.radioButton_13 = QRadioButton(self.frame_25)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.horizontalLayout_32.addWidget(self.radioButton_13)

        self.radioButton_14 = QRadioButton(self.frame_25)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.horizontalLayout_32.addWidget(self.radioButton_14)

        self.radioButton_15 = QRadioButton(self.frame_25)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.horizontalLayout_32.addWidget(self.radioButton_15)


        self.verticalLayout_24.addLayout(self.horizontalLayout_32)


        self.gridLayout_43.addWidget(self.frame_25, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.resourceAllocation, "")

        self.gridLayout_16.addWidget(self.tabWidget_4, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_14, 0, 0, 1, 1)

        self.stackedWidgetMainContent.addWidget(self.manageInventory)
        self.addAnimal = QWidget()
        self.addAnimal.setObjectName(u"addAnimal")
        self.gridLayout_7 = QGridLayout(self.addAnimal)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget = QWidget(self.addAnimal)
        self.widget.setObjectName(u"widget")
        self.gridLayout_8 = QGridLayout(self.widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_9.addWidget(self.label_11)


        self.gridLayout_8.addWidget(self.frame_8, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setMovable(True)
        self.addAnimal1 = QWidget()
        self.addAnimal1.setObjectName(u"addAnimal1")
        self.gridLayout_11 = QGridLayout(self.addAnimal1)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea = QScrollArea(self.addAnimal1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 316, 526))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.enterAnimalFrame = QFrame(self.scrollAreaWidgetContents)
        self.enterAnimalFrame.setObjectName(u"enterAnimalFrame")
        self.enterAnimalFrame.setStyleSheet(u"*{\n"
"	background-color: #fff;\n"
"	color: #000;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	padding: 10px;\n"
"}\n"
"\n"
"\n"
"#enterAnimalFrame{\n"
"	border: 2px solid #003366;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}")
        self.enterAnimalFrame.setFrameShape(QFrame.StyledPanel)
        self.enterAnimalFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.enterAnimalFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.enterAnimalFrame)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_12.addWidget(self.label_14)

        self.line_5 = QFrame(self.enterAnimalFrame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_5)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.enterAnimalFrame)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)

        self.label_19 = QLabel(self.enterAnimalFrame)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_11.addWidget(self.label_19)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tagIdInput = QLineEdit(self.enterAnimalFrame)
        self.tagIdInput.setObjectName(u"tagIdInput")

        self.horizontalLayout_8.addWidget(self.tagIdInput)

        self.animalBreedInput = QLineEdit(self.enterAnimalFrame)
        self.animalBreedInput.setObjectName(u"animalBreedInput")

        self.horizontalLayout_8.addWidget(self.animalBreedInput)

        self.label_20 = QLabel(self.enterAnimalFrame)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_8.addWidget(self.label_20)

        self.ageInMonths = QDoubleSpinBox(self.enterAnimalFrame)
        self.ageInMonths.setObjectName(u"ageInMonths")
        self.ageInMonths.setMaximum(1000.990000000000009)
        self.ageInMonths.setSingleStep(0.500000000000000)

        self.horizontalLayout_8.addWidget(self.ageInMonths)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.label_15 = QLabel(self.enterAnimalFrame)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_11.addWidget(self.label_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.newAnimalWeightInput = QDoubleSpinBox(self.enterAnimalFrame)
        self.newAnimalWeightInput.setObjectName(u"newAnimalWeightInput")
        self.newAnimalWeightInput.setMaximum(1000.990000000000009)
        self.newAnimalWeightInput.setSingleStep(0.500000000000000)

        self.horizontalLayout_9.addWidget(self.newAnimalWeightInput)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.label_27 = QLabel(self.enterAnimalFrame)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_12.addWidget(self.label_27)

        self.departmentInput = QComboBox(self.enterAnimalFrame)
        self.departmentInput.addItem("")
        self.departmentInput.addItem("")
        self.departmentInput.addItem("")
        self.departmentInput.setObjectName(u"departmentInput")
        self.departmentInput.setStyleSheet(u"#departmentInput {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	background-color: #fff;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"#departmentInput::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#departmentInput::down-arrow {\n"
"   image: url(images/icons-svg/arrow-204-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"#departmentInput:on {\n"
" 	border: 4px solid #c2dbfe;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"	font-size: 12px;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding:5px;\n"
"	background-color: #fff;\n"
"	outline: 0px;  \n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left:10px;\n"
"	background-color:#FFFFFF;\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.departmentInput)

        self.label_23 = QLabel(self.enterAnimalFrame)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_12.addWidget(self.label_23)

        self.sexInput = QComboBox(self.enterAnimalFrame)
        self.sexInput.addItem("")
        self.sexInput.addItem("")
        self.sexInput.setObjectName(u"sexInput")
        self.sexInput.setStyleSheet(u"#sexInput {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	background-color: #fff;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"#sexInput::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#sexInput::down-arrow {\n"
"   image: url(images/icons-svg/arrow-204-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"#sexInput:on {\n"
" 	border: 4px solid #c2dbfe;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"	font-size: 12px;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding:5px;\n"
"	background-color: #fff;\n"
"	outline: 0px;  \n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left:10px;\n"
"	background-color:#FFFFFF;\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.sexInput)

        self.label_16 = QLabel(self.enterAnimalFrame)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_12.addWidget(self.label_16)

        self.animalCharacteristicsInput = QPlainTextEdit(self.enterAnimalFrame)
        self.animalCharacteristicsInput.setObjectName(u"animalCharacteristicsInput")
        self.animalCharacteristicsInput.setMinimumSize(QSize(0, 100))

        self.verticalLayout_12.addWidget(self.animalCharacteristicsInput)

        self.frame_12 = QFrame(self.enterAnimalFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QPushButton:hover{\n"
"	background: #d9d9d9;\n"
"	color: #1a1a1a;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	padding: 10px;\n"
"	color: #fff;\n"
"	background: #404040;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.submitAnimalDataBtn = QPushButton(self.frame_12)
        self.submitAnimalDataBtn.setObjectName(u"submitAnimalDataBtn")
        self.submitAnimalDataBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submitAnimalDataBtn.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.submitAnimalDataBtn)


        self.verticalLayout_12.addWidget(self.frame_12)


        self.verticalLayout_22.addWidget(self.enterAnimalFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.errLabelAnimalDetails = QLabel(self.addAnimal1)
        self.errLabelAnimalDetails.setObjectName(u"errLabelAnimalDetails")
        self.errLabelAnimalDetails.setStyleSheet(u"color:rgb(238, 255, 84);")

        self.gridLayout_11.addWidget(self.errLabelAnimalDetails, 0, 0, 1, 1)

        self.tabWidget.addTab(self.addAnimal1, "")
        self.viewAnimalData = QWidget()
        self.viewAnimalData.setObjectName(u"viewAnimalData")
        self.gridLayout_9 = QGridLayout(self.viewAnimalData)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.scrollArea_2 = QScrollArea(self.viewAnimalData)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 412, 353))
        self.gridLayout_65 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.frame_9 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.filters = QWidget(self.frame_9)
        self.filters.setObjectName(u"filters")
        self.filters.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_63 = QGridLayout(self.filters)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.frame_10 = QFrame(self.filters)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"color: #fff;\n"
"font-weight: bold;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_62 = QGridLayout(self.frame_10)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.filter_tagId = QRadioButton(self.frame_10)
        self.filter_tagId.setObjectName(u"filter_tagId")

        self.gridLayout_62.addWidget(self.filter_tagId, 1, 3, 1, 1)

        self.filter_animalBreed = QRadioButton(self.frame_10)
        self.filter_animalBreed.setObjectName(u"filter_animalBreed")
        self.filter_animalBreed.setChecked(True)

        self.gridLayout_62.addWidget(self.filter_animalBreed, 1, 2, 1, 1)

        self.activateCategoryAndSexFilters = QCheckBox(self.frame_10)
        self.activateCategoryAndSexFilters.setObjectName(u"activateCategoryAndSexFilters")

        self.gridLayout_62.addWidget(self.activateCategoryAndSexFilters, 1, 0, 1, 1)


        self.gridLayout_63.addWidget(self.frame_10, 2, 0, 1, 1)

        self.secondaryFilterOptions = QFrame(self.filters)
        self.secondaryFilterOptions.setObjectName(u"secondaryFilterOptions")
        self.secondaryFilterOptions.setEnabled(False)
        self.secondaryFilterOptions.setMaximumSize(QSize(16777215, 100))
        self.secondaryFilterOptions.setStyleSheet(u"#secondaryFilterOptions{\n"
"border: 1px solid #fff;\n"
"border-radius: 4px;\n"
"}")
        self.secondaryFilterOptions.setFrameShape(QFrame.StyledPanel)
        self.secondaryFilterOptions.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.secondaryFilterOptions)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_28 = QLabel(self.secondaryFilterOptions)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 0, 1, 1, 1)

        self.sexFilterInput = QComboBox(self.secondaryFilterOptions)
        self.sexFilterInput.addItem("")
        self.sexFilterInput.addItem("")
        self.sexFilterInput.setObjectName(u"sexFilterInput")
        self.sexFilterInput.setMinimumSize(QSize(0, 40))
        self.sexFilterInput.setStyleSheet(u"#sexFilterInput {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	background-color: #fff;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"#sexFilterInput::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#sexFilterInput::down-arrow {\n"
"   image: url(images/icons-svg/arrow-204-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"#sexFilerInput:on {\n"
" 	border: 4px solid #c2dbfe;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"	font-size: 12px;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding:5px;\n"
"	background-color: #fff;\n"
"	outline: 0px;  \n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left:10px;\n"
"	background-color:#FFFFFF;\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.sexFilterInput, 3, 1, 1, 1)

        self.departmentFilterCategory = QComboBox(self.secondaryFilterOptions)
        self.departmentFilterCategory.addItem("")
        self.departmentFilterCategory.addItem("")
        self.departmentFilterCategory.addItem("")
        self.departmentFilterCategory.setObjectName(u"departmentFilterCategory")
        self.departmentFilterCategory.setMinimumSize(QSize(0, 40))
        self.departmentFilterCategory.setStyleSheet(u"#departmentFilterCategory {\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 4px;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	background-color: #fff;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"#departmentFilterCategory::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#departmentFilterCategory::down-arrow {\n"
"   image: url(images/icons-svg/arrow-204-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"#departmentFilterCategory:on {\n"
" 	border: 4px solid #c2dbfe;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"	font-size: 12px;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding:5px;\n"
"	background-color: #fff;\n"
"	outline: 0px;  \n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	padding-left:10px;\n"
"	background-color:#FFFFFF;\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.departmentFilterCategory, 3, 3, 1, 1)

        self.label_29 = QLabel(self.secondaryFilterOptions)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 0, 3, 1, 1)

        self.animalSexcheckBox = QCheckBox(self.secondaryFilterOptions)
        self.animalSexcheckBox.setObjectName(u"animalSexcheckBox")
        self.animalSexcheckBox.setChecked(True)

        self.gridLayout_2.addWidget(self.animalSexcheckBox, 1, 1, 1, 1)

        self.departmentCheckBox = QCheckBox(self.secondaryFilterOptions)
        self.departmentCheckBox.setObjectName(u"departmentCheckBox")

        self.gridLayout_2.addWidget(self.departmentCheckBox, 1, 3, 1, 1)


        self.gridLayout_63.addWidget(self.secondaryFilterOptions, 3, 0, 1, 1)

        self.label_12 = QLabel(self.filters)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_63.addWidget(self.label_12, 1, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.filters)

        self.SearchBar = QWidget(self.frame_9)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setStyleSheet(u"#SearchBar{\n"
"	border: 1px solid #fff;\n"
"	border-radius: 4px;\n"
"	padding: 2px;\n"
"}")
        self.gridLayout_64 = QGridLayout(self.SearchBar)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.searchBar = QLineEdit(self.SearchBar)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setStyleSheet(u"padding: 10px;\n"
"color: #fff;")

        self.gridLayout_64.addWidget(self.searchBar, 2, 1, 1, 1)

        self.searchBtn = QPushButton(self.SearchBar)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchBtn.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"padding: 10px;\n"
"color: #fff;\n"
"background: #404040;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: #003366;\n"
"}")
        self.searchBtn.setIcon(icon11)

        self.gridLayout_64.addWidget(self.searchBtn, 2, 2, 1, 1)

        self.widget_8 = QWidget(self.SearchBar)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_66 = QGridLayout(self.widget_8)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.checkBoxAllFilters = QCheckBox(self.widget_8)
        self.checkBoxAllFilters.setObjectName(u"checkBoxAllFilters")

        self.gridLayout_66.addWidget(self.checkBoxAllFilters, 0, 0, 1, 1)

        self.checkBoxHideFilters = QCheckBox(self.widget_8)
        self.checkBoxHideFilters.setObjectName(u"checkBoxHideFilters")
        self.checkBoxHideFilters.setChecked(True)

        self.gridLayout_66.addWidget(self.checkBoxHideFilters, 1, 0, 1, 1)


        self.gridLayout_64.addWidget(self.widget_8, 2, 0, 1, 1)

        self.animalResultsTable = QTableWidget(self.SearchBar)
        if (self.animalResultsTable.columnCount() < 7):
            self.animalResultsTable.setColumnCount(7)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.animalResultsTable.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.animalResultsTable.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.animalResultsTable.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.animalResultsTable.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.animalResultsTable.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.animalResultsTable.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.animalResultsTable.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        self.animalResultsTable.setObjectName(u"animalResultsTable")
        self.animalResultsTable.setFrameShape(QFrame.NoFrame)
        self.animalResultsTable.setRowCount(0)
        self.animalResultsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.animalResultsTable.horizontalHeader().setMinimumSectionSize(120)
        self.animalResultsTable.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.animalResultsTable.horizontalHeader().setStretchLastSection(True)
        self.animalResultsTable.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_64.addWidget(self.animalResultsTable, 3, 0, 1, 3)


        self.verticalLayout_10.addWidget(self.SearchBar)


        self.gridLayout_65.addWidget(self.frame_9, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_9.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.viewAnimalData, "")

        self.gridLayout_8.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidgetMainContent.addWidget(self.addAnimal)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.gridLayout_24 = QGridLayout(self.settingsPage)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.stackedSettings = QStackedWidget(self.settingsPage)
        self.stackedSettings.setObjectName(u"stackedSettings")
        self.settingsHome = QWidget()
        self.settingsHome.setObjectName(u"settingsHome")
        self.gridLayout_25 = QGridLayout(self.settingsHome)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.frame_18 = QFrame(self.settingsHome)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_18)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"color: #fff;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_19)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.line = QFrame(self.frame_19)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_27.addWidget(self.line, 0, 0, 1, 1)

        self.frame_55 = QFrame(self.frame_19)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_55)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.AboutSection = QFrame(self.frame_55)
        self.AboutSection.setObjectName(u"AboutSection")
        self.AboutSection.setMaximumSize(QSize(16777215, 171))
        self.AboutSection.setStyleSheet(u"#AboutSection{\n"
"	padding: 10px;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 10px;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.AboutSection)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.AboutSection)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_17.addWidget(self.label_10)

        self.label_13 = QLabel(self.AboutSection)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_17.addWidget(self.label_13)

        self.label_17 = QLabel(self.AboutSection)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_17.addWidget(self.label_17)

        self.label_21 = QLabel(self.AboutSection)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_17.addWidget(self.label_21)


        self.horizontalLayout_15.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.deviceName = QLabel(self.AboutSection)
        self.deviceName.setObjectName(u"deviceName")

        self.verticalLayout_18.addWidget(self.deviceName)

        self.softwareVersion = QLabel(self.AboutSection)
        self.softwareVersion.setObjectName(u"softwareVersion")

        self.verticalLayout_18.addWidget(self.softwareVersion)

        self.lastUpdateDate = QLabel(self.AboutSection)
        self.lastUpdateDate.setObjectName(u"lastUpdateDate")

        self.verticalLayout_18.addWidget(self.lastUpdateDate)

        self.installationDate = QLabel(self.AboutSection)
        self.installationDate.setObjectName(u"installationDate")

        self.verticalLayout_18.addWidget(self.installationDate)


        self.horizontalLayout_15.addLayout(self.verticalLayout_18)


        self.gridLayout_59.addWidget(self.AboutSection, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.frame_55, 1, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_19, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_18)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 141))
        self.label_4.setStyleSheet(u"color: #fff;")

        self.gridLayout_26.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.frame_18, 0, 0, 1, 1)

        self.stackedSettings.addWidget(self.settingsHome)
        self.databaseConnection = QWidget()
        self.databaseConnection.setObjectName(u"databaseConnection")
        self.stackedSettings.addWidget(self.databaseConnection)
        self.dataSynchronization = QWidget()
        self.dataSynchronization.setObjectName(u"dataSynchronization")
        self.stackedSettings.addWidget(self.dataSynchronization)
        self.dateAndTimeFormats = QWidget()
        self.dateAndTimeFormats.setObjectName(u"dateAndTimeFormats")
        self.stackedSettings.addWidget(self.dateAndTimeFormats)
        self.updates = QWidget()
        self.updates.setObjectName(u"updates")
        self.stackedSettings.addWidget(self.updates)

        self.gridLayout_24.addWidget(self.stackedSettings, 0, 0, 1, 1)

        self.stackedWidgetMainContent.addWidget(self.settingsPage)

        self.verticalLayout_3.addWidget(self.stackedWidgetMainContent)


        self.gridLayout_4.addWidget(self.mainContent, 0, 2, 1, 1)

        self.fullSideBar = QWidget(self.mainPage)
        self.fullSideBar.setObjectName(u"fullSideBar")
        self.fullSideBar.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	padding: 10px;\n"
"	font-size: 15px;\n"
"	color: #fff;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	border: 1px solid #e6e6e6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background: #e6e6e6;\n"
"	color: #262626;\n"
"}\n"
"\n"
"#fullSideBar, *{\n"
"	background-color:  #7474a4;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.fullSideBar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_2 = QWidget(self.fullSideBar)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(200, 0))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setStyleSheet(u"color: #fff;")

        self.verticalLayout_2.addWidget(self.label_5)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy5)
        self.pushButton.setStyleSheet(u"border: none;\n"
"background: none;\n"
"padding: 5px;\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/settings_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QSize(70, 70))

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_5 = QPushButton(self.fullSideBar)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.fullSideBar)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_2 = QPushButton(self.fullSideBar)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_6.addWidget(self.pushButton_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.closeSideBar = QPushButton(self.fullSideBar)
        self.closeSideBar.setObjectName(u"closeSideBar")
        self.closeSideBar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeSideBar.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeSideBar.setIcon(icon13)
        self.closeSideBar.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.closeSideBar)

        self.verticalSpacer_7 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)


        self.gridLayout_4.addWidget(self.fullSideBar, 0, 1, 1, 1)

        self.iconOnlySideBar = QWidget(self.mainPage)
        self.iconOnlySideBar.setObjectName(u"iconOnlySideBar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.iconOnlySideBar.sizePolicy().hasHeightForWidth())
        self.iconOnlySideBar.setSizePolicy(sizePolicy6)
        self.iconOnlySideBar.setMinimumSize(QSize(250, 0))
        self.iconOnlySideBar.setMaximumSize(QSize(101, 16777215))
        self.iconOnlySideBar.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	padding: 10px;\n"
"	font-size: 15px;\n"
"	color: #fff;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background: #7474a4;\n"
"	border-left: 2px solid #003380;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #7474a4;\n"
"	border-left: 2px solid #003380;\n"
"}\n"
"\n"
"#iconOnlySideBar{\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.iconOnlySideBar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logoContainer = QFrame(self.iconOnlySideBar)
        self.logoContainer.setObjectName(u"logoContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.logoContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(35, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.logoContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(20, 20))
        self.label_3.setStyleSheet(u"padding: 10px;\n"
"border-radius: 10px;")
        self.label_3.setPixmap(QPixmap(u":/images/images/images/cow-2-256.ico"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(35, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addWidget(self.logoContainer)

        self.verticalSpacer_4 = QSpacerItem(30, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.homeBtn = QPushButton(self.iconOnlySideBar)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(40, 0))
        self.homeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/home_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon14)
        self.homeBtn.setIconSize(QSize(25, 25))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setChecked(True)
        self.homeBtn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.cattleHealthBtn = QPushButton(self.iconOnlySideBar)
        self.cattleHealthBtn.setObjectName(u"cattleHealthBtn")
        self.cattleHealthBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/health_and_safety_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cattleHealthBtn.setIcon(icon15)
        self.cattleHealthBtn.setIconSize(QSize(25, 25))
        self.cattleHealthBtn.setCheckable(True)
        self.cattleHealthBtn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.cattleHealthBtn)

        self.manageBreedingBtn = QPushButton(self.iconOnlySideBar)
        self.manageBreedingBtn.setObjectName(u"manageBreedingBtn")
        self.manageBreedingBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/icons8-livestock-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.manageBreedingBtn.setIcon(icon16)
        self.manageBreedingBtn.setIconSize(QSize(25, 25))
        self.manageBreedingBtn.setCheckable(True)
        self.manageBreedingBtn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.manageBreedingBtn)

        self.manageFinancialsBtn = QPushButton(self.iconOnlySideBar)
        self.manageFinancialsBtn.setObjectName(u"manageFinancialsBtn")
        self.manageFinancialsBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/finance_mode_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.manageFinancialsBtn.setIcon(icon17)
        self.manageFinancialsBtn.setIconSize(QSize(25, 25))
        self.manageFinancialsBtn.setCheckable(True)
        self.manageFinancialsBtn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.manageFinancialsBtn)

        self.manageInventoryBtn = QPushButton(self.iconOnlySideBar)
        self.manageInventoryBtn.setObjectName(u"manageInventoryBtn")
        self.manageInventoryBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/icons/images/icons/inventory_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.manageInventoryBtn.setIcon(icon18)
        self.manageInventoryBtn.setIconSize(QSize(25, 25))
        self.manageInventoryBtn.setCheckable(True)
        self.manageInventoryBtn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.manageInventoryBtn)

        self.addAnimalBtn = QPushButton(self.iconOnlySideBar)
        self.addAnimalBtn.setObjectName(u"addAnimalBtn")
        self.addAnimalBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addAnimalBtn.setIcon(icon19)
        self.addAnimalBtn.setIconSize(QSize(25, 25))
        self.addAnimalBtn.setCheckable(True)
        self.addAnimalBtn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.addAnimalBtn)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.pushButton_19 = QPushButton(self.iconOnlySideBar)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setIcon(icon12)
        self.pushButton_19.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.pushButton_19)

        self.logOutBtn = QPushButton(self.iconOnlySideBar)
        self.logOutBtn.setObjectName(u"logOutBtn")
        self.logOutBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logOutBtn.setStyleSheet(u"QPushButton:hover{\n"
"	background: #ff6666;\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/icons/images/icons/cil-user-unfollow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logOutBtn.setIcon(icon20)
        self.logOutBtn.setIconSize(QSize(25, 25))
        self.logOutBtn.setCheckable(False)

        self.verticalLayout_7.addWidget(self.logOutBtn)

        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)


        self.gridLayout_4.addWidget(self.iconOnlySideBar, 0, 0, 1, 1)

        self.mainFrame.addWidget(self.mainPage)

        self.gridLayout_3.addWidget(self.mainFrame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.verticalLayout_20.addLayout(self.gridLayout)

        self.versiontext = QFrame(self.styleSheet)
        self.versiontext.setObjectName(u"versiontext")
        self.versiontext.setStyleSheet(u"background: #18123b;\n"
"border-radius: 5px 5px 0px 0px;\n"
"")
        self.versiontext.setFrameShape(QFrame.StyledPanel)
        self.versiontext.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.versiontext)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.versiontext)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #cac4ed;")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_20.addWidget(self.versiontext)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.mainFrame.setCurrentIndex(0)
        self.uathenticationStack.setCurrentIndex(0)
        self.stackedWidgetMainContent.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tableContainer.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedSettings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Simbanai Brahmans Cattle Farming suite", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn_3.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn_3.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn_3.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn_3.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn_3.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn_3.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn_3.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn_3.setText("")
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.logInButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.passwordLabel_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.farmIdLabel_2.setText(QCoreApplication.translate("MainWindow", u"Farm-Id", None))
        self.logInError.setText("")
        self.TitleLogin.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:38pt;\">Log In</span></p></body></html>", None))
        self.RegistrationTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:38pt;\">Register farm account</span></p></body></html>", None))
        self.lastNameLabel_2.setText(QCoreApplication.translate("MainWindow", u"last name(disabled)", None))
        self.farmIdRegisterLabel_2.setText(QCoreApplication.translate("MainWindow", u"Farm Id", None))
        self.firstNameLabel_2.setText(QCoreApplication.translate("MainWindow", u"first name(disabled)", None))
        self.passwordLabel_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.passwordLabelConfirm_2.setText(QCoreApplication.translate("MainWindow", u"Password confirmation", None))
        self.showPasswordChkBox.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.registrationErr.setText("")
        self.backToLogInBtn.setText(QCoreApplication.translate("MainWindow", u"Back to logIn", None))
        self.registerAccountButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.informationBox_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">To register for a farm account you must have a farm Id issued to you by the admin.</p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:48pt; color:#ffffff;\">Home</span></p><p align=\"right\"><span style=\" font-size:7pt; color:#ffffff;\">Simbanai brahmans.</span></p></body></html>", None))
        self.dateDisplay.setText(QCoreApplication.translate("MainWindow", u"23 jan 2025", None))
        self.dateTitle.setText("")
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"Finish sales report", None))
        self.label_51.setText("")
        self.task_1.setText(QCoreApplication.translate("MainWindow", u"1:00\u20132:00pm", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"Weekly All Hands", None))
        self.label_53.setText("")
        self.task_2.setText(QCoreApplication.translate("MainWindow", u"2:00\u20132:30pm", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"Out of office", None))
        self.label_55.setText("")
        self.task_3.setText(QCoreApplication.translate("MainWindow", u"2:30\u20134:30pm", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"Add new task...", None))
        self.label_57.setText("")
        self.task_4.setText(QCoreApplication.translate("MainWindow", u"4:30\u20135:30pm", None))
        self.wellComeTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; color:#c6c8b4;\">Notifications Panel</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Manage Animal Health</span></p></body></html>", None))
        self.searchBarHealthHist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Keyword(tag id, disease)...", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic; color:#d9f9ff;\">Track health history </span></p></body></html>", None))
        self.export_as_excel_1.setText(QCoreApplication.translate("MainWindow", u"Export data as Excel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#6bc8c2;\">Ooops Search Results not found</span></p></body></html>", None))
        self.label_43.setText("")
        self.dataViewOptionsHealthComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Health history", None))
        self.dataViewOptionsHealthComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Vaccination history", None))

        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline; color:#aaffff;\">Choose which data to view</span></p></body></html>", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.healthRecords), QCoreApplication.translate("MainWindow", u"Health Records", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Checkup Purpose</span></p></body></html>", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Date and time</span></p></body></html>", None))
        self.checkUpPurpose.setItemText(0, QCoreApplication.translate("MainWindow", u"vaccinations", None))
        self.checkUpPurpose.setItemText(1, QCoreApplication.translate("MainWindow", u"treatment", None))
        self.checkUpPurpose.setItemText(2, QCoreApplication.translate("MainWindow", u"regular check-up", None))

        self.checkUpDate.setSpecialValueText("")
        self.popupCalendar.setText("")
        self.btnSetAppointment.setText(QCoreApplication.translate("MainWindow", u"Set reiminder", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Vet / Organization</span></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic; color:#deeaff;\">Set reminders for upcoming health checks</span></p></body></html>", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.notificationsPanel), QCoreApplication.translate("MainWindow", u"Schedule vet appointment", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Monitor herd health trends", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Export data as Excel", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.diseaseTracking), QCoreApplication.translate("MainWindow", u"Disease Tracking", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Breeding And Reproduction Management Dashboard</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Track each animal\u2019s reproductive status, heat cycles, insemination dates, and estimated due dates.", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Export data as excel spread sheet", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Add breeding data", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"view data as table", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.breedingTracking), QCoreApplication.translate("MainWindow", u"Track Breeding Cycles", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Post-Natal </span></p><p align=\"center\"><span style=\" font-size:18pt;\">Care</span></p></body></html>", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"check", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Birthing</span></p><p align=\"center\"><span style=\" font-size:18pt;\"> Details</span></p></body></html>", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"check", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"check", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Pre-Natal</span></p><p><span style=\" font-size:18pt;\">Care</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Animal</span></p><p align=\"center\"><span style=\" font-size:18pt;\">information</span></p></body></html>", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#7ec8b9;\">Monitor livestock pragnancy status</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.pregnancyMonitoring), QCoreApplication.translate("MainWindow", u"Pregnancy Monitoring", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Set reiminder", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Notes</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Breeding Event</p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">date and time</p></body></html>", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"insemination timing", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"pregnancy check-up", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"expected delivery dates", None))

        self.dateTimeEdit_2.setSpecialValueText("")
        self.popupCalendar_2.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Set reminders for upcoming breeding events", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.notificationsBreeding), QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.geneticTracking), QCoreApplication.translate("MainWindow", u"Genetic Tracking", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Financial Tracking</span></p></body></html>", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.profitAnalysis), QCoreApplication.translate("MainWindow", u"Profit Analysis", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.trackFarmExpenses), QCoreApplication.translate("MainWindow", u"Track Farm Expenses", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.reportsAndAnalytics), QCoreApplication.translate("MainWindow", u"Reports and Analytics", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Inventory and Resource Management</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Manage feed, supplies and medicines", None))
        self.addInventoryBtn.setText(QCoreApplication.translate("MainWindow", u"Add Inventory", None))
        self.exportExcelBtn.setText(QCoreApplication.translate("MainWindow", u"Export data as Excel", None))
        self.searchInventoryBtn.setText(QCoreApplication.translate("MainWindow", u"Search inventory", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"item name", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"type", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"stock", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"modify", None));
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Fillter by", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"type", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.feedAndSupplies), QCoreApplication.translate("MainWindow", u"Feed and Supplies ", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Manage Farm medications", None))
        self.addMedicationBtn.setText(QCoreApplication.translate("MainWindow", u"Add medication", None))
        self.exportExcelMedicationBtn.setText(QCoreApplication.translate("MainWindow", u"Export data as Excel", None))
        self.searchMedicationBtn.setText(QCoreApplication.translate("MainWindow", u"Seach medication", None))
        ___qtablewidgetitem4 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Medication Name", None));
        ___qtablewidgetitem5 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Dosage", None));
        ___qtablewidgetitem6 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Frequency", None));
        ___qtablewidgetitem7 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Expiration Date", None));
        ___qtablewidgetitem8 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Comments", None));
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Filter By", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"medication name", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"expiration date", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.medicationRecords), QCoreApplication.translate("MainWindow", u"Medication Records", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Manage resource allocation", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Add resource", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Export logs as excel", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        ___qtablewidgetitem9 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Resource Type", None));
        ___qtablewidgetitem10 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Quantity used", None));
        ___qtablewidgetitem11 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"cost", None));
        ___qtablewidgetitem12 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem13 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"location", None));
        ___qtablewidgetitem14 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"comments", None));
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Filter by", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"resource type", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"location", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"cost", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.resourceAllocation), QCoreApplication.translate("MainWindow", u"Resource Allocation", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">ANIMAL PROFILE</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Enter new Animal details</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tag Id", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Animal Breed", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Age(in months)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Weight(KG)", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.departmentInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Dairy Production", None))
        self.departmentInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Breeding", None))
        self.departmentInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Meat Production", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.sexInput.setItemText(0, QCoreApplication.translate("MainWindow", u"male", None))
        self.sexInput.setItemText(1, QCoreApplication.translate("MainWindow", u"female", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Unique Characteristics", None))
        self.submitAnimalDataBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.errLabelAnimalDetails.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addAnimal1), QCoreApplication.translate("MainWindow", u"Add Animal", None))
        self.filter_tagId.setText(QCoreApplication.translate("MainWindow", u"Tag id", None))
        self.filter_animalBreed.setText(QCoreApplication.translate("MainWindow", u"animal breed", None))
        self.activateCategoryAndSexFilters.setText(QCoreApplication.translate("MainWindow", u"animal sex or department", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#89ff57;\">filter by the animal sex</span></p></body></html>", None))
        self.sexFilterInput.setItemText(0, QCoreApplication.translate("MainWindow", u"male", None))
        self.sexFilterInput.setItemText(1, QCoreApplication.translate("MainWindow", u"female", None))

        self.departmentFilterCategory.setItemText(0, QCoreApplication.translate("MainWindow", u"Dairy Production", None))
        self.departmentFilterCategory.setItemText(1, QCoreApplication.translate("MainWindow", u"Meat Production", None))
        self.departmentFilterCategory.setItemText(2, QCoreApplication.translate("MainWindow", u"Breeding", None))

        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#89ff57;\">filter by department</span></p></body></html>", None))
        self.animalSexcheckBox.setText("")
        self.departmentCheckBox.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Filter By", None))
        self.searchBar.setText("")
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search...", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Search cattle", None))
        self.checkBoxAllFilters.setText(QCoreApplication.translate("MainWindow", u"turn off filters", None))
        self.checkBoxHideFilters.setText(QCoreApplication.translate("MainWindow", u"hide filters", None))
        ___qtablewidgetitem15 = self.animalResultsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Tag Id", None));
        ___qtablewidgetitem16 = self.animalResultsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"breed", None));
        ___qtablewidgetitem17 = self.animalResultsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"age in months", None));
        ___qtablewidgetitem18 = self.animalResultsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"weight in kg", None));
        ___qtablewidgetitem19 = self.animalResultsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"sex", None));
        ___qtablewidgetitem20 = self.animalResultsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"unique characteristics", None));
        ___qtablewidgetitem21 = self.animalResultsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"department", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewAnimalData), QCoreApplication.translate("MainWindow", u"View / Search and Edit Animal Data", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Windows Version", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Last Updated", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Installed On", None))
        self.deviceName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.softwareVersion.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lastUpdateDate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.installationDate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:24pt;\">Settings Panel</span></p><p align=\"right\"><span style=\" font-size:9pt;\">About section.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Settings</span></p></body></html>", None))
        self.pushButton.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Data Synchronization", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Date and Time formats", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Updates", None))
        self.closeSideBar.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.label_3.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home ", None))
        self.cattleHealthBtn.setText(QCoreApplication.translate("MainWindow", u"manage cattle health", None))
        self.manageBreedingBtn.setText(QCoreApplication.translate("MainWindow", u"manage breeding", None))
        self.manageFinancialsBtn.setText(QCoreApplication.translate("MainWindow", u"manage financials", None))
        self.manageInventoryBtn.setText(QCoreApplication.translate("MainWindow", u"manage inventory", None))
        self.addAnimalBtn.setText(QCoreApplication.translate("MainWindow", u"add animal          ", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.logOutBtn.setText(QCoreApplication.translate("MainWindow", u"   Log Out", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">VERSION: 1.0.0</span></p></body></html>", None))
    # retranslateUi

