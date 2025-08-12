# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_animal.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_DialogCustom(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(651, 400)
        Dialog.setMinimumSize(QSize(651, 400))
        Dialog.setMaximumSize(QSize(651, 400))
        Dialog.setStyleSheet(u"*{\n"
"background:rgb(58, 58, 89);\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton{\n"
"background: #2c2c2c;\n"
"color: #fff;\n"
"font-family: sans;\n"
"font-size: 15px;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #eee;\n"
"color: #2c2c2c;\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainContainer = QFrame(Dialog)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setStyleSheet(u"#mainContainer{\n"
"	border-radius: 6px;\n"
"}")
        self.mainContainer.setFrameShape(QFrame.StyledPanel)
        self.mainContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.mainContainer)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.mainContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(411, 271))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(381, 231))
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.ageInMonths = QDoubleSpinBox(self.frame)
        self.ageInMonths.setObjectName(u"ageInMonths")
        self.ageInMonths.setEnabled(False)
        self.ageInMonths.setMaximum(1000.990000000000009)
        self.ageInMonths.setSingleStep(0.500000000000000)

        self.gridLayout_3.addWidget(self.ageInMonths, 3, 0, 1, 1)

        self.animalWeight = QDoubleSpinBox(self.frame)
        self.animalWeight.setObjectName(u"animalWeight")
        self.animalWeight.setEnabled(False)
        self.animalWeight.setMaximum(1000.990000000000009)
        self.animalWeight.setSingleStep(0.500000000000000)

        self.gridLayout_3.addWidget(self.animalWeight, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.sexComboBox = QComboBox(self.frame)
        self.sexComboBox.addItem("")
        self.sexComboBox.addItem("")
        self.sexComboBox.setObjectName(u"sexComboBox")
        self.sexComboBox.setEnabled(False)

        self.gridLayout_4.addWidget(self.sexComboBox, 3, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.departmentComboBox = QComboBox(self.frame)
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.setObjectName(u"departmentComboBox")
        self.departmentComboBox.setEnabled(False)

        self.gridLayout_4.addWidget(self.departmentComboBox, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_5)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)

        self.verticalLayout_3.addWidget(self.label_5)

        self.lineEditBreed = QLineEdit(self.frame)
        self.lineEditBreed.setObjectName(u"lineEditBreed")
        self.lineEditBreed.setEnabled(False)

        self.verticalLayout_3.addWidget(self.lineEditBreed)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.gridLayout_7.addWidget(self.frame, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.frame_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMinimumSize(QSize(289, 0))
        self.buttonBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonBox.setStyleSheet(u"width: 70px;\n"
"height: 30px;")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout_7.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.animalUpdateTitle = QLabel(self.frame_2)
        self.animalUpdateTitle.setObjectName(u"animalUpdateTitle")

        self.gridLayout_7.addWidget(self.animalUpdateTitle, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.mainContainer)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(191, 321))
        self.groupBox.setStyleSheet(u"\n"
"QGroupBox{\n"
"border: 2px solid rgb(173, 255, 129);\n"
"border-radius: 8px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame1 = QFrame(self.groupBox)
        self.frame1.setObjectName(u"frame1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setMinimumSize(QSize(0, 300))
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_6 = QCheckBox(self.frame1)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout.addWidget(self.checkBox_6)

        self.line = QFrame(self.frame1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.checkBox_2 = QCheckBox(self.frame1)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.line_2 = QFrame(self.frame1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.checkBox_5 = QCheckBox(self.frame1)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.line_3 = QFrame(self.frame1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.checkBox = QCheckBox(self.frame1)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.line_4 = QFrame(self.frame1)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.checkBox_3 = QCheckBox(self.frame1)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.line_5 = QFrame(self.frame1)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.checkBox_4 = QCheckBox(self.frame1)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout.addWidget(self.checkBox_4)


        self.gridLayout_2.addWidget(self.frame1, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.mainContainer, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.checkBox_6.toggled.connect(self.departmentComboBox.setEnabled)
        self.checkBox_5.toggled.connect(self.sexComboBox.setEnabled)
        self.checkBox.toggled.connect(self.animalWeight.setEnabled)
        self.checkBox_3.toggled.connect(self.ageInMonths.setEnabled)
        self.checkBox_4.toggled.connect(self.lineEditBreed.setEnabled)
        self.checkBox_2.toggled.connect(self.textEdit.setEnabled)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Weight in kg", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Age In months", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Department", None))
        self.sexComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"male", None))
        self.sexComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"female", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Sex", None))
        self.departmentComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Dairy Production", None))
        self.departmentComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Breeding", None))
        self.departmentComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Meat Production", None))

        self.label_5.setText(QCoreApplication.translate("Dialog", u"Breed", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Unique Characteristics", None))
        self.animalUpdateTitle.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#8dc84a;\">Update Data for animal</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Select the columns to edit", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"department", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"unique characteristics", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"sex", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"weight", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"age", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"breed", None))
    # retranslateUi

