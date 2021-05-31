# ---------------------------------------------------------------------------- #
#                                  main class                                  #
# ---------------------------------------------------------------------------- #

import sys
# import os
# import platform
# ------------------- IMPORT / GUI AND MODULES AND WIDGETS ------------------- #
from modules import *
from widgets import *
from threading import Thread
# --------------------------- SET AS GLOBAL WIDGETS -------------------------- #
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # --------------------------- SET AS GLOBAL WIDGETS -------------------------- #
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # ---------- USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX ---------- #
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # --------------------------------- APP NAME --------------------------------- #
        title = "ViperEO"
        description = "Face Recognition & Object Detection system"
        # -------------------------------- APPLY TEXTS ------------------------------- #
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # -------------------------------- TOGGLE MENU ------------------------------- #
        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))

        # ---------------------------- SET UI DEFINITIONS ---------------------------- #
        UIFunctions.uiDefinitions(self)
        # --------------------------------- load Data --------------------------------- #
        etat, list = False, []
        # threaded gettingData

        def gettingData():
            UIFunctions.errorOverall(
                self, "Loading data failed, please check your internet connexion.", -1)
            while(True):
                etat, list = AppFunctions.getData(self)
                if etat == True:
                    UIFunctions.errorOverall(
                        self, "Loading ...", -1)
                    UIFunctions.loadData(self, list)
                    UIFunctions.errorOverall(
                        self, "Loaded", 2)
                    break
        Thread(target=gettingData).start()
        # -------------------------- QTableWidget PARAMETERS ------------------------- #
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # ------------------------------- BUTTONS CLICK ------------------------------ #

        # MENUS PAGES
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_recognition.clicked.connect(self.buttonClick)
        widgets.btn_detection.clicked.connect(self.buttonClick)
        widgets.btn_management.clicked.connect(self.buttonClick)

        # MANAGEMENT's MENUS
        widgets.btn_management_overall.clicked.connect(self.buttonClick)
        widgets.btn_management_add.clicked.connect(self.buttonClick)
        widgets.btn_management_delete.clicked.connect(self.buttonClick)
        widgets.btn_management_update.clicked.connect(self.buttonClick)
        widgets.btn_images.clicked.connect(self.buttonClick)
        widgets.btn_images_back.clicked.connect(self.buttonClick)
        # FUNCTIONAL BUTTONS
        widgets.btn_add_submit.clicked.connect(self.buttonClick)
        widgets.btn_images_add.clicked.connect(self.buttonClick)
        widgets.btn_images_remove.clicked.connect(self.buttonClick)
        widgets.btn_update_update.clicked.connect(self.buttonClick)
        widgets.btn_delete_remove.clicked.connect(self.buttonClick)

        # ------------------------------ EXTRA LEFT BOX ------------------------------ #

        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # ------------------------------ EXTRA RIGHT BOX ----------------------------- #
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # --------------------------------- SHOW APP --------------------------------- #
        self.show()

        # ----------------------------- SET CUSTOM THEME ----------------------------- #
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # ---------------------------- SET THEME AND HACKS --------------------------- #
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # ----------------------- SET HOME PAGE AND SELECT MENU ---------------------- #
        widgets.app_pages.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
    # ------------------------------- BUTTONS CLICK ------------------------------ #

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        # ----------------------------------- MENUS ---------------------------------- #
        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.app_pages.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW Management page
        if btnName == "btn_management":
            widgets.app_pages.setCurrentWidget(widgets.management)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            # SET DEFAULT MENU
            widgets.pages.setCurrentWidget(widgets.management_overall)
            UIFunctions.resetManagementStyle(self, btnName)
            widgets.btn_management_overall.setStyleSheet(
                UIFunctions.selectManagementMenu(widgets.btn_management_overall.styleSheet()))
        # SHOW face Recognition page
        if btnName == "btn_recognition":
            widgets.app_pages.setCurrentWidget(
                widgets.recognition)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))
        # SHOW object detection
        if btnName == "btn_detection":
            widgets.app_pages.setCurrentWidget(
                widgets.detection)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))
        # ----------------------------- MANAGEMENT MENUS ----------------------------- #
        # SHOW OVERALL
        if btnName == "btn_management_overall":
            widgets.pages.setCurrentWidget(widgets.management_overall)
            UIFunctions.resetManagementStyle(self, btnName)
            widgets.btn_management_overall.setStyleSheet(
                UIFunctions.selectManagementMenu(widgets.btn_management_overall.styleSheet()))
         # SHOW ADD
        if btnName == "btn_management_add":
            widgets.pages.setCurrentWidget(widgets.management_add)
            UIFunctions.resetManagementStyle(self, btnName)
            widgets.btn_management_add.setStyleSheet(
                UIFunctions.selectManagementMenu(widgets.btn_management_add.styleSheet()))
         # SHOW DELETE
        if btnName == "btn_management_delete":
            widgets.pages.setCurrentWidget(widgets.management_delete)
            UIFunctions.resetManagementStyle(self, btnName)
            widgets.btn_management_delete.setStyleSheet(
                UIFunctions.selectManagementMenu(widgets.btn_management_delete.styleSheet()))
         # SHOW UPDATE
        if btnName == "btn_management_update":
            widgets.pages.setCurrentWidget(widgets.management_update)
            UIFunctions.resetManagementStyle(self, btnName)
            widgets.btn_management_update.setStyleSheet(
                UIFunctions.selectManagementMenu(widgets.btn_management_update.styleSheet()))
        # SHOW IMAGE
        if btnName == "btn_images":
            model = widgets.table_overall.selectedIndexes()
            if not model:
                UIFunctions.errorOverall(self, "Please select a person.", 4)
                return

            id = widgets.table_overall.model().data(model[0])
            firstname = widgets.table_overall.model().data(model[1])
            lastname = widgets.table_overall.model().data(model[2])
            widgets.labelFirstname_image.setText(firstname)
            widgets.labelLastname_image.setText(lastname)
            widgets.pages.setCurrentWidget(widgets.management_images)
            UIFunctions.resetManagementStyle(self, btnName)
            widgets.btn_images.setStyleSheet(
                UIFunctions.selectManagementMenu(widgets.btn_images.styleSheet()))
        # SHOW BACK IMAGE
        if btnName == "btn_images_back":
            widgets.pages.setCurrentWidget(widgets.management_overall)
            UIFunctions.resetManagementStyle(self, btnName)
            widgets.btn_images_back.setStyleSheet(
                UIFunctions.selectManagementMenu(widgets.btn_images_back.styleSheet()))
        # ----------------------------- FUNTIONAL BUTTONS ---------------------------- #
        if btnName == "btn_add_submit":
            # CHECK FORM VALIDATION
            stats, desc = AppFunctions.AddformValidate(self)
            UIFunctions.errorAdd(self, desc, 5)
            if stats:
                person = Person(widgets.add_firstname.text(), widgets.add_lastname.text(
                ), widgets.add_email.text(), widgets.add_phone.text(), widgets.add_adress.toPlainText())
                # CHECK EMAIL AND FIRSTNAME|LASTNAME UNICITY
                stats, desc = AppFunctions.CheckUnicity(self, person)
                if stats:
                    # ADD PERSON
                    if AppFunctions.NewPerson(self, person):
                        UIFunctions.errorAdd(
                            self, "person added successfuly.", 5)
                        UIFunctions.clearAddFeilds(self)
                    else:
                        UIFunctions.errorAdd(
                            self, "Something went wrong...(please contact support)", 5)
                else:
                    UIFunctions.errorAdd(self, desc, 5)

        if btnName == "btn_images_add":
            pass
        if btnName == "btn_images_remove":
            pass
        if btnName == "btn_update_update":
            pass
        if btnName == "btn_delete_remove":
            pass
        if btnName == "btn_add_submit":
            pass

   # ------------------------------- RESIZE EVENTS ------------------------------ #

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # ---------------------------- MOUSE CLICK EVENTS ---------------------------- #
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            # deselected tables .......
            pass
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
