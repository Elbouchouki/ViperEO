# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* -------------------------------------------------------------------------- */\n"
"/*                        STYLE CREATED BY ELBOUCHOUKI                        */\n"
"/* -------------------------------------------------------------------------- */\n"
"\n"
"QWidget {\n"
"  color: rgb(221, 221, 221);\n"
"  font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* --------------------------------- Tooltip -------------------------------- */\n"
"QToolTip {\n"
"  color: #ffffff;\n"
"  background-color: rgba(33, 37, 43, 180);\n"
"  border: 1px solid #211c23;\n"
"  background-image: none;\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 2px solid rgb(255, 121, 198);\n"
"  text-align: left;\n"
"  padding-left: 8px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"/* --------------------------------- Bg App --------------------------------- */\n"
"#bgApp {\n"
"  background-color: #18161b;\n"
"  border: 1px solid #211c23;\n"
"}\n"
"/* ---------------------------- Managment stylnig "
                        "--------------------------- */\n"
"\n"
"#managementcontainer .QPushButton {\n"
"  background-color: transparent;\n"
"  height: 30px;\n"
"  font: 16pt \"Segoe UI\";\n"
"  color: #a9a9a9;\n"
"}\n"
"#managementcontainer .QPushButton:hover {\n"
"  color: #463755;\n"
"}\n"
"#managementcontainer .QPushButton:pressed {\n"
"  font: 15pt \"Segoe UI\";\n"
"  color: #a9a9a9;\n"
"}\n"
"\n"
"/* -------------------------------- Left Menu ------------------------------- */\n"
"#leftMenuBg {\n"
"  background-color: #121212;\n"
"}\n"
"#topLogo {\n"
"  background-color: #121212;\n"
"}\n"
"#titleLeftApp {\n"
"  font: 63 12pt \"Segoe UI Semibold\";\n"
"}\n"
"#titleLeftDescription {\n"
"  font: 8pt \"Segoe UI\";\n"
"  color: #bb86fc;\n"
"}\n"
"\n"
"/* ---------------------------------- MENUS --------------------------------- */\n"
"#topMenu .QPushButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 22px solid transparent;\n"
"  background-color: transparent;\n"
""
                        "  text-align: left;\n"
"  padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"  background-color: #18161b;\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"  background-color: #bb86fc;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 20px solid transparent;\n"
"  background-color: transparent;\n"
"  text-align: left;\n"
"  padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"  background-color: #18161b;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"  background-color: #bb86fc;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame {\n"
"  border-top: 3px solid #211c23;\n"
"}\n"
"\n"
"/* ------------------------------ Toggle Button ------------------------------ */\n"
"#toggleButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 20px solid transparent;\n"
"  text-align: left;\n"
""
                        "  padding-left: 44px;\n"
"  color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"  background-color: #18161b;\n"
"}\n"
"#toggleButton:pressed {\n"
"  background-color: #bb86fc;\n"
"}\n"
"\n"
"/* -------------------------------- Title Menu ------------------------------- */\n"
"#titleRightInfo {\n"
"  padding-left: 10px;\n"
"}\n"
"\n"
"/* -------------------------------- Extra Tab ------------------------------- */\n"
"#extraLeftBox {\n"
"  background-color: #211c23;\n"
"}\n"
"#extraTopBg {\n"
"  background-color: #bb86fc;\n"
"}\n"
"\n"
"/* ---------------------------------- Icon ---------------------------------- */\n"
"#extraIcon {\n"
"  background-position: center;\n"
"  background-repeat: no-repeat;\n"
"  background-image: url(:/icons/images/icons/cil-fire.png);\n"
"}\n"
"\n"
"/* ---------------------------------- Label --------------------------------- */\n"
"#extraLabel {\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* -------------------------------- Btn Close -------------------------------"
                        " */\n"
"#extraCloseColumnBtn {\n"
"  background-color: rgba(255, 255, 255, 0);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"}\n"
"#extraCloseColumnBtn:hover {\n"
"  background-color: rgb(196, 161, 249);\n"
"  border-style: solid;\n"
"  border-radius: 4px;\n"
"}\n"
"#extraCloseColumnBtn:pressed {\n"
"  background-color: rgb(180, 141, 238);\n"
"  border-style: solid;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"/* ------------------------------ Extra Content ----------------------------- */\n"
"#extraContent {\n"
"  border-top: 3px solid #18161b;\n"
"}\n"
"\n"
"/* ----------------------------- Extra Top Menus ---------------------------- */\n"
"#extraTopMenu .QPushButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 22px solid transparent;\n"
"  background-color: transparent;\n"
"  text-align: left;\n"
"  padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"  background-color: #18161b;\n"
"}\n"
"#extraTopMenu .QPushButton:pre"
                        "ssed {\n"
"  background-color: #bb86fc;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ------------------------------- Content App ------------------------------ */\n"
"#contentTopBg {\n"
"  background-color: #121212;\n"
"}\n"
"#contentBottom {\n"
"  border-top: 3px solid #211c23;\n"
"}\n"
"\n"
"/* ------------------------------- Top Buttons ------------------------------ */\n"
"#rightButtons .QPushButton {\n"
"  background-color: rgba(255, 255, 255, 0);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"}\n"
"#rightButtons .QPushButton:hover {\n"
"  background-color: rgb(44, 49, 57);\n"
"  border-style: solid;\n"
"  border-radius: 4px;\n"
"}\n"
"#rightButtons .QPushButton:pressed {\n"
"  background-color: rgb(23, 26, 30);\n"
"  border-style: solid;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"/* ----------------------------- Theme Settings ----------------------------- */\n"
"#extraRightBox {\n"
"  background-color: #211c23;\n"
"}\n"
"#themeSettingsTopDetail {\n"
"  background-color: #bb86fc;\n"
"}\n"
"\n"
"/*"
                        " ------------------------------- /Bottom Bar ------------------------------ */\n"
"#bottomBar {\n"
"  background-color: #211c23;\n"
"}\n"
"#bottomBar QLabel {\n"
"  font-size: 11px;\n"
"  color: rgb(113, 126, 149);\n"
"  padding-left: 10px;\n"
"  padding-right: 10px;\n"
"  padding-bottom: 2px;\n"
"}\n"
"\n"
"/* ---------------------------- CONTENT SETTINGS ---------------------------- */\n"
"/* --------------------------------- MENUS --------------------------------- */\n"
"#contentSettings .QPushButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 22px solid transparent;\n"
"  background-color: transparent;\n"
"  text-align: left;\n"
"  padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"  background-color: #18161b;\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"  background-color: #bb86fc;\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ------------------------------ QTableWidget -----------------------------"
                        "- */\n"
"QTableWidget {\n"
"  background-color: transparent;\n"
"  padding: 10px;\n"
"  border-radius: 5px;\n"
"  gridline-color: #211c23;\n"
"  border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item {\n"
"  border-color: rgb(44, 49, 60);\n"
"  padding-left: 5px;\n"
"  padding-right: 5px;\n"
"  gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected {\n"
"  background-color: #bb86fc;\n"
"}\n"
"QHeaderView::section {\n"
"	height:30px;\n"
"  background-color: #121212;\n"
"  max-width: 30px;\n"
"  border: 1px solid #211c23;\n"
"  border-style: none;\n"
"  border-bottom: 1px solid rgb(44, 49, 60);\n"
"  border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalheader {\n"
"  background-color: #121212;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"  border-color: rgb(44, 49, 60);\n"
"  gridline-color: rgb(44, 49, 60);\n"
"  padding: 3px;\n"
"  border-top-left-radius: 7px;\n"
"  border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical {\n"
"  border: 1px"
                        " solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* -------------------------------- LineEdit -------------------------------- */\n"
"QLineEdit {\n"
"  background-color: #121212;\n"
"  border-radius: 5px;\n"
"  border: 2px solid #121212;\n"
"  padding-left: 10px;\n"
"  selection-color: rgb(255, 255, 255);\n"
"  selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"  border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 2px solid #9976c2;\n"
"}\n"
"\n"
"/* ------------------------------ PlainTextEdit ----------------------------- */\n"
"QPlainTextEdit {\n"
"  background-color: rgb(27, 29, 35);\n"
"  border-radius: 5px;\n"
"  border: 2px solid #121212;\n"
"  padding: 10px;\n"
"  selection-color: rgb(255, 255, 255);\n"
"  selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit QScrollBar:vertical {\n"
"  width: 8px;\n"
"}\n"
"QPlainTextEdit QScrollBar:horizontal {\n"
"  height: 8px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"  border: 2px solid rgb(64, 71, 88);\n"
""
                        "}\n"
"QPlainTextEdit:focus {\n"
"  border: 2px solid #9976c2;\n"
"}\n"
"\n"
"/* ------------------------------- ScrollBars ------------------------------- */\n"
"QScrollBar:horizontal {\n"
"  border: none;\n"
"  background: rgb(52, 59, 72);\n"
"  height: 8px;\n"
"  margin: 0px 21px 0 21px;\n"
"  border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"  background: #bb86fc;\n"
"  min-width: 25px;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"  border: none;\n"
"  background: rgb(55, 63, 77);\n"
"  width: 20px;\n"
"  border-top-right-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"  border: none;\n"
"  background: rgb(55, 63, 77);\n"
"  width: 20px;\n"
"  border-top-left-radius: 4px;\n"
"  border-bottom-left-radius: 4px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:hor"
                        "izontal {\n"
"  background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"  border: none;\n"
"  background: rgb(52, 59, 72);\n"
"  width: 8px;\n"
"  margin: 21px 0 21px 0;\n"
"  border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"  background: #bb86fc;\n"
"  min-height: 25px;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"  border: none;\n"
"  background: rgb(55, 63, 77);\n"
"  height: 20px;\n"
"  border-bottom-left-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"  border: none;\n"
"  background: rgb(55, 63, 77);\n"
"  height: 20px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"  backgroun"
                        "d: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"/* -------------------------------- CheckBox -------------------------------- */\n"
"QCheckBox::indicator {\n"
"  border: 3px solid rgb(52, 59, 72);\n"
"  width: 15px;\n"
"  height: 15px;\n"
"  border-radius: 10px;\n"
"  background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"  border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"  background: 3px solid #9976c2;\n"
"  border: 3px solid rgb(52, 59, 72);\n"
"  background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* ------------------------------- RadioButton ------------------------------ */\n"
"QRadioButton::indicator {\n"
"  border: 3px solid rgb(52, 59, 72);\n"
"  width: 15px;\n"
"  height: 15px;\n"
"  border-radius: 10px;\n"
"  background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"  border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::in"
                        "dicator:checked {\n"
"  background: 3px solid #9976c2;\n"
"  border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* -------------------------------- ComboBox -------------------------------- */\n"
"QComboBox {\n"
"  background-color: rgb(27, 29, 35);\n"
"  border-radius: 5px;\n"
"  border: 2px solid #121212;\n"
"  padding: 5px;\n"
"  padding-left: 10px;\n"
"}\n"
"QComboBox:hover {\n"
"  border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 25px;\n"
"  border-left-width: 3px;\n"
"  border-left-color: rgba(39, 44, 54, 150);\n"
"  border-left-style: solid;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"  background-position: center;\n"
"  background-repeat: no-reperat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"  color: rgb(255, 121, 198);\n"
"  background-color: #121212;\n"
"  padding: 10px;\n"
"  selection-b"
                        "ackground-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* --------------------------------- Sliders -------------------------------- */\n"
"QSlider::groove:horizontal {\n"
"  border-radius: 5px;\n"
"  height: 10px;\n"
"  margin: 0px;\n"
"  background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"  background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"  background-color: #bb86fc;\n"
"  border: none;\n"
"  height: 10px;\n"
"  width: 10px;\n"
"  margin: 0px;\n"
"  border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"  background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"  background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"  border-radius: 5px;\n"
"  width: 10px;\n"
"  margin: 0px;\n"
"  background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"  background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"  background-color: #bb86fc;\n"
"  border:"
                        " none;\n"
"  height: 10px;\n"
"  width: 10px;\n"
"  margin: 0px;\n"
"  border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"  background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"  background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* ---------------------------- CommandLinkButton --------------------------- */\n"
"QCommandLinkButton {\n"
"  color: rgb(255, 121, 198);\n"
"  border-radius: 5px;\n"
"  padding: 5px;\n"
"  color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {\n"
"  color: rgb(255, 170, 255);\n"
"  background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"  color: #bb86fc;\n"
"  background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* --------------------------------- Button --------------------------------- */\n"
"#pagesContainer QPushButton {\n"
"  border: 2px solid rgb(52, 59, 72);\n"
"  border-radius: 5px;\n"
"  background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"  background-color: rgb("
                        "57, 65, 80);\n"
"  border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"  background-color: rgb(35, 40, 49);\n"
"  border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.leftMenuBg.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.topLogoInfo)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 4, 9, 9)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.topLogo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 42, 42))
        self.label_2.setMinimumSize(QSize(42, 42))
        self.label_2.setMaximumSize(QSize(42, 42))
        self.label_2.setPixmap(QPixmap(u":/images/LOGO_topbar.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.topLogo)

        self.topLogo_2 = QFrame(self.topLogoInfo)
        self.topLogo_2.setObjectName(u"topLogo_2")
        self.topLogo_2.setMinimumSize(QSize(0, 42))
        self.topLogo_2.setMaximumSize(QSize(140, 42))
        self.topLogo_2.setFrameShape(QFrame.NoFrame)
        self.topLogo_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.topLogo_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-10, 0, 140, 42))
        self.label_3.setPixmap(QPixmap(u":/images/viperEO.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.topLogo_2)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setMaximumSize(QSize(57, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_management = QPushButton(self.topMenu)
        self.btn_management.setObjectName(u"btn_management")
        sizePolicy.setHeightForWidth(self.btn_management.sizePolicy().hasHeightForWidth())
        self.btn_management.setSizePolicy(sizePolicy)
        self.btn_management.setMinimumSize(QSize(0, 45))
        self.btn_management.setFont(font)
        self.btn_management.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_management.setLayoutDirection(Qt.LeftToRight)
        self.btn_management.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-screen-desktop.png);")

        self.verticalLayout_8.addWidget(self.btn_management)

        self.btn_recognition = QPushButton(self.topMenu)
        self.btn_recognition.setObjectName(u"btn_recognition")
        sizePolicy.setHeightForWidth(self.btn_recognition.sizePolicy().hasHeightForWidth())
        self.btn_recognition.setSizePolicy(sizePolicy)
        self.btn_recognition.setMinimumSize(QSize(0, 45))
        self.btn_recognition.setFont(font)
        self.btn_recognition.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recognition.setLayoutDirection(Qt.LeftToRight)
        self.btn_recognition.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-voice-over-record.png);")

        self.verticalLayout_8.addWidget(self.btn_recognition)

        self.btn_detection = QPushButton(self.topMenu)
        self.btn_detection.setObjectName(u"btn_detection")
        sizePolicy.setHeightForWidth(self.btn_detection.sizePolicy().hasHeightForWidth())
        self.btn_detection.setSizePolicy(sizePolicy)
        self.btn_detection.setMinimumSize(QSize(0, 45))
        self.btn_detection.setFont(font)
        self.btn_detection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_detection.setLayoutDirection(Qt.LeftToRight)
        self.btn_detection.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);")

        self.verticalLayout_8.addWidget(self.btn_detection)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-fire.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 20)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_WEB = QPushButton(self.extraTopMenu)
        self.btn_WEB.setObjectName(u"btn_WEB")
        sizePolicy.setHeightForWidth(self.btn_WEB.sizePolicy().hasHeightForWidth())
        self.btn_WEB.setSizePolicy(sizePolicy)
        self.btn_WEB.setMinimumSize(QSize(0, 45))
        self.btn_WEB.setFont(font)
        self.btn_WEB.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_WEB.setLayoutDirection(Qt.LeftToRight)
        self.btn_WEB.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_WEB)

        self.btn_LinkedIn = QPushButton(self.extraTopMenu)
        self.btn_LinkedIn.setObjectName(u"btn_LinkedIn")
        sizePolicy.setHeightForWidth(self.btn_LinkedIn.sizePolicy().hasHeightForWidth())
        self.btn_LinkedIn.setSizePolicy(sizePolicy)
        self.btn_LinkedIn.setMinimumSize(QSize(0, 45))
        self.btn_LinkedIn.setFont(font)
        self.btn_LinkedIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_LinkedIn.setLayoutDirection(Qt.LeftToRight)
        self.btn_LinkedIn.setStyleSheet(u"background-image: url(:/mine/linkedIn.png);")

        self.verticalLayout_11.addWidget(self.btn_LinkedIn)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setMinimumSize(QSize(0, 240))
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.extraBottom)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.partnership = QLabel(self.extraBottom)
        self.partnership.setObjectName(u"partnership")
        self.partnership.setMinimumSize(QSize(230, 230))
        self.partnership.setMaximumSize(QSize(230, 230))
        self.partnership.setPixmap(QPixmap(u":/images/partnerShipv2.png"))
        self.partnership.setScaledContents(True)

        self.verticalLayout_22.addWidget(self.partnership)


        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.app_pages = QStackedWidget(self.pagesContainer)
        self.app_pages.setObjectName(u"app_pages")
        self.app_pages.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(u"background-image: url(:/images/logo_jst.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.app_pages.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 353, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.app_pages.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.app_pages.addWidget(self.new_page)
        self.management = QWidget()
        self.management.setObjectName(u"management")
        self.management.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.management)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(20, 0, 30, 0)
        self.menus = QFrame(self.management)
        self.menus.setObjectName(u"menus")
        self.menus.setMinimumSize(QSize(0, 40))
        self.menus.setMaximumSize(QSize(16777215, 40))
        self.menus.setStyleSheet(u"QFrame{border-bottom:1px solid #463755}\n"
"")
        self.menus.setFrameShape(QFrame.StyledPanel)
        self.menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.menus)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 0, 0, 0)
        self.managementcontainer = QFrame(self.menus)
        self.managementcontainer.setObjectName(u"managementcontainer")
        self.managementcontainer.setStyleSheet(u"QFrame{border:none}\n"
"QPushButton{\n"
"border:none;\n"
"border-bottom: 2px solid transparent;\n"
"border-radius:0px;\n"
"}")
        self.managementcontainer.setFrameShape(QFrame.StyledPanel)
        self.managementcontainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.managementcontainer)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_management_overall = QPushButton(self.managementcontainer)
        self.btn_management_overall.setObjectName(u"btn_management_overall")
        self.btn_management_overall.setStyleSheet(u"")
        self.btn_management_overall.setIconSize(QSize(16, 16))
        self.btn_management_overall.setAutoDefault(False)
        self.btn_management_overall.setFlat(False)

        self.horizontalLayout_8.addWidget(self.btn_management_overall)

        self.btn_management_add = QPushButton(self.managementcontainer)
        self.btn_management_add.setObjectName(u"btn_management_add")

        self.horizontalLayout_8.addWidget(self.btn_management_add)

        self.btn_management_delete = QPushButton(self.managementcontainer)
        self.btn_management_delete.setObjectName(u"btn_management_delete")

        self.horizontalLayout_8.addWidget(self.btn_management_delete)

        self.btn_management_update = QPushButton(self.managementcontainer)
        self.btn_management_update.setObjectName(u"btn_management_update")

        self.horizontalLayout_8.addWidget(self.btn_management_update)


        self.verticalLayout_25.addWidget(self.managementcontainer, 0, Qt.AlignLeft)


        self.verticalLayout_21.addWidget(self.menus)

        self.pagescontainer = QFrame(self.management)
        self.pagescontainer.setObjectName(u"pagescontainer")
        self.pagescontainer.setFrameShape(QFrame.StyledPanel)
        self.pagescontainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.pagescontainer)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.pagescontainer)
        self.pages.setObjectName(u"pages")
        self.management_overall = QWidget()
        self.management_overall.setObjectName(u"management_overall")
        self.verticalLayout_26 = QVBoxLayout(self.management_overall)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.overall_container = QFrame(self.management_overall)
        self.overall_container.setObjectName(u"overall_container")
        self.overall_container.setFrameShape(QFrame.StyledPanel)
        self.overall_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.overall_container)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.overall_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.table_overall = QTableWidget(self.frame_2)
        if (self.table_overall.columnCount() < 6):
            self.table_overall.setColumnCount(6)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_overall.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_overall.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_overall.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_overall.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_overall.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_overall.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        if (self.table_overall.rowCount() < 2):
            self.table_overall.setRowCount(2)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_overall.setVerticalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_overall.setItem(0, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_overall.setItem(0, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_overall.setItem(0, 2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_overall.setItem(0, 3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_overall.setItem(0, 4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_overall.setItem(0, 5, __qtablewidgetitem36)
        self.table_overall.setObjectName(u"table_overall")
        sizePolicy3.setHeightForWidth(self.table_overall.sizePolicy().hasHeightForWidth())
        self.table_overall.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.table_overall.setPalette(palette1)
        self.table_overall.setFrameShape(QFrame.NoFrame)
        self.table_overall.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_overall.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_overall.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_overall.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_overall.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_overall.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_overall.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_overall.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_overall.setShowGrid(True)
        self.table_overall.setGridStyle(Qt.SolidLine)
        self.table_overall.setSortingEnabled(False)
        self.table_overall.setRowCount(2)
        self.table_overall.horizontalHeader().setVisible(False)
        self.table_overall.horizontalHeader().setCascadingSectionResizes(True)
        self.table_overall.horizontalHeader().setMinimumSectionSize(0)
        self.table_overall.horizontalHeader().setDefaultSectionSize(200)
        self.table_overall.horizontalHeader().setStretchLastSection(True)
        self.table_overall.verticalHeader().setVisible(False)
        self.table_overall.verticalHeader().setCascadingSectionResizes(False)
        self.table_overall.verticalHeader().setMinimumSectionSize(25)
        self.table_overall.verticalHeader().setDefaultSectionSize(40)
        self.table_overall.verticalHeader().setHighlightSections(False)
        self.table_overall.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_10.addWidget(self.table_overall)


        self.verticalLayout_27.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.overall_container)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 70))
        self.frame_4.setMaximumSize(QSize(16777215, 70))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_4)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.btn_images = QPushButton(self.frame_4)
        self.btn_images.setObjectName(u"btn_images")
        self.btn_images.setMinimumSize(QSize(150, 30))
        self.btn_images.setFont(font)
        self.btn_images.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_images.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-image1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_images.setIcon(icon6)
        self.btn_images.setIconSize(QSize(12, 12))

        self.verticalLayout_39.addWidget(self.btn_images, 0, Qt.AlignLeft)

        self.error_overall = QLabel(self.frame_4)
        self.error_overall.setObjectName(u"error_overall")
        self.error_overall.setFont(font)
        self.error_overall.setStyleSheet(u"color:#c495fd;")

        self.verticalLayout_39.addWidget(self.error_overall)


        self.verticalLayout_27.addWidget(self.frame_4)


        self.verticalLayout_26.addWidget(self.overall_container)

        self.pages.addWidget(self.management_overall)
        self.management_images = QWidget()
        self.management_images.setObjectName(u"management_images")
        self.verticalLayout_41 = QVBoxLayout(self.management_images)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.images_container = QFrame(self.management_images)
        self.images_container.setObjectName(u"images_container")
        self.images_container.setFrameShape(QFrame.StyledPanel)
        self.images_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.images_container)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.images_container)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 30))
        self.frame_19.setMaximumSize(QSize(16777215, 30))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(10, 0, 0, 0)
        self.error_images = QLabel(self.frame_19)
        self.error_images.setObjectName(u"error_images")
        self.error_images.setFont(font)
        self.error_images.setStyleSheet(u"color:#c495fd;")

        self.horizontalLayout_18.addWidget(self.error_images, 0, Qt.AlignBottom)


        self.verticalLayout_43.addWidget(self.frame_19)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.row_4 = QFrame(self.images_container)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setMinimumSize(QSize(0, 149))
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.row_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setSizeConstraint(QLayout.SetMaximumSize)
        self.frame_17 = QFrame(self.row_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(300, 0))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_17)
        self.verticalLayout_44.setSpacing(20)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_17)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 100))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_24)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_27)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(5)
        self.gridLayout_6.setContentsMargins(50, 0, 50, -1)
        self.error_images_2 = QLabel(self.frame_27)
        self.error_images_2.setObjectName(u"error_images_2")
        self.error_images_2.setFont(font)
        self.error_images_2.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_6.addWidget(self.error_images_2, 0, 0, 1, 1, Qt.AlignBottom)

        self.labelLastname_image = QLabel(self.frame_27)
        self.labelLastname_image.setObjectName(u"labelLastname_image")
        self.labelLastname_image.setFont(font)
        self.labelLastname_image.setStyleSheet(u"color:#c495fd;")

        self.gridLayout_6.addWidget(self.labelLastname_image, 1, 1, 1, 1, Qt.AlignTop)

        self.error_images_4 = QLabel(self.frame_27)
        self.error_images_4.setObjectName(u"error_images_4")
        self.error_images_4.setFont(font)
        self.error_images_4.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout_6.addWidget(self.error_images_4, 1, 0, 1, 1, Qt.AlignTop)

        self.labelFirstname_image = QLabel(self.frame_27)
        self.labelFirstname_image.setObjectName(u"labelFirstname_image")
        self.labelFirstname_image.setFont(font)
        self.labelFirstname_image.setStyleSheet(u"color:#c495fd;")

        self.gridLayout_6.addWidget(self.labelFirstname_image, 0, 1, 1, 1, Qt.AlignBottom)


        self.verticalLayout_50.addLayout(self.gridLayout_6)


        self.horizontalLayout_21.addWidget(self.frame_27)


        self.verticalLayout_47.addWidget(self.frame_25)


        self.verticalLayout_44.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.frame_17)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(200, 0))
        self.frame_23.setMaximumSize(QSize(16777215, 16777215))
        self.frame_23.setSizeIncrement(QSize(4, 0))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_23)
        self.verticalLayout_45.setSpacing(20)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.btn_images_add = QPushButton(self.frame_23)
        self.btn_images_add.setObjectName(u"btn_images_add")
        self.btn_images_add.setMinimumSize(QSize(150, 30))
        self.btn_images_add.setFont(font)
        self.btn_images_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_images_add.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_images_add.setIcon(icon7)

        self.verticalLayout_45.addWidget(self.btn_images_add)

        self.btn_images_remove = QPushButton(self.frame_23)
        self.btn_images_remove.setObjectName(u"btn_images_remove")
        self.btn_images_remove.setMinimumSize(QSize(150, 30))
        self.btn_images_remove.setFont(font)
        self.btn_images_remove.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_images_remove.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-library-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_images_remove.setIcon(icon8)

        self.verticalLayout_45.addWidget(self.btn_images_remove)


        self.verticalLayout_44.addWidget(self.frame_23, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.gridLayout_20.addWidget(self.frame_17, 0, 1, 1, 1, Qt.AlignTop)

        self.table_images = QTableWidget(self.row_4)
        if (self.table_images.columnCount() < 2):
            self.table_images.setColumnCount(2)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_images.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_images.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        if (self.table_images.rowCount() < 16):
            self.table_images.setRowCount(16)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font2);
        self.table_images.setVerticalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(6, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(7, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(8, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(9, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(10, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(11, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(12, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(13, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(14, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.table_images.setVerticalHeaderItem(15, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.table_images.setItem(0, 0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.table_images.setItem(0, 1, __qtablewidgetitem56)
        self.table_images.setObjectName(u"table_images")
        sizePolicy3.setHeightForWidth(self.table_images.sizePolicy().hasHeightForWidth())
        self.table_images.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.table_images.setPalette(palette2)
        self.table_images.setFrameShape(QFrame.NoFrame)
        self.table_images.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_images.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_images.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_images.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_images.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_images.setShowGrid(True)
        self.table_images.setGridStyle(Qt.SolidLine)
        self.table_images.setSortingEnabled(False)
        self.table_images.horizontalHeader().setVisible(False)
        self.table_images.horizontalHeader().setCascadingSectionResizes(True)
        self.table_images.horizontalHeader().setMinimumSectionSize(0)
        self.table_images.horizontalHeader().setDefaultSectionSize(400)
        self.table_images.horizontalHeader().setStretchLastSection(True)
        self.table_images.verticalHeader().setVisible(False)
        self.table_images.verticalHeader().setCascadingSectionResizes(False)
        self.table_images.verticalHeader().setHighlightSections(False)
        self.table_images.verticalHeader().setStretchLastSection(True)

        self.gridLayout_20.addWidget(self.table_images, 0, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_20)


        self.gridLayout_17.addWidget(self.row_4, 0, 0, 1, 1)

        self.frame_18 = QFrame(self.images_container)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 0))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btn_images_back = QPushButton(self.frame_18)
        self.btn_images_back.setObjectName(u"btn_images_back")
        self.btn_images_back.setMinimumSize(QSize(150, 30))
        self.btn_images_back.setFont(font)
        self.btn_images_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_images_back.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_images_back.setIcon(icon9)
        self.btn_images_back.setIconSize(QSize(12, 12))

        self.horizontalLayout_19.addWidget(self.btn_images_back)


        self.gridLayout_17.addWidget(self.frame_18, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.frame_22 = QFrame(self.images_container)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.gridLayout_17.addWidget(self.frame_22, 2, 0, 1, 1)


        self.verticalLayout_43.addLayout(self.gridLayout_17)


        self.verticalLayout_41.addWidget(self.images_container)

        self.pages.addWidget(self.management_images)
        self.management_add = QWidget()
        self.management_add.setObjectName(u"management_add")
        self.verticalLayout_28 = QVBoxLayout(self.management_add)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.add_container = QFrame(self.management_add)
        self.add_container.setObjectName(u"add_container")
        self.add_container.setFrameShape(QFrame.StyledPanel)
        self.add_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.add_container)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.add_container)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setMaximumSize(QSize(16777215, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(250, 0, 0, 0)
        self.error_add = QLabel(self.frame_5)
        self.error_add.setObjectName(u"error_add")
        self.error_add.setFont(font)
        self.error_add.setStyleSheet(u"color:#c495fd;")

        self.horizontalLayout_14.addWidget(self.error_add, 0, Qt.AlignBottom)


        self.verticalLayout_29.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.add_container)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_7)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(250, 0, 300, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_8)
        self.verticalLayout_31.setSpacing(5)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_8 = QLabel(self.frame_8)
        self.labelVersion_8.setObjectName(u"labelVersion_8")
        self.labelVersion_8.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_8.setLineWidth(1)
        self.labelVersion_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelVersion_8, 0, 1, 1, 1)

        self.labelVersion_4 = QLabel(self.frame_8)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelVersion_4, 0, 0, 1, 1)

        self.add_firstname = QLineEdit(self.frame_8)
        self.add_firstname.setObjectName(u"add_firstname")
        self.add_firstname.setMinimumSize(QSize(0, 30))
        self.add_firstname.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.add_firstname, 1, 0, 1, 1)

        self.add_lastname = QLineEdit(self.frame_8)
        self.add_lastname.setObjectName(u"add_lastname")
        self.add_lastname.setMinimumSize(QSize(0, 30))
        self.add_lastname.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.add_lastname, 1, 1, 1, 1)


        self.verticalLayout_31.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.add_email = QLineEdit(self.frame_8)
        self.add_email.setObjectName(u"add_email")
        self.add_email.setMinimumSize(QSize(0, 30))
        self.add_email.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.add_email, 1, 0, 1, 1)

        self.labelVersion_5 = QLabel(self.frame_8)
        self.labelVersion_5.setObjectName(u"labelVersion_5")
        self.labelVersion_5.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_5.setLineWidth(1)
        self.labelVersion_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelVersion_5, 0, 0, 1, 1)


        self.verticalLayout_31.addLayout(self.gridLayout_4)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.add_phone = QLineEdit(self.frame_8)
        self.add_phone.setObjectName(u"add_phone")
        self.add_phone.setMinimumSize(QSize(0, 30))
        self.add_phone.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_8.addWidget(self.add_phone, 1, 0, 1, 1)

        self.labelVersion_10 = QLabel(self.frame_8)
        self.labelVersion_10.setObjectName(u"labelVersion_10")
        self.labelVersion_10.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_10.setLineWidth(1)
        self.labelVersion_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.labelVersion_10, 0, 0, 1, 1)


        self.verticalLayout_31.addLayout(self.gridLayout_8)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.add_adress = QPlainTextEdit(self.frame_8)
        self.add_adress.setObjectName(u"add_adress")
        self.add_adress.setMinimumSize(QSize(200, 100))
        self.add_adress.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_9.addWidget(self.add_adress, 1, 0, 1, 1)

        self.labelVersion_11 = QLabel(self.frame_8)
        self.labelVersion_11.setObjectName(u"labelVersion_11")
        self.labelVersion_11.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_11.setLineWidth(1)
        self.labelVersion_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.labelVersion_11, 0, 0, 1, 1)


        self.verticalLayout_31.addLayout(self.gridLayout_9)


        self.verticalLayout_30.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setSizeIncrement(QSize(0, 100))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.btn_add_submit = QPushButton(self.frame_6)
        self.btn_add_submit.setObjectName(u"btn_add_submit")
        self.btn_add_submit.setMinimumSize(QSize(150, 30))
        self.btn_add_submit.setFont(font)
        self.btn_add_submit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_submit.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_submit.setIcon(icon10)

        self.verticalLayout_32.addWidget(self.btn_add_submit, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_30.addWidget(self.frame_6)


        self.verticalLayout_29.addWidget(self.frame_7)


        self.verticalLayout_28.addWidget(self.add_container)

        self.pages.addWidget(self.management_add)
        self.management_delete = QWidget()
        self.management_delete.setObjectName(u"management_delete")
        self.verticalLayout_40 = QVBoxLayout(self.management_delete)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.management_delete)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 30))
        self.frame_16.setMaximumSize(QSize(16777215, 30))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(250, 0, 0, 0)
        self.error_delete = QLabel(self.frame_16)
        self.error_delete.setObjectName(u"error_delete")
        self.error_delete.setFont(font)
        self.error_delete.setStyleSheet(u"color:#c495fd;")

        self.horizontalLayout_16.addWidget(self.error_delete, 0, Qt.AlignBottom)


        self.verticalLayout_40.addWidget(self.frame_16)

        self.frame_13 = QFrame(self.management_delete)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_13)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(250, 0, 300, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_15)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setVerticalSpacing(10)
        self.btn_delete_remove = QPushButton(self.frame_15)
        self.btn_delete_remove.setObjectName(u"btn_delete_remove")
        self.btn_delete_remove.setMinimumSize(QSize(150, 30))
        self.btn_delete_remove.setFont(font)
        self.btn_delete_remove.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_remove.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-user-unfollow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_remove.setIcon(icon11)

        self.gridLayout_16.addWidget(self.btn_delete_remove, 1, 0, 1, 1, Qt.AlignHCenter)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(10)
        self.gridLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_18 = QLabel(self.frame_15)
        self.labelVersion_18.setObjectName(u"labelVersion_18")
        self.labelVersion_18.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_18.setLineWidth(1)
        self.labelVersion_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.labelVersion_18, 0, 0, 1, 1)

        self.delete_comboBox = QComboBox(self.frame_15)
        self.delete_comboBox.addItem("")
        self.delete_comboBox.addItem("")
        self.delete_comboBox.addItem("")
        self.delete_comboBox.setObjectName(u"delete_comboBox")
        self.delete_comboBox.setFont(font)
        self.delete_comboBox.setAutoFillBackground(False)
        self.delete_comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.delete_comboBox.setIconSize(QSize(16, 16))
        self.delete_comboBox.setFrame(True)

        self.gridLayout_15.addWidget(self.delete_comboBox, 1, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.verticalLayout_38.addLayout(self.gridLayout_16)


        self.horizontalLayout_17.addWidget(self.frame_15, 0, Qt.AlignTop)


        self.verticalLayout_37.addWidget(self.frame_14)


        self.verticalLayout_40.addWidget(self.frame_13)

        self.pages.addWidget(self.management_delete)
        self.management_update = QWidget()
        self.management_update.setObjectName(u"management_update")
        self.verticalLayout_36 = QVBoxLayout(self.management_update)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.management_update)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 30))
        self.frame_9.setMaximumSize(QSize(16777215, 30))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(250, 0, 0, 0)
        self.error_update = QLabel(self.frame_9)
        self.error_update.setObjectName(u"error_update")
        self.error_update.setFont(font)
        self.error_update.setStyleSheet(u"color:#c495fd;")

        self.horizontalLayout_15.addWidget(self.error_update, 0, Qt.AlignBottom)


        self.verticalLayout_36.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.management_update)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_10)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(250, 0, 300, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_11)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_17 = QLabel(self.frame_11)
        self.labelVersion_17.setObjectName(u"labelVersion_17")
        self.labelVersion_17.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_17.setLineWidth(1)
        self.labelVersion_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.labelVersion_17, 0, 0, 1, 1)

        self.update_comboBox = QComboBox(self.frame_11)
        self.update_comboBox.addItem("")
        self.update_comboBox.addItem("")
        self.update_comboBox.addItem("")
        self.update_comboBox.setObjectName(u"update_comboBox")
        self.update_comboBox.setFont(font)
        self.update_comboBox.setAutoFillBackground(False)
        self.update_comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.update_comboBox.setIconSize(QSize(16, 16))
        self.update_comboBox.setFrame(True)

        self.gridLayout_14.addWidget(self.update_comboBox, 1, 0, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_14)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setSpacing(10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_12 = QLabel(self.frame_11)
        self.labelVersion_12.setObjectName(u"labelVersion_12")
        self.labelVersion_12.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_12.setLineWidth(1)
        self.labelVersion_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.labelVersion_12, 0, 1, 1, 1)

        self.labelVersion_13 = QLabel(self.frame_11)
        self.labelVersion_13.setObjectName(u"labelVersion_13")
        self.labelVersion_13.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_13.setLineWidth(1)
        self.labelVersion_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.labelVersion_13, 0, 0, 1, 1)

        self.update_firstname = QLineEdit(self.frame_11)
        self.update_firstname.setObjectName(u"update_firstname")
        self.update_firstname.setMinimumSize(QSize(0, 30))
        self.update_firstname.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_10.addWidget(self.update_firstname, 1, 0, 1, 1)

        self.update_lastname = QLineEdit(self.frame_11)
        self.update_lastname.setObjectName(u"update_lastname")
        self.update_lastname.setMinimumSize(QSize(0, 30))
        self.update_lastname.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_10.addWidget(self.update_lastname, 1, 1, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_10)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.update_email = QLineEdit(self.frame_11)
        self.update_email.setObjectName(u"update_email")
        self.update_email.setMinimumSize(QSize(0, 30))
        self.update_email.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_11.addWidget(self.update_email, 1, 0, 1, 1)

        self.labelVersion_14 = QLabel(self.frame_11)
        self.labelVersion_14.setObjectName(u"labelVersion_14")
        self.labelVersion_14.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_14.setLineWidth(1)
        self.labelVersion_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.labelVersion_14, 0, 0, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_11)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.update_phone = QLineEdit(self.frame_11)
        self.update_phone.setObjectName(u"update_phone")
        self.update_phone.setMinimumSize(QSize(0, 30))
        self.update_phone.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_12.addWidget(self.update_phone, 1, 0, 1, 1)

        self.labelVersion_15 = QLabel(self.frame_11)
        self.labelVersion_15.setObjectName(u"labelVersion_15")
        self.labelVersion_15.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_15.setLineWidth(1)
        self.labelVersion_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.labelVersion_15, 0, 0, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_12)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_16 = QLabel(self.frame_11)
        self.labelVersion_16.setObjectName(u"labelVersion_16")
        self.labelVersion_16.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_16.setLineWidth(1)
        self.labelVersion_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.labelVersion_16, 0, 0, 1, 1)

        self.update_adress = QPlainTextEdit(self.frame_11)
        self.update_adress.setObjectName(u"update_adress")
        self.update_adress.setMinimumSize(QSize(200, 100))
        self.update_adress.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_13.addWidget(self.update_adress, 1, 0, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_13)


        self.verticalLayout_33.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 100))
        self.frame_12.setSizeIncrement(QSize(0, 100))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_12)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.btn_update_update = QPushButton(self.frame_12)
        self.btn_update_update.setObjectName(u"btn_update_update")
        self.btn_update_update.setMinimumSize(QSize(150, 30))
        self.btn_update_update.setFont(font)
        self.btn_update_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update_update.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-wrap-text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update_update.setIcon(icon12)

        self.verticalLayout_35.addWidget(self.btn_update_update, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_33.addWidget(self.frame_12)


        self.verticalLayout_36.addWidget(self.frame_10)

        self.pages.addWidget(self.management_update)

        self.verticalLayout_24.addWidget(self.pages)


        self.verticalLayout_21.addWidget(self.pagescontainer)

        self.app_pages.addWidget(self.management)
        self.recognition = QWidget()
        self.recognition.setObjectName(u"recognition")
        self.verticalLayout_42 = QVBoxLayout(self.recognition)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.recognition_container = QFrame(self.recognition)
        self.recognition_container.setObjectName(u"recognition_container")
        self.recognition_container.setFrameShape(QFrame.StyledPanel)
        self.recognition_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.recognition_container)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_26 = QFrame(self.recognition_container)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(20, 20, 20, 10)
        self.recognition_label = QLabel(self.frame_28)
        self.recognition_label.setObjectName(u"recognition_label")
        self.recognition_label.setStyleSheet(u"border-radius:50px;\n"
"")

        self.horizontalLayout_25.addWidget(self.recognition_label)


        self.horizontalLayout_22.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(300, 0))
        self.frame_29.setMaximumSize(QSize(300, 16777215))
        self.frame_29.setStyleSheet(u"QFrame{border-left:2px solid #211c23;}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_29)
        self.verticalLayout_49.setSpacing(10)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(-1, 10, 10, 10)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"QFrame{border-left:0px}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_30)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.frame_39 = QFrame(self.frame_30)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_39)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setVerticalSpacing(10)
        self.gridLayout_25.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_20 = QLabel(self.frame_39)
        self.labelVersion_20.setObjectName(u"labelVersion_20")
        self.labelVersion_20.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_20.setLineWidth(1)
        self.labelVersion_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.labelVersion_20, 0, 0, 1, 1)

        self.combobox_recognition_cam = QComboBox(self.frame_39)
        self.combobox_recognition_cam.addItem("")
        self.combobox_recognition_cam.addItem("")
        self.combobox_recognition_cam.addItem("")
        self.combobox_recognition_cam.setObjectName(u"combobox_recognition_cam")
        self.combobox_recognition_cam.setFont(font)
        self.combobox_recognition_cam.setAutoFillBackground(False)
        self.combobox_recognition_cam.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.combobox_recognition_cam.setIconSize(QSize(16, 16))
        self.combobox_recognition_cam.setFrame(True)

        self.gridLayout_25.addWidget(self.combobox_recognition_cam, 1, 0, 1, 1)


        self.verticalLayout_56.addLayout(self.gridLayout_25)


        self.gridLayout_24.addWidget(self.frame_39, 1, 0, 1, 2, Qt.AlignTop)

        self.btnRecognitionByCamera = QPushButton(self.frame_30)
        self.btnRecognitionByCamera.setObjectName(u"btnRecognitionByCamera")
        self.btnRecognitionByCamera.setMinimumSize(QSize(30, 30))
        self.btnRecognitionByCamera.setMaximumSize(QSize(50, 16777215))
        self.btnRecognitionByCamera.setFont(font)
        self.btnRecognitionByCamera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRecognitionByCamera.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon13 = QIcon()
        icon13.addFile(u":/mine/cam.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRecognitionByCamera.setIcon(icon13)

        self.gridLayout_24.addWidget(self.btnRecognitionByCamera, 2, 1, 1, 1)

        self.btnRecognitionByImage = QPushButton(self.frame_30)
        self.btnRecognitionByImage.setObjectName(u"btnRecognitionByImage")
        self.btnRecognitionByImage.setMinimumSize(QSize(30, 30))
        self.btnRecognitionByImage.setMaximumSize(QSize(50, 16777215))
        self.btnRecognitionByImage.setFont(font)
        self.btnRecognitionByImage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRecognitionByImage.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon14 = QIcon()
        icon14.addFile(u":/mine/C:/Users/Agent1/Downloads/symbole-d'interface-d'image-avec-un-paysage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRecognitionByImage.setIcon(icon14)

        self.gridLayout_24.addWidget(self.btnRecognitionByImage, 2, 0, 1, 1)


        self.verticalLayout_48.addLayout(self.gridLayout_24)


        self.verticalLayout_49.addWidget(self.frame_30)


        self.horizontalLayout_22.addWidget(self.frame_29)


        self.gridLayout_22.addWidget(self.frame_26, 0, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_22, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.recognition_container)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 100))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_21)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(10, 10, 10, 10)
        self.recognition_log = QPlainTextEdit(self.frame_21)
        self.recognition_log.setObjectName(u"recognition_log")
        self.recognition_log.setEnabled(False)
        self.recognition_log.setMinimumSize(QSize(0, 0))
        self.recognition_log.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_55.addWidget(self.recognition_log)


        self.gridLayout_19.addWidget(self.frame_21, 1, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_19, 1, 0, 1, 1)

        self.frame_20 = QFrame(self.recognition_container)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 30))
        self.frame_20.setMaximumSize(QSize(16777215, 30))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(15, 0, 0, 0)
        self.error_recognition = QLabel(self.frame_20)
        self.error_recognition.setObjectName(u"error_recognition")
        self.error_recognition.setFont(font)
        self.error_recognition.setStyleSheet(u"color:#c495fd;")

        self.horizontalLayout_20.addWidget(self.error_recognition, 0, Qt.AlignBottom)


        self.gridLayout_18.addWidget(self.frame_20, 2, 0, 1, 1)


        self.verticalLayout_46.addLayout(self.gridLayout_18)


        self.verticalLayout_42.addWidget(self.recognition_container)

        self.app_pages.addWidget(self.recognition)
        self.detection = QWidget()
        self.detection.setObjectName(u"detection")
        self.verticalLayout_54 = QVBoxLayout(self.detection)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.detection_container = QFrame(self.detection)
        self.detection_container.setObjectName(u"detection_container")
        self.detection_container.setFrameShape(QFrame.StyledPanel)
        self.detection_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.detection_container)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.frame_32 = QFrame(self.detection_container)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(300, 0))
        self.frame_34.setMaximumSize(QSize(300, 16777215))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_34)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(-1, 50, 50, 0)
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_35)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setVerticalSpacing(10)
        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setVerticalSpacing(10)
        self.gridLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_22 = QLabel(self.frame_35)
        self.labelVersion_22.setObjectName(u"labelVersion_22")
        self.labelVersion_22.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_22.setLineWidth(1)
        self.labelVersion_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_30.addWidget(self.labelVersion_22, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_35)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setFont(font)
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_3.setIconSize(QSize(16, 16))
        self.comboBox_3.setFrame(True)

        self.gridLayout_30.addWidget(self.comboBox_3, 1, 0, 1, 1)


        self.gridLayout_29.addLayout(self.gridLayout_30, 0, 0, 1, 1)

        self.delete_comboBox_5 = QComboBox(self.frame_35)
        self.delete_comboBox_5.addItem("")
        self.delete_comboBox_5.addItem("")
        self.delete_comboBox_5.addItem("")
        self.delete_comboBox_5.setObjectName(u"delete_comboBox_5")
        self.delete_comboBox_5.setFont(font)
        self.delete_comboBox_5.setAutoFillBackground(False)
        self.delete_comboBox_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.delete_comboBox_5.setIconSize(QSize(16, 16))
        self.delete_comboBox_5.setFrame(True)

        self.gridLayout_29.addWidget(self.delete_comboBox_5, 3, 0, 1, 1)

        self.labelVersion_23 = QLabel(self.frame_35)
        self.labelVersion_23.setObjectName(u"labelVersion_23")
        self.labelVersion_23.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_23.setLineWidth(1)
        self.labelVersion_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.labelVersion_23, 2, 0, 1, 1)

        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 30))
        self.frame_36.setMaximumSize(QSize(16777215, 30))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.gridLayout_29.addWidget(self.frame_36, 1, 0, 1, 1)


        self.verticalLayout_53.addLayout(self.gridLayout_29)


        self.verticalLayout_52.addWidget(self.frame_35, 0, Qt.AlignTop)


        self.horizontalLayout_23.addWidget(self.frame_34)


        self.gridLayout_28.addWidget(self.frame_32, 0, 0, 1, 1)


        self.gridLayout_27.addLayout(self.gridLayout_28, 0, 0, 1, 1)

        self.frame_37 = QFrame(self.detection_container)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(16777215, 100))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.gridLayout_27.addWidget(self.frame_37, 1, 0, 1, 1)


        self.gridLayout_26.addLayout(self.gridLayout_27, 1, 0, 1, 1)

        self.frame_38 = QFrame(self.detection_container)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 30))
        self.frame_38.setMaximumSize(QSize(16777215, 30))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.error_recognition_2 = QLabel(self.frame_38)
        self.error_recognition_2.setObjectName(u"error_recognition_2")
        self.error_recognition_2.setFont(font)
        self.error_recognition_2.setStyleSheet(u"color:#c495fd;")

        self.horizontalLayout_24.addWidget(self.error_recognition_2, 0, Qt.AlignBottom)


        self.gridLayout_26.addWidget(self.frame_38, 2, 0, 1, 1)


        self.verticalLayout_51.addLayout(self.gridLayout_26)


        self.verticalLayout_54.addWidget(self.detection_container)

        self.app_pages.addWidget(self.detection)

        self.verticalLayout_15.addWidget(self.app_pages)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.contentSettings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_3)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.labelBoxBlenderInstalation_3)


        self.verticalLayout_13.addWidget(self.frame_3)

        self.frame = QFrame(self.contentSettings)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(30, -1, -1, -1)
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setMaximumSize(QSize(50, 16777215))
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.labelBoxBlenderInstalation_2)

        self.darkmodeFrame = QFrame(self.frame)
        self.darkmodeFrame.setObjectName(u"darkmodeFrame")
        self.darkmodeFrame.setFrameShape(QFrame.StyledPanel)
        self.darkmodeFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.darkmodeFrame)


        self.verticalLayout_13.addWidget(self.frame)

        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignBottom)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(False)
        font3.setItalic(False)
        self.creditsLabel.setFont(font3)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.app_pages.setCurrentIndex(3)
        self.btn_management_overall.setDefault(False)
        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_management.setText(QCoreApplication.translate("MainWindow", u"Management", None))
        self.btn_recognition.setText(QCoreApplication.translate("MainWindow", u"Face recognition", None))
        self.btn_detection.setText(QCoreApplication.translate("MainWindow", u"Object detection", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btn_WEB.setText(QCoreApplication.translate("MainWindow", u"ViperEO's Site web", None))
        self.btn_LinkedIn.setText(QCoreApplication.translate("MainWindow", u"Creator", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Viper</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">EO</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An App created using Python , aiming to recognize a person by their face automatically, and detection objects using neural network.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Elbouchouki x Oumadane</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Face Recognition</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">opencv &amp; face detection librarie</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Object Detection</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-"
                        "size:9pt; color:#ffffff;\">YOLOv\u00a3 &amp; darknet neural network</span></p></body></html>", None))
        self.partnership.setText("")
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"ViperEO | PageName", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.btn_management_overall.setText(QCoreApplication.translate("MainWindow", u"Overall", None))
        self.btn_management_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_management_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_management_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        ___qtablewidgetitem24 = self.table_overall.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem25 = self.table_overall.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Firstname", None));
        ___qtablewidgetitem26 = self.table_overall.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Lastname", None));
        ___qtablewidgetitem27 = self.table_overall.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem28 = self.table_overall.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem29 = self.table_overall.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        ___qtablewidgetitem30 = self.table_overall.verticalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"header", None));

        __sortingEnabled1 = self.table_overall.isSortingEnabled()
        self.table_overall.setSortingEnabled(False)
        ___qtablewidgetitem31 = self.table_overall.item(0, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem32 = self.table_overall.item(0, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Firstname", None));
        ___qtablewidgetitem33 = self.table_overall.item(0, 2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Lastname", None));
        ___qtablewidgetitem34 = self.table_overall.item(0, 3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem35 = self.table_overall.item(0, 4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem36 = self.table_overall.item(0, 5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        self.table_overall.setSortingEnabled(__sortingEnabled1)

        self.btn_images.setText(QCoreApplication.translate("MainWindow", u"Pictures", None))
        self.error_overall.setText(QCoreApplication.translate("MainWindow", u"Something went wrong ...", None))
        self.error_images.setText(QCoreApplication.translate("MainWindow", u"Something went wrong ...", None))
        self.error_images_2.setText(QCoreApplication.translate("MainWindow", u"Firstname :", None))
        self.labelLastname_image.setText("")
        self.error_images_4.setText(QCoreApplication.translate("MainWindow", u"LastName :", None))
        self.labelFirstname_image.setText("")
        self.btn_images_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_images_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        ___qtablewidgetitem37 = self.table_images.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem38 = self.table_images.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"image", None));
        ___qtablewidgetitem39 = self.table_images.verticalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.table_images.verticalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.table_images.verticalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.table_images.verticalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem43 = self.table_images.verticalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem44 = self.table_images.verticalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem45 = self.table_images.verticalHeaderItem(6)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem46 = self.table_images.verticalHeaderItem(7)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem47 = self.table_images.verticalHeaderItem(8)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem48 = self.table_images.verticalHeaderItem(9)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem49 = self.table_images.verticalHeaderItem(10)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem50 = self.table_images.verticalHeaderItem(11)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem51 = self.table_images.verticalHeaderItem(12)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem52 = self.table_images.verticalHeaderItem(13)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem53 = self.table_images.verticalHeaderItem(14)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem54 = self.table_images.verticalHeaderItem(15)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.table_images.isSortingEnabled()
        self.table_images.setSortingEnabled(False)
        ___qtablewidgetitem55 = self.table_images.item(0, 0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem56 = self.table_images.item(0, 1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        self.table_images.setSortingEnabled(__sortingEnabled2)

        self.btn_images_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.error_add.setText(QCoreApplication.translate("MainWindow", u"Something went wrong ...", None))
        self.labelVersion_8.setText(QCoreApplication.translate("MainWindow", u"Lastname", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"Firstname", None))
        self.add_firstname.setText("")
        self.add_firstname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.add_lastname.setText("")
        self.add_lastname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.add_email.setText("")
        self.add_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"exemple@domain.com", None))
        self.labelVersion_5.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.add_phone.setText("")
        self.add_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelVersion_10.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.add_adress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type the adress ...", None))
        self.labelVersion_11.setText(QCoreApplication.translate("MainWindow", u"Adress", None))
        self.btn_add_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.error_delete.setText(QCoreApplication.translate("MainWindow", u"Something went wrong ...", None))
        self.btn_delete_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.labelVersion_18.setText(QCoreApplication.translate("MainWindow", u"Person", None))
        self.delete_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.delete_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.delete_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.error_update.setText(QCoreApplication.translate("MainWindow", u"Something went wrong ...", None))
        self.labelVersion_17.setText(QCoreApplication.translate("MainWindow", u"Person", None))
        self.update_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.update_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.update_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.labelVersion_12.setText(QCoreApplication.translate("MainWindow", u"Lastname", None))
        self.labelVersion_13.setText(QCoreApplication.translate("MainWindow", u"Firstname", None))
        self.update_firstname.setText("")
        self.update_firstname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.update_lastname.setText("")
        self.update_lastname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.update_email.setText("")
        self.update_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"exemple@domain.com", None))
        self.labelVersion_14.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.update_phone.setText("")
        self.update_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelVersion_15.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.labelVersion_16.setText(QCoreApplication.translate("MainWindow", u"Adress", None))
        self.update_adress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type the adress ...", None))
        self.btn_update_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.recognition_label.setText("")
        self.labelVersion_20.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.combobox_recognition_cam.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.combobox_recognition_cam.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.combobox_recognition_cam.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.btnRecognitionByCamera.setText("")
        self.btnRecognitionByImage.setText("")
        self.error_recognition.setText(QCoreApplication.translate("MainWindow", u"Something went wrong ...", None))
        self.labelVersion_22.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.delete_comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.delete_comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.delete_comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.labelVersion_23.setText(QCoreApplication.translate("MainWindow", u"Person", None))
        self.error_recognition_2.setText(QCoreApplication.translate("MainWindow", u"Something went wrong ...", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Preferences</span></p></body></html>", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#bd93f9;\">Dark Mode </span></p></body></html>", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"ViperEO \u00a9 2020 - 2021", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v2.1", None))
    # retranslateUi

