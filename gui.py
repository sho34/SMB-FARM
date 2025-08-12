# ......................................... CUSTOM UI FILE IMPORTS .........................................

from UI_FILE import Ui_MainWindow
from main_dropdown import Ui_Dialog
from UI_FILE_EDIT_ANIMAL import Ui_DialogCustom
from UI_FILE_SPLASH_SCREEN import Ui_SplashScreen

# ......................................... PYSIDE6 IMPORTS       ..........................................
import PySide6
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QColor, QFont, QFontDatabase, QCursor, QIcon, QKeyEvent
from PySide6.QtCore import QDate, QDateTime, QTime, QEvent, QPropertyAnimation, Signal, QCoreApplication
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QTableWidgetItem, QApplication, QMainWindow, QDialog, \
    QFileDialog

# windows API stuff
from ctypes.wintypes import MSG

# global variables, date-view and
from globals import *
from dtview import *
import platform
import security
from excel_exports import ExportExcelData
import database.random_id_generator as rnd

# import the connection class 
from database.connection import Connection
import datetime

import pandas as pd


# the calendar
class DropDown(QDialog):
    # Signal emitted when date and time are changed in the dropdown
    dateTimeChanged_str = Signal(str)

    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Ensure only one of the buttons can be checked at a time
        self.ui.pm_btn.setAutoExclusive(True)
        self.ui.am_btn.setAutoExclusive(True)

        # Set initial selection in the list widgets
        self.ui.listWidget.setCurrentRow(0)
        self.ui.listWidget_2.setCurrentRow(1)

        # Connect signals of UI elements to custom methods
        self.ui.calendarWidget.selectionChanged.connect(self.emit_signal)
        self.ui.listWidget.itemSelectionChanged.connect(self.emit_signal)
        self.ui.listWidget_2.itemSelectionChanged.connect(self.emit_signal)
        self.ui.pm_btn.clicked.connect(self.emit_signal)
        self.ui.am_btn.clicked.connect(self.emit_signal)

    def emit_signal(self):
        # Get selected date, time, and AM/PM from UI elements
        date = self.ui.calendarWidget.selectedDate()
        time_hour = self.ui.listWidget.currentItem().text()
        time_min = self.ui.listWidget_2.currentItem().text()

        # Determine if it's AM or PM
        pm_am_str = "PM" if self.ui.pm_btn.isChecked() else "AM"

        # Emit signal with formatted date and time
        self.dateTimeChanged_str.emit(f"{date.month()},{date.day()},{date.year()},{time_hour},{time_min},{pm_am_str}")


# the splash screen
class SplashScreen(QMainWindow):
    def __init__(self):
        global CUSTOM_TITLE_BAR
        super(SplashScreen, self).__init__()

        # load all the resources required by the app

        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)
        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.Description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.Description.setText("<strong>LOADING</strong> USER INTERFACE"))
        # initialize the database 

        self.connection = Connection()

        # SHOW THE MAIN WINDOW
        self.show()

    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        if counter > 100:
            # STOP TIMER 
            self.timer.stop()
            # SHOW MAIN WINDOW

            # if some file is no available and the flag is set to new install prompt the user to setup the local
            # database. self.db_menu = DatabaseLogin() self.db_menu.show()

            # if flag is set to old install but file is not available ask the user to restore or fix the issue

            # if file is available and flag is set to old install proceed to main window 

            if self.connection.error():
                print("connection success")
                self.main = MainWindow(self.connection)
                self.main.show()
                # CLOSE THE SPLASH SCREEN
                self.close()
            else:
                self.ui.loading.setText("failed to load application")
                QtCore.QTimer.singleShot(3000, lambda: self.ui.Description.setText(
                    "<strong>DATABASE CONNECTION</strong> FAILED"
                ))
                self.connection.error()

        counter += 1


# for the dialog box 
class DialogBoxDbEdit(QDialog):
    def __init__(self, animalTagId: str):
        super().__init__()

        self.ui = Ui_DialogCustom()
        self.ui.setupUi(self)

        self.tag_id = animalTagId

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setWindowTitle("Edit Animal infomation")
        self.ui.animalUpdateTitle.setText(
            QCoreApplication.translate(
                "Dialog",
                u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#8dc84a;\">" \
                "Update Data for animal"
                " [" + animalTagId + "]"
                                     "</span></p></body></html>",
                None
            )
        )
        # self.ui.animalUpdateTitle.setText(f"Update Data for animal {animalTagId}")
        self.ui.textEdit.setStyleSheet("color: #000")

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.mainContainer.setGraphicsEffect(self.shadow)

        # bind the buttons to signals.
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        # append the sql queries to the list self.queries
        self.queries = list()
        self.ui.departmentComboBox.currentTextChanged.connect(self.addDataDepartment)
        self.ui.checkBox_6.clicked.connect(
            self.addDataDepartment)  # when the user selects department but desires the current text entry
        self.ui.sexComboBox.currentTextChanged.connect(self.addDataAnimalSex)
        self.ui.checkBox_5.clicked.connect(
            self.addDataAnimalSex)  # when the user selects animal sex but desires the current text entry
        self.ui.animalWeight.editingFinished.connect(self.addDataAnimalWeight)
        self.ui.ageInMonths.editingFinished.connect(self.addDataAnimalAge)
        self.ui.checkBox_2.clicked.connect(self.addDataAnimalCharacteristics)
        self.ui.lineEditBreed.editingFinished.connect(self.addDataAnimalBreed)

    def addDataDepartment(self):
        global query_index_cache
        if self.ui.checkBox_6.isChecked():
            sql = (f""
                   f"UPDATE animal SET "
                   f"department='{self.ui.departmentComboBox.currentText()}' "
                   f"WHERE tag_id='{self.tag_id}'"
                   )
            self.queries.append(sql)
            query_index_cache = len(self.queries) - 1
        else:
            if len(self.queries) > 0:
                self.queries.pop(query_index_cache)
            # remove the item from the buffer.
            print("department unchecked")

    def addDataAnimalSex(self):
        if self.ui.checkBox_5.isChecked():
            sex = {"male": 1, "female": 0}
            sql = f"UPDATE animal SET sex={sex[self.ui.sexComboBox.currentText()]} WHERE tag_id='{self.tag_id}'"
            self.queries.append(sql)
            # print(sql)
        else:
            print("animal sex unchecked")

    def addDataAnimalWeight(self):
        if self.ui.checkBox.isChecked():
            sql = f"UPDATE animal SET weight_in_kg='{self.ui.animalWeight.value()}' WHERE tag_id='{self.tag_id}'"
            self.queries.append(sql)
            # print(sql)
        else:
            print("animal weight unchecked")

    def addDataAnimalAge(self):
        if self.ui.checkBox_3.isChecked():
            sql = f"UPDATE animal SET age_in_months='{self.ui.ageInMonths.value()}' WHERE tag_id='{self.tag_id}'"
            self.queries.append(sql)
            # print(sql)
        else:
            print("animal age unchecked")

    def addDataAnimalBreed(self):
        if self.ui.checkBox_4.isChecked():
            sql = f"UPDATE animal SET breed='{self.ui.lineEditBreed.text()}' WHERE tag_id='{self.tag_id}'"
            self.queries.append(sql)
            # print(sql)
        else:
            print("animal breed unchecked")

    def addDataAnimalCharacteristics(self):
        if self.ui.checkBox_2.isChecked():
            sql = f"UPDATE animal SET unique_characteristics='none' WHERE tag_id='{self.tag_id}'"
            self.queries.append(sql)
            # print(sql)
        else:
            print("animal characteristics unchecked")

    # def getLineData(self) -> str:
    #     return ""

    def getData(self) -> list:
        return self.queries

    def clearQueryBuffer(self):
        if len(self.queries) > 0:
            self.queries.clear()


# Table model to display data from the database.
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):

        if role == Qt.ItemDataRole.DisplayRole:
            # get the raw value
            value = self._data.iloc[index.row()][index.column()]

            # Perform per-type checks and render accordingly.
            if isinstance(value, datetime.date):
                # Render time to YYY-MM-DD
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                # Render float to 2dp
                return "%.2f" % value

            # Default (anything not captured above: e.g. int)
            return str(value)

        # Add icons for the calendar column.
        if role == Qt.ItemDataRole.DecorationRole:
            value = self._data.iloc[index.row()][index.column()]

            if isinstance(value, datetime.date):
                return QtGui.QIcon('images/icons-svg/calendar.svg')

        # change the color of the 4th column to blue.
        if role == Qt.ItemDataRole.BackgroundRole and index.column() == 4:
            return QtGui.QColor('#80ff80')

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row
        if role == Qt.ItemDataRole.DisplayRole:
            # will rename the individual columns to their respective names
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])


# the main file user interface
class MainWindow(QMainWindow):
    def __init__(self, connection: Connection):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.conn = connection
        self.date_time = QDate.currentDate()
        self.caveman_crypt = security.CavemanCrypt()

        # change the window title 
        self.setWindowTitle("Agro IQ")
        self.setWindowIcon(QIcon("images/images/cow-2-256.ico"))
        self.dropdown = DropDown()

        self.initialSetUp()

        # go to the registration page
        self.ui.registerButton.clicked.connect(self.switchToRegPage)
        # go back to login page
        self.ui.backToLogInBtn.clicked.connect(self.switchToLogInPage)

        # close the window
        self.ui.closeAppBtn_3.clicked.connect(self.close)
        # maximize restore btn
        self.ui.maximizeRestoreAppBtn_3.clicked.connect(self.maximizeRestore)
        # minimize btn 
        self.ui.minimizeAppBtn_3.clicked.connect(self.showMinimized)
        # login button 
        self.ui.logInButton.clicked.connect(self.uathenticateLogin)
        # register button
        self.ui.registerAccountButton.clicked.connect(self.authenticateRegistration)

        self.cleanInputsOnTyping()

        # apply the shadow effect on the login page and registration page.
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.registerFrame.setGraphicsEffect(self.shadow)

        self.shadow1 = QGraphicsDropShadowEffect(self)
        self.shadow1.setBlurRadius(20)
        self.shadow1.setXOffset(0)
        self.shadow1.setYOffset(0)
        self.shadow1.setColor(QColor(0, 0, 0, 60))
        self.ui.logInFrame.setGraphicsEffect(self.shadow1)

        # CHANGE THE FONT  
        self.changeFont()

        # LOG OUT 
        self.ui.logOutBtn.clicked.connect(self.logOut)

        self.animationSideBar = QPropertyAnimation(self.ui.fullSideBar, b"maximumWidth")
        self.animationFilters = QPropertyAnimation(self.ui.filters, b"maximumHeight")
        self.ui.settingsTopBtn_3.clicked.connect(self.toggleSideBar)
        self.ui.closeSideBar.clicked.connect(self.toggleSideBar)
        self.ui.pushButton_19.clicked.connect(self.toggleSideBar)

        # paging buttons
        self.ui.homeBtn.clicked.connect(self.home)
        self.ui.cattleHealthBtn.clicked.connect(self.cattleHealth)
        self.ui.manageBreedingBtn.clicked.connect(self.manageBreeding)
        self.ui.manageFinancialsBtn.clicked.connect(self.manageFinancials)
        self.ui.manageInventoryBtn.clicked.connect(self.manageInventory)
        self.ui.addAnimalBtn.clicked.connect(self.addAnimal)

        #  SET THE DATE TO THE MAIN PAGE 
        self.displayDateInMainPage()
        # REFRESH THE PAGE EVERY 24 hours 

        self.herHealth()

        # MA DROP DOWNS ACHO ANOTANGIRA PANO
        self.calendar_btn = self.ui.popupCalendar
        self.date_time_1 = self.ui.checkUpDate
        self.calendar_btn.clicked.connect(self.open_dropdown)
        self.date_time_frame = self.ui.frame_33
        self.dropdown.installEventFilter(self)

        self.dropdown.dateTimeChanged_str.connect(self.set_new_date_time)

        self.getDeviceDetails()

        # show the password 
        self.ui.showPasswordChkBox.clicked.connect(self.showPassword)
        # when the user starts typing in the farm id input show their name

        self.ui.farmIdRegisterInput.textChanged.connect(self.displayUserDetails)

        # hide filters 
        self.ui.checkBoxHideFilters.clicked.connect(self.hideFilters)

        # when the user presses the submit button for adding animal data
        self.ui.submitAnimalDataBtn.clicked.connect(self.animalProfile)
        self.viewAnimalData()

        # self.showResultsTable()
        self.checkIfFiltersHidden()
        # self.switchFilterMethods()
        self.ui.checkBoxAllFilters.clicked.connect(self.switchFilterMethods)
        self.switchFilterMethods()

        self.ui.departmentCheckBox.clicked.connect(self.enableFilterDepartment)
        self.ui.animalSexcheckBox.clicked.connect(self.enableFilterAnimalSex)

        self.updateAnimalData()
        # search for animal health history
        self.searchAnimalHealthHistory()
        self.ui.dataViewOptionsHealthComboBox.currentTextChanged.connect(self.searchAnimalHealthHistory)
        # when the user clicks on the export as excel button.
        self.ui.export_as_excel_1.clicked.connect(
            lambda:  self.fileExportExcel( search_results_table[0], animal_health_detail_colums)
        )

        self.showResultsForAnimalData()

        # when someone presses the set reminder btn on the schedule vet appontment page.
        self.ui.btnSetAppointment.clicked.connect(self.setVetAppointMent)

    def setVetAppointMent(self):
        # get the data from the inputs
        # sql_notifications = f"INSERT INTO notifications VALUES('{data["date_set"]}', '{data["date_end"]}', '{data[""]}', '{data["notification_id"]}')"
        # sql_vet_appointments = f"INSERT INTO vet_appointments VALUES('{data["purpose"]}', '{data["notification_id"]}', '{data["organization"]}', '{data["is_queued"]}')"

        # generate a unique id for every notification.
        rand = rnd.randomValueGen()
        date_time = self.ui.checkUpDate.dateTime()

        data = {
            "date_set": datetime.datetime.now(),
            "date_end": self.ui.checkUpDate.dateTime().toPython(),
            "notification_id": rand.generate_random_id(),
            "purpose": self.ui.checkUpPurpose.currentText(), 
            "organization": self.ui.vetOrgName.text(),
            "is_queued": True
        }

        print(data)
        # send the data to the database
        # self.conn.addVetAppointment(data)

    def fileExportExcel(self, data: list, columns: list):
        file_filters = [
            "Comma Separated Values (*.csv)"
        ]

        initial_dir = ""

        if len(data) < 1:
            print("cannot save empty data..!")
        else:
            filename = QFileDialog.getSaveFileName(
                self, caption="", dir=initial_dir, filter=file_filters[0]
            )

            print("SAVED: ", filename)

            print(f"DATA={data}")
            print(f"COLUMNS={columns}")

            if len(filename[0]) < 1:
                print("cancelled file save..!")
            else:
                export_csv = ExportExcelData(data=data, columns=columns, filename=filename[0])
                export_csv.export_to_file()


    def initialSetUp(self):

        # REMOVE TITLE BAR
        if not CUSTOM_TITLE_BAR:
            self.ui.title_bar.setVisible(False)
            # move the settings icon elsewhere
        else:
            ## REMOVE THE TITLE BAR AND SET TO CUSTOM
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            # remove the settings button from the sidebar in this mode
            self.ui.pushButton_19.setVisible(False)

        # HIDE THE SETTINGS BAR
        self.ui.fullSideBar.setFixedWidth(0)

    def keyPressEvent(self, event):
        global KEY_RETURN

        if isinstance(event, QKeyEvent):
            key_text = event.key()

            if event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter:
                print(f"enter was pressed: {QtCore.Qt.Key.Key_Return}")
                KEY_RETURN = event.key()
                return event
            else:
                # KEY_RETURN = event.key()
                print(f"{key_text} was pressed.")
                return event

    def enableFilterDepartment(self):

        if self.ui.departmentCheckBox.isChecked():
            self.ui.departmentFilterCategory.setDisabled(False)
        else:
            self.ui.departmentFilterCategory.setDisabled(True)

    def enableFilterAnimalSex(self):

        if self.ui.animalSexcheckBox.isChecked():
            self.ui.sexFilterInput.setDisabled(False)
        else:
            self.ui.sexFilterInput.setDisabled(True)

    def updateAnimalData(self):
        """
            - When a user clicks on a cell in the search results table and changes its data, 
              update that particular column data in the database.
        """
        self.ui.animalResultsTable.cellDoubleClicked.connect(self.cellClickedCustom)

    def cellClickedCustom(self, row, column):

        dlg = DialogBoxDbEdit(self.ui.animalResultsTable.item(row, 0).text())

        if dlg.exec():
            for i, query in enumerate(dlg.getData()):
                print(f"buffered sql query[{i}]: ", query)
                # execute the buffered queries
                self.conn.updateAnimal(query)

            # clear the buffer after execution
            dlg.clearQueryBuffer()
            # update the search results
            self.showResultsTable()
        else:
            print("transaction cancelled.")

    def searchAnimalHealthHistory(self):
        global search_option
        global search_results_table
        global animal_health_detail_colums

        vaccination_history = False
        health_history = True


        if self.ui.dataViewOptionsHealthComboBox.currentText() == "Health history":
            # set the label to health history
            self.ui.label_52.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html>"
                                                                u"<head/>"
                                                                u"<body>"
                                                                u"<p><span style=\" font-style:italic; "
                                                                u"color:#d9f9ff;\">Track health history </span></p>"
                                                                u"</body>"
                                                                u"</html>",
                                                                None))
            search_option = True
        else:
            # set the label to vaccination history
            self.ui.label_52.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html>"
                                                                u"<head/>"
                                                                u"<body>"
                                                                u"<p><span style=\" font-style:italic; "
                                                                u"color:#d9f9ff;\">Track vaccination history "
                                                                u"</span></p>"
                                                                u"</body>"
                                                                u"</html>",
                                                                None))
            search_option = False

        if search_option is health_history:
            self.ui.searchBarHealthHist.setPlaceholderText("Search Keyword(tag id, disease name)...")
            # will add functionality to keep fetching the data in batches of 20 everytime a user scrolls.
            search_results = self.conn.selectAllHealthHistory()
            search_results_table = [search_results, 0]

            data = pd.DataFrame(
                search_results,
                columns=['tag id', 'disease', 'disease description/info', 'symptoms', 'date infected']
            )

            model = TableModel(data)
            self.ui.tableView.setModel(model)

            # when the user starts typing in the search bar show the results
            self.ui.searchBarHealthHist.textChanged.connect(self.createUpdateResultsTableForHealthHistory)
            animal_health_detail_colums = ['tag id', 'disease', 'disease description/info', 'symptoms', 'date infected']

        elif search_option is vaccination_history:

            search_results = self.conn.selectAllVaccinationHistory()
            search_results_table = [search_results, 0]

            print(search_results)
            data = pd.DataFrame(
                search_results,
                columns=['tag id', 'vaccine name', 'dosage in mg', 'date vaccinated', 'reason for vaccination', 'org..']
            )

            model = TableModel(data)
            self.ui.tableView.setModel(model)

            # when the user starts typing in the search bar show the results
            self.ui.searchBarHealthHist.textChanged.connect(self.createUpdateResultsTableForHealthHistory)
            self.ui.searchBarHealthHist.textChanged.connect(self.createUpdateResultsTableForVaccinationHistory)
            self.ui.searchBarHealthHist.setPlaceholderText("Search Keyword(tag id, vaccine name, organization)...")
            animal_health_detail_colums = ['tag id', 'vaccine name', 'dosage in mg', 'date vaccinated', 'reason for vaccination', 'org..']


    def createUpdateResultsTableForVaccinationHistory(self):
        global search_results_table
        global search_option

        vaccination_history = False
        print("THE CURRENT TABLE DATA: ", search_results_table)

        # IF THE USER SELECTS THE VACCINATION HISTORY OPTION.
        if search_option is vaccination_history:

            search_results_table = self.conn.searchForVaccinationHistory(
                [self.ui.searchBarHealthHist.text()]
            )
            print(search_results_table)
            self.ui.tableContainer.setCurrentIndex(0)
            if self.ui.searchBarHealthHist.text() != "":
                if search_results_table[1] == 0:

                    data = pd.DataFrame(
                        search_results_table[0],
                        columns=['tag id', 'vaccine name', 'dosage in mg', 'date vaccinated', 'reason for vaccination',
                                 'org..']
                    )
                    self.ui.tableContainer.setCurrentIndex(1)
                    model = TableModel(data)
                    self.ui.tableView.setModel(model)
                else:
                    data = pd.DataFrame(
                        search_results_table[0],
                        columns=['tag id', 'vaccine name', 'dosage in mg', 'date vaccinated', 'reason for vaccination',
                                 'org..']
                    )
                    self.ui.tableContainer.setCurrentIndex(0)
                    model = TableModel(data)
                    self.ui.tableView.setModel(model)

                    for res in search_results_table:
                        print(f"search results: {res}")
            else:
                # will add functionality to keep fetching the data in batches of 20 everytime a user scrolls.
                search_results = self.conn.selectAllVaccinationHistory()

                search_results_table = search_results
                print("SEARCH RESULTS DATA", search_results_table)
                print(search_results)
                data = pd.DataFrame(
                    search_results,
                    columns=['tag id', 'vaccine name', 'dosage in mg', 'date vaccinated', 'reason for vaccination',
                             'org..']
                )

                model = TableModel(data)
                self.ui.tableView.setModel(model)

    def createUpdateResultsTableForHealthHistory(self):
        global search_results_table
        global search_option

        health_history = True

        print("THE CURRENT TABLE DATA: ", search_results_table)

        if search_option is health_history:
            search_results_table = self.conn.searchForDisease(
                [self.ui.searchBarHealthHist.text()]
            )
            print("SEARCH RESULTS DATA", search_results_table)

            if len(self.ui.searchBarHealthHist.text()) > 0:
                if search_results_table[1] == 0:

                    data = pd.DataFrame(
                        search_results_table[0],
                        columns=['tag id', 'disease', 'disease description/info', 'symptoms', 'date infected']
                    )
                    self.ui.tableContainer.setCurrentIndex(1)
                    model = TableModel(data)
                    self.ui.tableView.setModel(model)
                else:
                    data = pd.DataFrame(
                        search_results_table[0],
                        columns=['tag id', 'disease', 'disease description/info', 'symptoms', 'date infected']
                    )
                    self.ui.tableContainer.setCurrentIndex(0)
                    model = TableModel(data)
                    self.ui.tableView.setModel(model)

                    for res in search_results_table:
                        print(f"search results: {res}")
            else:
                # will add functionality to keep fetching the data in batches of 20 everytime a user scrolls.
                search_results = self.conn.selectAllHealthHistory()
                search_results_table = search_results
                print("SEARCH RESULTS DATA", search_results_table)
                data = pd.DataFrame(
                    search_results,
                    columns=['tag id', 'disease', 'disease description/info', 'symptoms', 'date infected']
                )

                model = TableModel(data)
                self.ui.tableView.setModel(model)

    def switchFilterMethods(self):
        """
            - when the user disables the filter methods, use the search button to update results.
        """

        if self.ui.checkBoxAllFilters.isChecked():
            self.ui.searchBar.setPlaceholderText(
                "search by any key word or number in the tables (breed, tag id and department).")
            self.ui.searchBar.textChanged.connect(self.search)
            self.ui.searchBtn.clicked.connect(self.search)
        else:
            self.ui.searchBar.setPlaceholderText("search...")
            self.ui.searchBar.textChanged.connect(self.search)
            self.ui.searchBtn.clicked.connect(self.search)

    def search(self):
        # to store the animal search results globally
        global search_results_table_animal

        # update the search result table
        search_results = self.conn.searchForAnimal([

            self.ui.filter_animalBreed.isChecked(),  # filter by breed
            self.ui.filter_tagId.isChecked(),  # filter by tag id
            self.ui.animalSexcheckBox.isChecked(),  # filter by sex
            self.ui.departmentCheckBox.isChecked(),  # filter by department
            self.ui.activateCategoryAndSexFilters.isChecked(),  # animal or sex department checkbox
            self.ui.searchBar.text(),  # search bar data
            self.ui.sexFilterInput.currentText(),
            self.ui.departmentFilterCategory.currentText(),
            self.ui.checkBoxAllFilters.isChecked()
        ])

        search_results_table_animal = search_results

        print(f"SEARCH RESULTS FOR ANIMAL: {search_results}")
        # # update the table as i am typing
        self.showResultsTable()


    def showResultsForAnimalData(self):
        # update the search results table with all the data in the database 
        # later will add functionality to fetct the data as the user scrolls.
        global search_results_table_animal
        search_results_table_animal = self.conn.fetchAllAnimalData()
        self.showResultsTable()

    def showResultsTable(self):
        """
            - Display the filtered results in the results table
        """

        # we are now reading the search results from a global list instead of the views
        search_results = search_results_table_animal

        print(f"SEARCH RESULTS: {search_results}\n")
        self.ui.animalResultsTable.setRowCount(len(search_results))

        animal_sex = {"1": "male", "0": "female"}
        for i, (tagId, breed, age, weight, sex, chars, dep) in enumerate(search_results):
            result_item_tag_id = QTableWidgetItem(tagId)
            result_item_breed = QTableWidgetItem(breed)
            result_item_age = QTableWidgetItem(str(age))
            result_item_weight = QTableWidgetItem(str(weight))
            result_item_sex = QTableWidgetItem(animal_sex[str(sex)])
            result_item_chars = QTableWidgetItem(chars)
            result_item_dep = QTableWidgetItem(dep)

            self.ui.animalResultsTable.setItem(i, 0, result_item_tag_id)
            self.ui.animalResultsTable.setItem(i, 1, result_item_breed)
            self.ui.animalResultsTable.setItem(i, 2, result_item_age)
            self.ui.animalResultsTable.setItem(i, 3, result_item_weight)
            self.ui.animalResultsTable.setItem(i, 4, result_item_sex)
            self.ui.animalResultsTable.setItem(i, 5, result_item_chars)
            self.ui.animalResultsTable.setItem(i, 6, result_item_dep)

    def checkIfFiltersHidden(self):
        if self.ui.checkBoxHideFilters.isChecked():
            self.ui.filters.setFixedHeight(0)

    def hideFilters(self):
        global FILTERS_HIDDEN
        current_height = self.ui.filters.height()
        expanded_height = 200
        collapsed_height = 0

        if self.ui.checkBoxHideFilters.isChecked():
            target_height = collapsed_height
            FILTERS_HIDDEN = True

        else:
            target_height = expanded_height
            FILTERS_HIDDEN = False

        self.animationFilters.setDuration(250)
        self.animationFilters.setStartValue(current_height)
        self.animationFilters.setEndValue(target_height)
        self.animationFilters.start()

    def displayUserDetails(self):
        if len(self.ui.farmIdRegisterInput.text()) == 5:
            self.ui.firstNameInput.setText(
                self.conn.getUserDetails(self.ui.farmIdRegisterInput.text())[0]  # set the first name
            )

            self.ui.lastNameInput.setText(
                self.conn.getUserDetails(self.ui.farmIdRegisterInput.text())[1]  # set the last name
            )
        else:
            # clear the inputs when user deletes stuff from farm id text book
            self.ui.firstNameInput.setText(
                ""  # set the first name
            )
            self.ui.lastNameInput.setText(
                ""  # set the last name
            )

    def showPassword(self):

        if self.ui.showPasswordChkBox.isChecked():
            # print("cheked")
            self.ui.passwordInputConfirm.setEchoMode(PySide6.QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.ui.passwordInputConfirm.setEchoMode(PySide6.QtWidgets.QLineEdit.EchoMode.Password)
            # print("unchecked")

    def getDeviceDetails(self):
        sys_info = platform.uname()
        self.ui.deviceName.setText(f"{sys_info.system} {sys_info.version}")
        self.ui.softwareVersion.setText(f"{sys_info.processor}")

    def set_new_date_time(self, date_str: str):
        # Extract date and time components from the formatted string
        data_list = date_str.split(",")

        am_pm_str = data_list.pop()

        month, day, year, hour, minute = map(int, data_list)

        # Adjust hour for PM
        if am_pm_str == "PM":
            hour += 12

        # Create QDateTime object and set it to the date time edit field
        date_time_1 = QDateTime(QDate(year, month, day), QTime(hour, minute))
        self.date_time_1.setDateTime(date_time_1)

    def open_dropdown(self, state):
        if state and not self.dropdown.isVisible():
            # Position the dropdown below the date time edit field
            self.dropdown.move(self.pos().x() + self.date_time_frame.pos().x(),
                               self.pos().y() + self.date_time_frame.pos().y() + self.date_time_frame.height() + 40)
            self.dropdown.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            self.dropdown.show()
            print("sate: ", state)
        else:
            self.dropdown.close()

    def closeEvent(self, event):
        # Close the dropdown when the main window is closed
        self.dropdown.close()
        self.calendar_btn.setChecked(False)

    def eventFilter(self, obj, event):
        # Close the dropdown if it loses focus
        if self.calendar_btn.isChecked() and obj == self.dropdown and event.type() == QEvent.WindowDeactivate:
            self.dropdown.close()
        return super().eventFilter(obj, event)

    # for the heard health monitoring
    def herHealth(self):
        self.anotherChart()
        # cw = ChartWidget(self.ui.plotCard)
        # cw.add_chart()

    def anotherChart(self):
        # create a function that draws these charts with just puting data as input.
        self.set0 = QBarSet("Bovine Viral Diarrhea (BVD)")
        self.set1 = QBarSet("Bovine Respiratory Disease Complex (BRD)")
        self.set2 = QBarSet("Mastitis")
        self.set3 = QBarSet("Bloat")
        self.set4 = QBarSet("Foot Rot")

        self.set0.append([1, 2, 3, 4, 5, 6])
        self.set1.append([5, 0, 0, 4, 0, 7])
        self.set2.append([3, 5, 8, 13, 8, 5])
        self.set3.append([5, 6, 7, 3, 4, 5])
        self.set4.append([9, 7, 5, 3, 1, 2])

        self._bar_series = QBarSeries()
        self._bar_series.append(self.set0)
        self._bar_series.append(self.set1)
        self._bar_series.append(self.set2)
        self._bar_series.append(self.set3)
        self._bar_series.append(self.set4)

        self._line_series = QLineSeries()
        self._line_series.setName("trend")
        self._line_series.append(QPoint(0, 4))
        self._line_series.append(QPoint(1, 15))
        self._line_series.append(QPoint(2, 20))
        self._line_series.append(QPoint(3, 4))
        self._line_series.append(QPoint(4, 12))
        self._line_series.append(QPoint(5, 17))

        self.chart = QChart()
        self.chart.addSeries(self._bar_series)
        self.chart.addSeries(self._line_series)
        self.chart.setTitle("Graph of disease against number of cows for the first six months.")

        self.categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self.categories)
        self.chart.addAxis(self._axis_x, Qt.AlignBottom)
        self._line_series.attachAxis(self._axis_x)
        self._bar_series.attachAxis(self._axis_x)
        self._axis_x.setRange("Jan", "Jun")

        self._axis_y = QValueAxis()
        self.chart.addAxis(self._axis_x, Qt.AlignLeft)
        self._line_series.attachAxis(self._axis_y)
        self._bar_series.attachAxis(self._axis_y)
        self._axis_y.setRange(0, 20)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.ui.plotCard.addWidget(self._chart_view)

        self.shadofyTheCards()

    # create backdrop shadows for frames 
    def shadofyTheCards(self):
        cards = [self.ui.frame_43, self.ui.frame_44, self.ui.frame_45, self.ui.frame_46]

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))

        self.shadow1 = QGraphicsDropShadowEffect(self)
        self.shadow1.setBlurRadius(20)
        self.shadow1.setXOffset(0)
        self.shadow1.setYOffset(0)
        self.shadow1.setColor(QColor(0, 0, 0, 60))

        self.shadow2 = QGraphicsDropShadowEffect(self)
        self.shadow2.setBlurRadius(20)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.shadow2.setColor(QColor(0, 0, 0, 60))

        self.shadow3 = QGraphicsDropShadowEffect(self)
        self.shadow3.setBlurRadius(20)
        self.shadow3.setXOffset(0)
        self.shadow3.setYOffset(0)
        self.shadow3.setColor(QColor(0, 0, 0, 60))

        cards[0].setGraphicsEffect(self.shadow)
        cards[1].setGraphicsEffect(self.shadow1)
        cards[2].setGraphicsEffect(self.shadow2)
        cards[3].setGraphicsEffect(self.shadow3)

        # for the side bar
        self.shadow4 = QGraphicsDropShadowEffect(self)
        self.shadow4.setBlurRadius(20)
        self.shadow4.setXOffset(0)
        self.shadow4.setYOffset(0)
        self.shadow4.setColor(QColor(0, 0, 0, 60))
        self.ui.iconOnlySideBar.setGraphicsEffect(self.shadow4)

    # FUNCTION TO CLEAN THE INPUTS
    def cleanInputsOnTyping(self):
        # the string containing the style for the inputs 
        border_err_none = "border: none; QLineEdit:focus{ border: 2px solid #bbb;}"

        # WHEN THE USER STARTS TYPING IN THE INPUT REMOVE THE RED STYLES
        self.ui.passwordInputLogIn.textChanged.connect(
            lambda: self.ui.passwordInputLogIn.setStyleSheet(border_err_none)
        )

        self.ui.passwordInputLogIn.textChanged.connect(
            lambda: self.ui.registrationErr.setText("")
        )

        self.ui.farmIdInput.textChanged.connect(
            lambda: self.ui.farmIdInput.setStyleSheet(border_err_none)
        )

        self.ui.farmIdInput.textChanged.connect(
            lambda: self.ui.registrationErr.setText("")
        )

        # FOR THE REGISTRATION FORM 
        self.ui.farmIdRegisterInput.textChanged.connect(
            lambda: self.ui.farmIdRegisterInput.setStyleSheet(border_err_none)
        )

        self.ui.farmIdRegisterInput.textChanged.connect(
            lambda: self.ui.registrationErr.setText("")
        )

        self.ui.lastNameInput.textChanged.connect(
            lambda: self.ui.lastNameInput.setStyleSheet(border_err_none)
        )

        self.ui.lastNameInput.textChanged.connect(
            lambda: self.ui.registrationErr.setText("")
        )

        # 
        self.ui.firstNameInput.textChanged.connect(
            lambda: self.ui.firstNameInput.setStyleSheet(border_err_none)
        )

        self.ui.firstNameInput.textChanged.connect(
            lambda: self.ui.registrationErr.setText("")
        )

        self.ui.passwordInputReg.textChanged.connect(
            lambda: self.ui.passwordInputReg.setStyleSheet(border_err_none)
        )

        self.ui.passwordInputReg.textChanged.connect(
            lambda: self.ui.registrationErr.setText("")
        )

        self.ui.passwordInputConfirm.textChanged.connect(
            lambda: self.ui.passwordInputConfirm.setStyleSheet(border_err_none)
        )

        self.ui.passwordInputConfirm.textChanged.connect(
            lambda: self.ui.registrationErr.setText("")
        )

        # clean the inputs of the animal profile page

        # tag id
        self.ui.tagIdInput.textChanged.connect(
            lambda: self.ui.errLabelAnimalDetails.setText("")
        )

        self.ui.tagIdInput.textChanged.connect(
            lambda: self.ui.tagIdInput.setStyleSheet("border: 1px solid #000")
        )

        self.ui.tagIdInput.textChanged.connect(
            lambda: self.ui.label_18.setText("Tag Id")
        )

        self.ui.tagIdInput.textChanged.connect(
            lambda: self.ui.label_18.setStyleSheet("color: #000")
        )

        # animal breed 
        self.ui.animalBreedInput.textChanged.connect(
            lambda: self.ui.errLabelAnimalDetails.setText("")
        )

        self.ui.animalBreedInput.textChanged.connect(
            lambda: self.ui.label_19.setText("Animal Breed")
        )

        self.ui.tagIdInput.textChanged.connect(
            lambda: self.ui.label_19.setStyleSheet("color: #000")
        )

        self.ui.animalBreedInput.textChanged.connect(
            lambda: self.ui.animalBreedInput.setStyleSheet("border: 1px solid #000")
        )

    # FUNCTION TO DISPLAY THE CURRENT DATE 
    def displayDateInMainPage(self):
        date_string = f"{self.date_time.toString(Qt.DateFormat.RFC2822Date)}"
        self.ui.dateDisplay.setText(date_string)

    # PAGING FUNCTIONS
    def home(self):
        # cache the previous index 
        global STACKED_INDEX
        self.ui.stackedWidgetMainContent.setCurrentIndex(0)
        STACKED_INDEX = self.ui.stackedWidgetMainContent.currentIndex()

        if SIDE_BAR_VISIBLE:
            self.toggleSideBar()

    def cattleHealth(self):
        # cache the previous index 
        global STACKED_INDEX
        self.ui.stackedWidgetMainContent.setCurrentIndex(1)
        STACKED_INDEX = self.ui.stackedWidgetMainContent.currentIndex()

        if SIDE_BAR_VISIBLE:
            self.toggleSideBar()

    def manageBreeding(self):
        # cache the previous index 
        global STACKED_INDEX
        self.ui.stackedWidgetMainContent.setCurrentIndex(2)
        STACKED_INDEX = self.ui.stackedWidgetMainContent.currentIndex()

        if SIDE_BAR_VISIBLE:
            self.toggleSideBar()

    def manageFinancials(self):
        # cache the previous index 
        global STACKED_INDEX
        self.ui.stackedWidgetMainContent.setCurrentIndex(3)
        STACKED_INDEX = self.ui.stackedWidgetMainContent.currentIndex()

        if SIDE_BAR_VISIBLE:
            self.toggleSideBar()

    def manageInventory(self):
        # cache the previous index 
        global STACKED_INDEX
        self.ui.stackedWidgetMainContent.setCurrentIndex(4)
        STACKED_INDEX = self.ui.stackedWidgetMainContent.currentIndex()

        if SIDE_BAR_VISIBLE:
            self.toggleSideBar()

    def addAnimal(self):
        # cache the previous index 

        global STACKED_INDEX
        self.ui.stackedWidgetMainContent.setCurrentIndex(5)
        STACKED_INDEX = self.ui.stackedWidgetMainContent.currentIndex()

        if SIDE_BAR_VISIBLE:
            self.toggleSideBar()

    # LOG OUT FUNCTION
    def logOut(self):
        global LOGGED_IN
        self.ui.mainFrame.setCurrentIndex(0)
        LOGGED_IN = False

    # WHEN THE USER TRIES TO LOGIN 
    def logIn(self):
        global LOGGED_IN
        self.ui.mainFrame.setCurrentIndex(1)
        LOGGED_IN = True

    # APPLY SIDE BAR ANIMATION
    def toggleSideBar(self):
        global LOGGED_IN
        global STACKED_INDEX
        global SIDE_BAR_VISIBLE
        # this functionality only activates when the user is logged in
        if (LOGGED_IN):
            current_width = self.ui.fullSideBar.width()
            expanded_width = 200
            collapsed_width = 0

            if current_width == collapsed_width:
                target_width = expanded_width
                # show the settings page
                self.ui.stackedWidgetMainContent.setCurrentIndex(6)
                SIDE_BAR_VISIBLE = True

            else:
                # revert to that previous index 
                self.ui.stackedWidgetMainContent.setCurrentIndex(STACKED_INDEX)
                target_width = collapsed_width
                SIDE_BAR_VISIBLE = False

            self.animationSideBar.setDuration(250)
            self.animationSideBar.setStartValue(current_width)
            self.animationSideBar.setEndValue(target_width)
            self.animationSideBar.start()

        else:
            print("settings not available right now please log in")

    #   WHEN THE USER PRESSES THE RESIZE BUTTON 
    def maximizeRestore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.maximizeRestoreAppBtn_3.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn_3.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))

        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.ui.maximizeRestoreAppBtn_3.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn_3.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))

    def changeFont(self):
        id = QFontDatabase.addApplicationFont("Roboto/static/Roboto-Bold.ttf")
        if id < 0: print("Error")

        # add to the font families database 
        families = QFontDatabase.applicationFontFamilies(id)

        # set the font for the title login and registration
        self.ui.TitleLogin.setFont(QFont(families[0], 72))
        self.ui.RegistrationTitle.setFont(QFont(families[0], 72))

    def activateCategoryAndSexFiltersCheckBox(self):

        # tuned off by deafalt 
        self.ui.departmentFilterCategory.setEnabled(False)

        if self.ui.activateCategoryAndSexFilters.isChecked():
            self.ui.secondaryFilterOptions.setEnabled(True)
            print("enabled..!")
        else:
            print("disabled...!")
            self.ui.secondaryFilterOptions.setEnabled(False)

    def viewAnimalData(self):
        # button to activate the sex and department filters 
        self.ui.activateCategoryAndSexFilters.clicked.connect(
            self.activateCategoryAndSexFiltersCheckBox
        )

        # searching function 

    def animalProfile(self):
        # add new animal to the database 

        animal_sex_param = False  # male
        if self.ui.sexInput.currentText() == "male":
            animal_sex_param = True
        else:
            animal_sex_param = False

        animal_data_cache = {
            "id": self.ui.tagIdInput.text(),
            "breed": self.ui.animalBreedInput.text(),
            "age_months": self.ui.ageInMonths.value(),
            "weight_kg": self.ui.newAnimalWeightInput.value(),
            "sex": animal_sex_param,
            "animal_characteristics": "",  # will add functionality to extract the text later on.
            "department": self.ui.departmentInput.currentText()
        }


        if self.ui.tagIdInput.text() == '':
            self.ui.tagIdInput.setStyleSheet("border: 1px solid #ff6666")
            self.ui.errLabelAnimalDetails.setText("Tag Id is required to complete operation.")
            self.ui.label_18.setStyleSheet("color: #ff6666;")
            self.ui.label_18.setText("Tag Id (field required!)")

        elif self.ui.animalBreedInput.text() == '':
            self.ui.animalBreedInput.setStyleSheet("border: 1px solid #ff6666")
            self.ui.errLabelAnimalDetails.setText("animal breed field is required to complete operation.")
            self.ui.label_19.setStyleSheet("color: #ff6666;")
            self.ui.label_19.setText("Animal Breed (field required!)")

        elif not self.conn.addAnimal(animal_data_cache):
            self.ui.tagIdInput.setStyleSheet("border: 1px solid #ff6666")
            self.ui.errLabelAnimalDetails.setText("Tag Id is already logged in the database.")
            self.ui.label_18.setStyleSheet("color: #ff6666;")
            self.ui.label_18.setText("Tag Id")
        else:
            # clear the inputs on success 
            self.ui.tagIdInput.clear()
            self.ui.animalBreedInput.clear()
            self.ui.newAnimalWeightInput.setValue(0.0)
            self.ui.ageInMonths.setValue(0.0)
            # add a dialogue box indicating successifull logging
            self.ui.errLabelAnimalDetails.setText("Animal Details succesifully added to database.")

    def switchToRegPage(self):
        # clear the login inputs 
        self.ui.logInError.setText("")
        self.ui.passwordInputLogIn.setText("")
        self.ui.farmIdInput.setText("")
        self.ui.passwordInputLogIn.setStyleSheet("border: none; QLineEdit:focus{ border: 2px solid #bbb;}")
        self.ui.farmIdInput.setStyleSheet("border: none; QLineEdit:focus{ border: 2px solid #bbb;}")
        self.ui.uathenticationStack.setCurrentIndex(1)

    def switchToLogInPage(self):
        self.ui.uathenticationStack.setCurrentIndex(0)
        self.resetRegistrationInputs()

    def resetRegistrationInputs(self):
        self.ui.firstNameInput.setStyleSheet("border: none; QLineEdit:focus{ border: 2px solid #bbb;}")
        self.ui.lastNameInput.setStyleSheet("border: none; QLineEdit:focus{ border: 2px solid #bbb;}")
        self.ui.passwordInputReg.setStyleSheet("border: none; QLineEdit:focus{ border: 2px solid #bbb;}")
        self.ui.passwordInputConfirm.setStyleSheet("border: none; QLineEdit:focus{ border: 2px solid #bbb;}")
        self.ui.farmIdRegisterInput.setStyleSheet("border: none; QLineEdit:focus{ border: 2px solid #bbb;}")
        self.ui.passwordInputReg.setStyleSheet("border: none; QLineEdit:focus{ border: 2px solid #bbb;}")
        self.ui.registrationErr.setText("")

        # remove the text from the inputs 
        self.ui.firstNameInput.setText("")
        self.ui.lastNameInput.setText("")
        self.ui.passwordInputReg.setText("")
        self.ui.passwordInputConfirm.setText("")
        self.ui.farmIdRegisterInput.setText("")
        self.ui.passwordInputReg.setText("")

    def authenticateRegistration(self):
        # the user data 
        farm_acc_reg_data = [
            "data",
            "data",
            self.ui.farmIdRegisterInput.text(),
            self.ui.passwordInputReg.text()
        ]

        # if self.ui.firstNameInput.text() == '':
        #     self.ui.firstNameInput.setStyleSheet("border: 2px solid #ff6666;")
        #     self.ui.registrationErr.setText("first name is required")

        # elif self.ui.lastNameInput.text() == '':
        #     self.ui.lastNameInput.setStyleSheet("border: 2px solid #ff6666;")
        #     self.ui.registrationErr.setText("the last name field is required")

        if self.ui.farmIdRegisterInput.text() == '':
            self.ui.farmIdRegisterInput.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.registrationErr.setText("the farmIdRegisterInput field is required")

        # check if the farm id exist in the employee database 
        elif self.conn.register(farm_acc_reg_data)[0] == 0:
            self.ui.farmIdRegisterInput.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.registrationErr.setText(f"The farm id provided is not recognised within our employee database.")

        # check if the account is already registered 
        elif self.conn.register(farm_acc_reg_data)[1] >= 1:
            self.ui.farmIdRegisterInput.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.registrationErr.setText("the farm id provided is already registered as suite user.")

        # check if user is authorised to create a farm account.
        elif not bool(self.conn.register(farm_acc_reg_data)[2]):
            self.ui.farmIdRegisterInput.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.registrationErr.setText(
                "The user associated with this farm id is not authorised to register a farm account")

        elif self.ui.passwordInputReg.text() == '':
            self.ui.passwordInputReg.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.registrationErr.setText("the password field is required")

        elif self.ui.passwordInputConfirm.text() == '':
            self.ui.passwordInputConfirm.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.registrationErr.setText("the passwordConfirm field is required")


        elif self.ui.passwordInputReg.text() != self.ui.passwordInputConfirm.text():
            self.ui.passwordInputReg.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.passwordInputConfirm.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.registrationErr.setText("the passwords dont match")

        else:
            # encrypt the password using our caveman encryption teqniques.
            encrypted_password = self.caveman_crypt.start_encryption(self.ui.passwordInputReg.text())

            self.conn.add_user_data_to_database(
                [self.ui.farmIdRegisterInput.text(), encrypted_password]
            )
            # clean the inputs 
            self.resetRegistrationInputs()

    def uathenticateLogin(self):

        # for username
        if self.ui.farmIdInput.text() == '':
            self.ui.farmIdInput.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.logInError.setText("Oops, farmId field is required")

        # check the farm id
        elif self.conn.logIn([self.ui.farmIdInput.text(), self.ui.passwordInputLogIn.text()])[1] != 1:
            self.ui.farmIdInput.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.logInError.setText("Oops, invalid farm id")

        # check if user has given input 
        elif self.ui.passwordInputLogIn.text() == '':
            self.ui.passwordInputLogIn.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.logInError.setText("Oops, password field is required")

        elif not self.caveman_crypt.is_password_correct(
                self.conn.logIn([self.ui.farmIdInput.text(), self.ui.passwordInputLogIn.text()])[2],
                self.ui.passwordInputLogIn.text()):
            self.ui.passwordInputLogIn.setStyleSheet("border: 2px solid #ff6666;")
            self.ui.logInError.setText("Oops, invalid password")


        else:
            self.ui.logInError.setText("")
            # clear the login inputs 
            self.ui.passwordInputLogIn.setText("")
            self.ui.farmIdInput.setText("")
            self.logIn()

    # THE EVENT HANDLERS
    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            print("")
        super().changeEvent(event)
        event.accept()

    def window_state_changed(self, state):
        self.normal_button.setVisible(state == Qt.WindowState.WindowMaximized)
        self.max_button.setVisible(state != Qt.WindowState.WindowMaximized)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):
        global GLOBAL_STATE
        if QPoint(self.initial_pos) is not None:
            if self.isMaximized():
                GLOBAL_STATE = False
                self.showNormal()
                self.ui.maximizeRestoreAppBtn_3.setToolTip("Maximize")
                self.ui.maximizeRestoreAppBtn_3.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
                self.initial_pos = self.pos

            current_pos = event.position().toPoint()
            delta = QPoint(current_pos) - self.initial_pos

            # calculations to prevent the window from being dragged out of view 
            new_x = self.window().x() + delta.x()
            new_y = self.window().x() + delta.y()

            # get the screen geometry
            screen_geometry = QApplication.primaryScreen().geometry()
            screen_width = screen_geometry.width()
            screen_height = screen_geometry.height()

            # ensure window remains within screen bounds 
            new_x = max(0, min(new_x, screen_width - self.width()))
            new_y = max(0, min(new_y, screen_height - self.height()))

            self.window().move(new_x, new_y)

            # check if mouse is at the top
            if self.y() <= 0:
                self.showMaximized()
                GLOBAL_STATE = True
                self.ui.maximizeRestoreAppBtn_3.setToolTip("Restore")
                self.ui.maximizeRestoreAppBtn_3.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
                self.initial_pos = None

        super().mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.initial_pos = None
        super().mouseReleaseEvent(event)
        event.accept()

        # the drag resize functionaity

    def nativeEvent(self, eventType, message):
        if eventType == 'windows_generic_MSG':
            msg = MSG.from_address(int(message))
            if msg.message == WM_NCHITTEST:
                return self.handleHitTest(msg.lParam)

        return False, 0

    # HANDLE THE RESIZING OF THE WINDOW USING THE RESIZE CURSOR 
    def handleHitTest(self, lparam):
        pos = QCursor.pos()
        rect = self.rect()

        margin = 10
        x, y = pos.x(), pos.y()

        # check if the cursor is at the edges of the corners 
        if rect.top() + margin >= y >= rect.top() and rect.left() + margin >= x >= rect.left():
            return True, HTTOPLEFT
        elif rect.top() + margin >= y >= rect.top() and rect.right() - margin <= x <= rect.right():
            return True, HTTOPRIGHT
        elif rect.bottom() - margin <= y <= rect.bottom() and rect.left() + margin >= x >= rect.left():
            return True, HTBOTTOMLEFT
        elif rect.bottom() - margin <= y <= rect.bottom() and rect.right() - margin <= x <= rect.right():
            return True, HTBOTTOMRIGHT
        elif rect.top() + margin >= y >= rect.top():
            return True, HTTOP
        elif rect.bottom() - margin <= y <= rect.bottom():
            return True, HTBOTTOM
        elif rect.left() + margin >= x >= rect.left():
            return True, HTLEFT
        elif rect.right() - margin <= x <= rect.right():
            return True, HTRIGHT
        else:
            return True, HTCLIENT
