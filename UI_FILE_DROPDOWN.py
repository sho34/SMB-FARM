# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dropdown.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(755, 413)
        Dialog.setStyleSheet(u"/* Common styles for various widgets \n"
"  #################################################### */\n"
"QDialog, QCalendarWidget, QCalendarWidget QWidget, QListWidget {\n"
"	background-color: #ffffbf;\n"
"}\n"
"\n"
"QPushButton {\n"
"    min-width: 30px;\n"
"    padding: 10px 25px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    margin-bottom: 5px;\n"
"}\n"
"\n"
"QDialog {\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QListWidge t{\n"
"	border: none;\n"
"	min-width: 80px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	padding: 10px 25px;\n"
"	border-radius: 5px;\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	margin-bottom: 5px;\n"
"}\n"
"\n"
"/* Hover and selection styles \n"
"  #################################################### */\n"
"QListWidget::item:hover {\n"
"    background-color: #b2d5ff;\n"
"	color: #000;\n"
"}\n"
"\n"
"QPushButton:checked, QListWidget::item:selected {\n"
"    background-color: #0075ff;\n"
"	color: #fff;\n"
"}\n"
"\n"
"/* style for top navigation area \n"
""
                        "  #################################################### */ \n"
"#qt_calendar_navigationbar {\n"
"	border-bottom: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* style for month change buttons \n"
"  #################################################### */\n"
"#qt_calendar_prevmonth, #qt_calendar_nextmonth {\n"
"	/* border delete */\n"
"    border: none;  \n"
"    /* delete default icons */\n"
"	qproperty-icon: none; \n"
"    min-width: 25px;\n"
"    max-width: 25px;\n"
"    min-height: 25px;\n"
"    max-height: 25px;\n"
"    border-radius: 5px; \n"
"	/* set background transparent */\n"
"    background-color: transparent; \n"
"	padding: 5px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {\n"
"    background-color: #b2d5ff;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {\n"
"    background-color: #0075ff;\n"
"}\n"
"\n"
"/* style for pre month button \n"
"  #################################################### */\n"
""
                        "#qt_calendar_prevmonth {\n"
"	/* set text for button */\n"
"	/*qproperty-text: \">\";*/\n"
"	margin-left:5px;\n"
"	image:url(:/icons/images/arrow_up.svg);\n"
"}\n"
"\n"
"/* style for next month button \n"
"  #################################################### */\n"
"#qt_calendar_nextmonth {\n"
"	margin-right:5px;\n"
"	image: url(:/icons/images/arrow_down.svg);\n"
"    /* qproperty-text: \">\"; */\n"
"}\n"
"\n"
"\n"
"/* Style for month and yeat buttons #################################### */\n"
"\n"
"#qt_calendar_yearbutton {\n"
"    color: #000;\n"
"	margin:5px;\n"
"    border-radius: 5px;\n"
"	font-size: 16px;\n"
"	padding:5px 15px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"	width: 110px;\n"
"    color: #000;\n"
"	margin:5px 0px;\n"
"    border-radius: 5px;\n"
"	padding:5px 0;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_monthbutton:hover {\n"
"    background-color: #b2d5ff;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
""
                        "    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/* Style for year input lineEdit \n"
"  #################################################### */\n"
"#qt_calendar_yearedit {\n"
"    min-width: 100px;\n"
"    color: #000;\n"
"	font-size: 16px;\n"
"   margin:5px;\n"
"	padding: 0 5px;\n"
"}\n"
"\n"
"/* Style for year change buttons \n"
"  #################################################### */\n"
"#qt_calendar_yearedit::up-button { \n"
"	image:url(:/icons/images/arrow-151-48.ico);\n"
"    subcontrol-position: right;\n"
"	height: 30px;\n"
"	width: 30px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button { \n"
"	image:url(:/icons/images/arrow-213-48.ico);\n"
"    subcontrol-position: left; \n"
"	height: 30px;\n"
"	width: 30px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
"#qt_calendar_yearedit::up-button {\n"
"	width:10px;\n"
"	padding: 0px 5px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button:hover, \n"
"#qt_calendar_yearedit::up-button:hover {\n"
"	background-co"
                        "lor: #55aaff;\n"
"}\n"
"\n"
"/* Style for month select menu \n"
"  #################################################### */\n"
"#calendarWidget QToolButton QMenu {\n"
"     background-color: #fff;\n"
"	border: 1px solid #f3f3f3;\n"
"\n"
"}\n"
"#calendarWidget QToolButton QMenu::item {\n"
"	padding: 5px 20px;\n"
"	font-size: 14px;\n"
"}\n"
" #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidget QToolButton::menu-indicator {\n"
"	/* Remove toolButton arrow */\n"
"      /*image: none; */\n"
"	nosubcontrol-origin: margin;\n"
"	subcontrol-position: right center;\n"
"	margin-top: 10px;\n"
"	width:20px;\n"
"}\n"
"\n"
"/* Style for calendar table \n"
"  #################################################### */\n"
"#qt_calendar_calendarview {\n"
"	/* Remove the selected dashed box */\n"
"    outline: 0px;\n"
"	border-top: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item {\n"
""
                        "	 border-radius:5px;\n"
"	margin: 1px;	\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"	background-color:#b2d5ff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected {\n"
"    background-color: #0075ff; \n"
"	color: #fff;\n"
"}\n"
"\n"
"#clear_btn,\n"
"#now_btn {\n"
"	color: #0078d8;\n"
"	padding: 10px 15px;\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, 15)
        self.calendarWidget = QCalendarWidget(Dialog)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMinimumSize(QSize(335, 0))
        self.calendarWidget.setMaximumSize(QSize(370, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setFocusPolicy(Qt.NoFocus)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)

        self.verticalLayout.addWidget(self.calendarWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.clear_btn = QPushButton(Dialog)
        self.clear_btn.setObjectName(u"clear_btn")
        font1 = QFont()
        font1.setBold(True)
        self.clear_btn.setFont(font1)
        self.clear_btn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.clear_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.now_btn = QPushButton(Dialog)
        self.now_btn.setObjectName(u"now_btn")
        self.now_btn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.now_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 15, -1, 25)
        self.listWidget_2 = QListWidget(Dialog)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem9 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem10 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem11 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem12 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem13 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem14 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem15 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem16 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem17 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem18 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem19 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem20 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem21 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem22 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem23 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem24 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem25 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem26 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem27 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem28 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem29 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem30 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem31 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem32 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem33 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem34 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem35 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem36 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem37 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem37.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem38 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem38.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem39 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem39.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem40 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem40.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem41 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem41.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem42 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem42.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem43 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem43.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem44 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem44.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem45 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem45.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem46 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem46.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem47 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem47.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem48 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem48.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem49 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem49.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem50 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem50.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem51 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem51.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem52 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem52.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem53 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem53.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem54 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem54.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem55 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem55.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem56 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem56.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem57 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem57.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem58 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem58.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem59 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMinimumSize(QSize(0, 0))
        self.listWidget_2.setMaximumSize(QSize(80, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.listWidget_2.setFont(font2)
        self.listWidget_2.setFocusPolicy(Qt.NoFocus)
        self.listWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_2.addWidget(self.listWidget_2, 0, 1, 1, 1)

        self.listWidget = QListWidget(Dialog)
        __qlistwidgetitem60 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem60.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem61 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem61.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem62 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem62.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem63 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem63.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem64 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem64.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem65 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem65.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem66 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem66.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem67 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem67.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem68 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem68.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem69 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem69.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem70 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem70.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem71 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(80, 16777215))
        self.listWidget.setFont(font2)
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setAutoScroll(True)

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(80, 20))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 15)
        self.pm_btn = QPushButton(Dialog)
        self.pm_btn.setObjectName(u"pm_btn")
        self.pm_btn.setFocusPolicy(Qt.NoFocus)
        self.pm_btn.setCheckable(True)
        self.pm_btn.setChecked(True)

        self.verticalLayout_2.addWidget(self.pm_btn)

        self.am_btn = QPushButton(Dialog)
        self.am_btn.setObjectName(u"am_btn")
        self.am_btn.setFocusPolicy(Qt.NoFocus)
        self.am_btn.setCheckable(True)

        self.verticalLayout_2.addWidget(self.am_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.clear_btn.setText(QCoreApplication.translate("Dialog", u"Clear", None))
        self.now_btn.setText(QCoreApplication.translate("Dialog", u"Now", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"00", None));
        ___qlistwidgetitem1 = self.listWidget_2.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"01", None));
        ___qlistwidgetitem2 = self.listWidget_2.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"02", None));
        ___qlistwidgetitem3 = self.listWidget_2.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"03", None));
        ___qlistwidgetitem4 = self.listWidget_2.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"04", None));
        ___qlistwidgetitem5 = self.listWidget_2.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Dialog", u"05", None));
        ___qlistwidgetitem6 = self.listWidget_2.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Dialog", u"06", None));
        ___qlistwidgetitem7 = self.listWidget_2.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Dialog", u"07", None));
        ___qlistwidgetitem8 = self.listWidget_2.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Dialog", u"08", None));
        ___qlistwidgetitem9 = self.listWidget_2.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Dialog", u"09", None));
        ___qlistwidgetitem10 = self.listWidget_2.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Dialog", u"10", None));
        ___qlistwidgetitem11 = self.listWidget_2.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Dialog", u"11", None));
        ___qlistwidgetitem12 = self.listWidget_2.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Dialog", u"12", None));
        ___qlistwidgetitem13 = self.listWidget_2.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Dialog", u"13", None));
        ___qlistwidgetitem14 = self.listWidget_2.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Dialog", u"14", None));
        ___qlistwidgetitem15 = self.listWidget_2.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Dialog", u"15", None));
        ___qlistwidgetitem16 = self.listWidget_2.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Dialog", u"16", None));
        ___qlistwidgetitem17 = self.listWidget_2.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Dialog", u"17", None));
        ___qlistwidgetitem18 = self.listWidget_2.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Dialog", u"18", None));
        ___qlistwidgetitem19 = self.listWidget_2.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Dialog", u"19", None));
        ___qlistwidgetitem20 = self.listWidget_2.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Dialog", u"20", None));
        ___qlistwidgetitem21 = self.listWidget_2.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Dialog", u"21", None));
        ___qlistwidgetitem22 = self.listWidget_2.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Dialog", u"22", None));
        ___qlistwidgetitem23 = self.listWidget_2.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Dialog", u"23", None));
        ___qlistwidgetitem24 = self.listWidget_2.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Dialog", u"24", None));
        ___qlistwidgetitem25 = self.listWidget_2.item(25)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("Dialog", u"25", None));
        ___qlistwidgetitem26 = self.listWidget_2.item(26)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("Dialog", u"25", None));
        ___qlistwidgetitem27 = self.listWidget_2.item(27)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("Dialog", u"27", None));
        ___qlistwidgetitem28 = self.listWidget_2.item(28)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("Dialog", u"28", None));
        ___qlistwidgetitem29 = self.listWidget_2.item(29)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("Dialog", u"29", None));
        ___qlistwidgetitem30 = self.listWidget_2.item(30)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("Dialog", u"30", None));
        ___qlistwidgetitem31 = self.listWidget_2.item(31)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("Dialog", u"31", None));
        ___qlistwidgetitem32 = self.listWidget_2.item(32)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("Dialog", u"32", None));
        ___qlistwidgetitem33 = self.listWidget_2.item(33)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("Dialog", u"33", None));
        ___qlistwidgetitem34 = self.listWidget_2.item(34)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("Dialog", u"34", None));
        ___qlistwidgetitem35 = self.listWidget_2.item(35)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("Dialog", u"35", None));
        ___qlistwidgetitem36 = self.listWidget_2.item(36)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("Dialog", u"36", None));
        ___qlistwidgetitem37 = self.listWidget_2.item(37)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("Dialog", u"37", None));
        ___qlistwidgetitem38 = self.listWidget_2.item(38)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("Dialog", u"38", None));
        ___qlistwidgetitem39 = self.listWidget_2.item(39)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("Dialog", u"39", None));
        ___qlistwidgetitem40 = self.listWidget_2.item(40)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("Dialog", u"40", None));
        ___qlistwidgetitem41 = self.listWidget_2.item(41)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("Dialog", u"41", None));
        ___qlistwidgetitem42 = self.listWidget_2.item(42)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("Dialog", u"42", None));
        ___qlistwidgetitem43 = self.listWidget_2.item(43)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("Dialog", u"43", None));
        ___qlistwidgetitem44 = self.listWidget_2.item(44)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("Dialog", u"44", None));
        ___qlistwidgetitem45 = self.listWidget_2.item(45)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("Dialog", u"45", None));
        ___qlistwidgetitem46 = self.listWidget_2.item(46)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("Dialog", u"46", None));
        ___qlistwidgetitem47 = self.listWidget_2.item(47)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("Dialog", u"47", None));
        ___qlistwidgetitem48 = self.listWidget_2.item(48)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("Dialog", u"48", None));
        ___qlistwidgetitem49 = self.listWidget_2.item(49)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("Dialog", u"49", None));
        ___qlistwidgetitem50 = self.listWidget_2.item(50)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("Dialog", u"50", None));
        ___qlistwidgetitem51 = self.listWidget_2.item(51)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("Dialog", u"51", None));
        ___qlistwidgetitem52 = self.listWidget_2.item(52)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("Dialog", u"52", None));
        ___qlistwidgetitem53 = self.listWidget_2.item(53)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("Dialog", u"53", None));
        ___qlistwidgetitem54 = self.listWidget_2.item(54)
        ___qlistwidgetitem54.setText(QCoreApplication.translate("Dialog", u"54", None));
        ___qlistwidgetitem55 = self.listWidget_2.item(55)
        ___qlistwidgetitem55.setText(QCoreApplication.translate("Dialog", u"55", None));
        ___qlistwidgetitem56 = self.listWidget_2.item(56)
        ___qlistwidgetitem56.setText(QCoreApplication.translate("Dialog", u"56", None));
        ___qlistwidgetitem57 = self.listWidget_2.item(57)
        ___qlistwidgetitem57.setText(QCoreApplication.translate("Dialog", u"57", None));
        ___qlistwidgetitem58 = self.listWidget_2.item(58)
        ___qlistwidgetitem58.setText(QCoreApplication.translate("Dialog", u"58", None));
        ___qlistwidgetitem59 = self.listWidget_2.item(59)
        ___qlistwidgetitem59.setText(QCoreApplication.translate("Dialog", u"59", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem60 = self.listWidget.item(0)
        ___qlistwidgetitem60.setText(QCoreApplication.translate("Dialog", u"01", None));
        ___qlistwidgetitem61 = self.listWidget.item(1)
        ___qlistwidgetitem61.setText(QCoreApplication.translate("Dialog", u"02", None));
        ___qlistwidgetitem62 = self.listWidget.item(2)
        ___qlistwidgetitem62.setText(QCoreApplication.translate("Dialog", u"03", None));
        ___qlistwidgetitem63 = self.listWidget.item(3)
        ___qlistwidgetitem63.setText(QCoreApplication.translate("Dialog", u"04", None));
        ___qlistwidgetitem64 = self.listWidget.item(4)
        ___qlistwidgetitem64.setText(QCoreApplication.translate("Dialog", u"05", None));
        ___qlistwidgetitem65 = self.listWidget.item(5)
        ___qlistwidgetitem65.setText(QCoreApplication.translate("Dialog", u"06", None));
        ___qlistwidgetitem66 = self.listWidget.item(6)
        ___qlistwidgetitem66.setText(QCoreApplication.translate("Dialog", u"07", None));
        ___qlistwidgetitem67 = self.listWidget.item(7)
        ___qlistwidgetitem67.setText(QCoreApplication.translate("Dialog", u"08", None));
        ___qlistwidgetitem68 = self.listWidget.item(8)
        ___qlistwidgetitem68.setText(QCoreApplication.translate("Dialog", u"09", None));
        ___qlistwidgetitem69 = self.listWidget.item(9)
        ___qlistwidgetitem69.setText(QCoreApplication.translate("Dialog", u"10", None));
        ___qlistwidgetitem70 = self.listWidget.item(10)
        ___qlistwidgetitem70.setText(QCoreApplication.translate("Dialog", u"11", None));
        ___qlistwidgetitem71 = self.listWidget.item(11)
        ___qlistwidgetitem71.setText(QCoreApplication.translate("Dialog", u"12", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

        self.label.setText(QCoreApplication.translate("Dialog", u"Hours", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"    Minutes", None))
        self.pm_btn.setText(QCoreApplication.translate("Dialog", u"PM", None))
        self.am_btn.setText(QCoreApplication.translate("Dialog", u"AM", None))
    # retranslateUi

