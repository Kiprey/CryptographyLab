# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrXVjYR.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1155, 763)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
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
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
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
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
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
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

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

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_fangshe = QPushButton(self.topMenu)
        self.btn_fangshe.setObjectName(u"btn_fangshe")
        sizePolicy.setHeightForWidth(self.btn_fangshe.sizePolicy().hasHeightForWidth())
        self.btn_fangshe.setSizePolicy(sizePolicy)
        self.btn_fangshe.setMinimumSize(QSize(0, 45))
        self.btn_fangshe.setFont(font)
        self.btn_fangshe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fangshe.setLayoutDirection(Qt.LeftToRight)
        self.btn_fangshe.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_fangshe)

        self.btn_liu = QPushButton(self.topMenu)
        self.btn_liu.setObjectName(u"btn_liu")
        sizePolicy.setHeightForWidth(self.btn_liu.sizePolicy().hasHeightForWidth())
        self.btn_liu.setSizePolicy(sizePolicy)
        self.btn_liu.setMinimumSize(QSize(0, 45))
        self.btn_liu.setFont(font)
        self.btn_liu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_liu.setLayoutDirection(Qt.LeftToRight)
        self.btn_liu.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_liu)

        self.btn_liu_2 = QPushButton(self.topMenu)
        self.btn_liu_2.setObjectName(u"btn_liu_2")
        sizePolicy.setHeightForWidth(self.btn_liu_2.sizePolicy().hasHeightForWidth())
        self.btn_liu_2.setSizePolicy(sizePolicy)
        self.btn_liu_2.setMinimumSize(QSize(0, 45))
        self.btn_liu_2.setFont(font)
        self.btn_liu_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_liu_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_liu_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_liu_2)

        self.btn_duichen = QPushButton(self.topMenu)
        self.btn_duichen.setObjectName(u"btn_duichen")
        sizePolicy.setHeightForWidth(self.btn_duichen.sizePolicy().hasHeightForWidth())
        self.btn_duichen.setSizePolicy(sizePolicy)
        self.btn_duichen.setMinimumSize(QSize(0, 45))
        self.btn_duichen.setFont(font)
        self.btn_duichen.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_duichen.setLayoutDirection(Qt.LeftToRight)
        self.btn_duichen.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_duichen)

        self.btn_feiduichen = QPushButton(self.topMenu)
        self.btn_feiduichen.setObjectName(u"btn_feiduichen")
        sizePolicy.setHeightForWidth(self.btn_feiduichen.sizePolicy().hasHeightForWidth())
        self.btn_feiduichen.setSizePolicy(sizePolicy)
        self.btn_feiduichen.setMinimumSize(QSize(0, 45))
        self.btn_feiduichen.setFont(font)
        self.btn_feiduichen.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_feiduichen.setLayoutDirection(Qt.LeftToRight)
        self.btn_feiduichen.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_feiduichen)

        self.btn_DH = QPushButton(self.topMenu)
        self.btn_DH.setObjectName(u"btn_DH")
        sizePolicy.setHeightForWidth(self.btn_DH.sizePolicy().hasHeightForWidth())
        self.btn_DH.setSizePolicy(sizePolicy)
        self.btn_DH.setMinimumSize(QSize(0, 45))
        self.btn_DH.setFont(font)
        self.btn_DH.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_DH.setLayoutDirection(Qt.LeftToRight)
        self.btn_DH.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_DH)

        self.btn_SSL = QPushButton(self.topMenu)
        self.btn_SSL.setObjectName(u"btn_SSL")
        sizePolicy.setHeightForWidth(self.btn_SSL.sizePolicy().hasHeightForWidth())
        self.btn_SSL.setSizePolicy(sizePolicy)
        self.btn_SSL.setMinimumSize(QSize(0, 45))
        self.btn_SSL.setFont(font)
        self.btn_SSL.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_SSL.setLayoutDirection(Qt.LeftToRight)
        self.btn_SSL.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_SSL)


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
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

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

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

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


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


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
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

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
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
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
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setMidLineWidth(-4)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 283, 218))
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
        font4 = QFont()
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
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
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
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

        self.stackedWidget.addWidget(self.widgets)
        self.fang_page = QWidget()
        self.fang_page.setObjectName(u"fang_page")
        self.verticalLayout_20 = QVBoxLayout(self.fang_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalWidget = QWidget(self.fang_page)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMinimumSize(QSize(0, 100))
        self.verticalLayout_33 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.plainTextEdit_13 = QPlainTextEdit(self.verticalWidget)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")
        self.plainTextEdit_13.setMaximumSize(QSize(16777215, 250))
        self.plainTextEdit_13.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_33.addWidget(self.plainTextEdit_13)


        self.verticalLayout_20.addWidget(self.verticalWidget)

        self.verticalWidget1 = QWidget(self.fang_page)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalLayout_31 = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalWidget = QWidget(self.verticalWidget1)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.plainTextEdit_15 = QPlainTextEdit(self.horizontalWidget)
        self.plainTextEdit_15.setObjectName(u"plainTextEdit_15")
        self.plainTextEdit_15.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_15.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_6.addWidget(self.plainTextEdit_15)

        self.verticalWidget2 = QWidget(self.horizontalWidget)
        self.verticalWidget2.setObjectName(u"verticalWidget2")
        self.verticalWidget2.setMinimumSize(QSize(200, 0))
        self.verticalLayout_32 = QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.lineEdit_5 = QLineEdit(self.verticalWidget2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_32.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.verticalWidget2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_32.addWidget(self.lineEdit_6)

        self.pushButton_8 = QPushButton(self.verticalWidget2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(200, 0))
        self.pushButton_8.setMaximumSize(QSize(201, 16777215))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_32.addWidget(self.pushButton_8, 0, Qt.AlignHCenter)

        self.pushButton_9 = QPushButton(self.verticalWidget2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(200, 0))
        self.pushButton_9.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_32.addWidget(self.pushButton_9, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.verticalWidget2)

        self.plainTextEdit_14 = QPlainTextEdit(self.horizontalWidget)
        self.plainTextEdit_14.setObjectName(u"plainTextEdit_14")
        self.plainTextEdit_14.setMaximumSize(QSize(16777215, 300))
        self.plainTextEdit_14.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_6.addWidget(self.plainTextEdit_14)


        self.verticalLayout_31.addWidget(self.horizontalWidget)


        self.verticalLayout_20.addWidget(self.verticalWidget1)

        self.label_3 = QLabel(self.fang_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.fang_page)
        self.liu_page = QWidget()
        self.liu_page.setObjectName(u"liu_page")
        self.verticalLayout_21 = QVBoxLayout(self.liu_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalWidget3 = QWidget(self.liu_page)
        self.verticalWidget3.setObjectName(u"verticalWidget3")
        self.verticalWidget3.setMaximumSize(QSize(16777215, 250))
        self.verticalLayout_29 = QVBoxLayout(self.verticalWidget3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.plainTextEdit_10 = QPlainTextEdit(self.verticalWidget3)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setMaximumSize(QSize(16777215, 200))
        self.plainTextEdit_10.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_29.addWidget(self.plainTextEdit_10)


        self.verticalLayout_21.addWidget(self.verticalWidget3)

        self.horizontalWidget1 = QWidget(self.liu_page)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.plainTextEdit_12 = QPlainTextEdit(self.horizontalWidget1)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_12.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_12.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_8.addWidget(self.plainTextEdit_12)

        self.verticalWidget4 = QWidget(self.horizontalWidget1)
        self.verticalWidget4.setObjectName(u"verticalWidget4")
        self.verticalWidget4.setMinimumSize(QSize(0, 0))
        self.verticalWidget4.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_30 = QVBoxLayout(self.verticalWidget4)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.plainTextEdit_18 = QPlainTextEdit(self.verticalWidget4)
        self.plainTextEdit_18.setObjectName(u"plainTextEdit_18")
        self.plainTextEdit_18.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_18.setMaximumSize(QSize(16777215, 200))
        self.plainTextEdit_18.setLayoutDirection(Qt.LeftToRight)
        self.plainTextEdit_18.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_30.addWidget(self.plainTextEdit_18)

        self.pushButton_7 = QPushButton(self.verticalWidget4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(200, 0))
        self.pushButton_7.setMaximumSize(QSize(200, 16777215))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_30.addWidget(self.pushButton_7, 0, Qt.AlignHCenter)

        self.pushButton_6 = QPushButton(self.verticalWidget4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(200, 0))
        self.pushButton_6.setMaximumSize(QSize(200, 16777215))
        self.pushButton_6.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_30.addWidget(self.pushButton_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.verticalWidget4)

        self.plainTextEdit_11 = QPlainTextEdit(self.horizontalWidget1)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_11.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_11.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_11.setLayoutDirection(Qt.LeftToRight)
        self.plainTextEdit_11.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_8.addWidget(self.plainTextEdit_11)


        self.verticalLayout_21.addWidget(self.horizontalWidget1)

        self.label = QLabel(self.liu_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label)

        self.stackedWidget.addWidget(self.liu_page)
        self.liu_2_page = QWidget()
        self.liu_2_page.setObjectName(u"liu_2_page")
        self.verticalLayout_34 = QVBoxLayout(self.liu_2_page)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalWidget5 = QWidget(self.liu_2_page)
        self.verticalWidget5.setObjectName(u"verticalWidget5")
        self.verticalWidget5.setMaximumSize(QSize(16777213, 250))
        self.verticalLayout_36 = QVBoxLayout(self.verticalWidget5)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.plainTextEdit_17 = QPlainTextEdit(self.verticalWidget5)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")
        self.plainTextEdit_17.setMaximumSize(QSize(16777215, 200))
        self.plainTextEdit_17.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_36.addWidget(self.plainTextEdit_17)


        self.verticalLayout_34.addWidget(self.verticalWidget5)

        self.horizontalWidget_2 = QWidget(self.liu_2_page)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.plainTextEdit_22 = QPlainTextEdit(self.horizontalWidget_2)
        self.plainTextEdit_22.setObjectName(u"plainTextEdit_22")
        self.plainTextEdit_22.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_22.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_15.addWidget(self.plainTextEdit_22)

        self.verticalWidget6 = QWidget(self.horizontalWidget_2)
        self.verticalWidget6.setObjectName(u"verticalWidget6")
        self.verticalWidget6.setMinimumSize(QSize(0, 0))
        self.verticalLayout_38 = QVBoxLayout(self.verticalWidget6)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.plainTextEdit_23 = QPlainTextEdit(self.verticalWidget6)
        self.plainTextEdit_23.setObjectName(u"plainTextEdit_23")
        self.plainTextEdit_23.setMaximumSize(QSize(16777215, 200))
        self.plainTextEdit_23.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_38.addWidget(self.plainTextEdit_23)

        self.pushButton_10 = QPushButton(self.verticalWidget6)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(200, 0))
        self.pushButton_10.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_38.addWidget(self.pushButton_10, 0, Qt.AlignHCenter)

        self.pushButton_11 = QPushButton(self.verticalWidget6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(200, 0))
        self.pushButton_11.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_38.addWidget(self.pushButton_11, 0, Qt.AlignHCenter)


        self.horizontalLayout_15.addWidget(self.verticalWidget6)

        self.plainTextEdit_21 = QPlainTextEdit(self.horizontalWidget_2)
        self.plainTextEdit_21.setObjectName(u"plainTextEdit_21")
        self.plainTextEdit_21.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_21.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_15.addWidget(self.plainTextEdit_21)


        self.verticalLayout_34.addWidget(self.horizontalWidget_2)

        self.label_6 = QLabel(self.liu_2_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.liu_2_page)
        self.duichen_page = QWidget()
        self.duichen_page.setObjectName(u"duichen_page")
        self.duichen_page.setMinimumSize(QSize(0, 150))
        self.verticalLayout_22 = QVBoxLayout(self.duichen_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalWidget7 = QWidget(self.duichen_page)
        self.verticalWidget7.setObjectName(u"verticalWidget7")
        self.verticalWidget7.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_26 = QVBoxLayout(self.verticalWidget7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.plainTextEdit_2 = QPlainTextEdit(self.verticalWidget7)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_26.addWidget(self.plainTextEdit_2)


        self.verticalLayout_22.addWidget(self.verticalWidget7)

        self.horizontalWidget2 = QWidget(self.duichen_page)
        self.horizontalWidget2.setObjectName(u"horizontalWidget2")
        self.horizontalWidget2.setMinimumSize(QSize(100, 300))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.plainTextEdit_4 = QPlainTextEdit(self.horizontalWidget2)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_7.addWidget(self.plainTextEdit_4)

        self.verticalWidget8 = QWidget(self.horizontalWidget2)
        self.verticalWidget8.setObjectName(u"verticalWidget8")
        self.verticalWidget8.setMaximumSize(QSize(200, 500))
        self.verticalLayout_27 = QVBoxLayout(self.verticalWidget8)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.lineEdit_2 = QLineEdit(self.verticalWidget8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_27.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.verticalWidget8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_27.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.verticalWidget8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_27.addWidget(self.pushButton_2)


        self.horizontalLayout_7.addWidget(self.verticalWidget8)

        self.plainTextEdit_3 = QPlainTextEdit(self.horizontalWidget2)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_7.addWidget(self.plainTextEdit_3)


        self.verticalLayout_22.addWidget(self.horizontalWidget2)

        self.label_2 = QLabel(self.duichen_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.duichen_page)
        self.feiduichen_page = QWidget()
        self.feiduichen_page.setObjectName(u"feiduichen_page")
        self.verticalLayout_23 = QVBoxLayout(self.feiduichen_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalWidget9 = QWidget(self.feiduichen_page)
        self.verticalWidget9.setObjectName(u"verticalWidget9")
        self.verticalWidget9.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_25 = QVBoxLayout(self.verticalWidget9)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.plainTextEdit_5 = QPlainTextEdit(self.verticalWidget9)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_5.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_25.addWidget(self.plainTextEdit_5)


        self.verticalLayout_23.addWidget(self.verticalWidget9)

        self.horizontalWidget3 = QWidget(self.feiduichen_page)
        self.horizontalWidget3.setObjectName(u"horizontalWidget3")
        self.gridLayout_3 = QGridLayout(self.horizontalWidget3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalWidget_3 = QWidget(self.horizontalWidget3)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.plainTextEdit_26 = QPlainTextEdit(self.horizontalWidget_3)
        self.plainTextEdit_26.setObjectName(u"plainTextEdit_26")
        self.plainTextEdit_26.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_26.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_26.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_19.addWidget(self.plainTextEdit_26)

        self.plainTextEdit_27 = QPlainTextEdit(self.horizontalWidget_3)
        self.plainTextEdit_27.setObjectName(u"plainTextEdit_27")
        self.plainTextEdit_27.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_27.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_27.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_19.addWidget(self.plainTextEdit_27)


        self.gridLayout_3.addWidget(self.horizontalWidget_3, 1, 2, 1, 1)

        self.horizontalWidget4 = QWidget(self.horizontalWidget3)
        self.horizontalWidget4.setObjectName(u"horizontalWidget4")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalWidget4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.plainTextEdit_25 = QPlainTextEdit(self.horizontalWidget4)
        self.plainTextEdit_25.setObjectName(u"plainTextEdit_25")
        self.plainTextEdit_25.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_25.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_25.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_17.addWidget(self.plainTextEdit_25)

        self.plainTextEdit_24 = QPlainTextEdit(self.horizontalWidget4)
        self.plainTextEdit_24.setObjectName(u"plainTextEdit_24")
        self.plainTextEdit_24.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_24.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_24.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_17.addWidget(self.plainTextEdit_24)


        self.gridLayout_3.addWidget(self.horizontalWidget4, 1, 0, 1, 1)

        self.plainTextEdit_6 = QPlainTextEdit(self.horizontalWidget3)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_6.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.plainTextEdit_6, 0, 0, 1, 1)

        self.verticalWidget10 = QWidget(self.horizontalWidget3)
        self.verticalWidget10.setObjectName(u"verticalWidget10")
        self.verticalWidget10.setMinimumSize(QSize(200, 0))
        self.verticalWidget10.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_28 = QVBoxLayout(self.verticalWidget10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.pushButton_25 = QPushButton(self.verticalWidget10)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_28.addWidget(self.pushButton_25)

        self.pushButton_5 = QPushButton(self.verticalWidget10)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_28.addWidget(self.pushButton_5)

        self.pushButton_15 = QPushButton(self.verticalWidget10)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_28.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.verticalWidget10)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_28.addWidget(self.pushButton_16)

        self.pushButton_4 = QPushButton(self.verticalWidget10)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_28.addWidget(self.pushButton_4)


        self.gridLayout_3.addWidget(self.verticalWidget10, 0, 1, 2, 1)

        self.plainTextEdit_7 = QPlainTextEdit(self.horizontalWidget3)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_7.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_7.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.plainTextEdit_7, 0, 2, 1, 1)


        self.verticalLayout_23.addWidget(self.horizontalWidget3)

        self.label_4 = QLabel(self.feiduichen_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.feiduichen_page)
        self.DH_page = QWidget()
        self.DH_page.setObjectName(u"DH_page")
        self.verticalLayout_24 = QVBoxLayout(self.DH_page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalWidget5 = QWidget(self.DH_page)
        self.horizontalWidget5.setObjectName(u"horizontalWidget5")
        self.horizontalWidget5.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalWidget5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalWidget11 = QWidget(self.horizontalWidget5)
        self.verticalWidget11.setObjectName(u"verticalWidget11")
        self.verticalWidget11.setMinimumSize(QSize(0, 0))
        self.verticalWidget11.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_35 = QVBoxLayout(self.verticalWidget11)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.plainTextEdit_16 = QPlainTextEdit(self.verticalWidget11)
        self.plainTextEdit_16.setObjectName(u"plainTextEdit_16")
        self.plainTextEdit_16.setMaximumSize(QSize(16777215, 400))
        self.plainTextEdit_16.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_35.addWidget(self.plainTextEdit_16)

        self.plainTextEdit_19 = QPlainTextEdit(self.verticalWidget11)
        self.plainTextEdit_19.setObjectName(u"plainTextEdit_19")
        self.plainTextEdit_19.setMaximumSize(QSize(16777215, 100))
        self.plainTextEdit_19.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_35.addWidget(self.plainTextEdit_19)


        self.horizontalLayout_10.addWidget(self.verticalWidget11)

        self.verticalWidget12 = QWidget(self.horizontalWidget5)
        self.verticalWidget12.setObjectName(u"verticalWidget12")
        self.verticalWidget12.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_40 = QVBoxLayout(self.verticalWidget12)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.plainTextEdit_20 = QPlainTextEdit(self.verticalWidget12)
        self.plainTextEdit_20.setObjectName(u"plainTextEdit_20")
        self.plainTextEdit_20.setMaximumSize(QSize(16777215, 300))
        self.plainTextEdit_20.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_40.addWidget(self.plainTextEdit_20)

        self.formWidget_2 = QWidget(self.verticalWidget12)
        self.formWidget_2.setObjectName(u"formWidget_2")
        self.formWidget_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_14 = QHBoxLayout(self.formWidget_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lineEdit_9 = QLineEdit(self.formWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(230, 0))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_14.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.formWidget_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_14.addWidget(self.lineEdit_10)


        self.verticalLayout_40.addWidget(self.formWidget_2)

        self.formWidget = QWidget(self.verticalWidget12)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_13 = QHBoxLayout(self.formWidget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_13 = QPushButton(self.formWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 20))
        self.pushButton_13.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_13.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.formWidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 20))
        self.pushButton_14.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_13.addWidget(self.pushButton_14)


        self.verticalLayout_40.addWidget(self.formWidget)

        self.pushButton_12 = QPushButton(self.verticalWidget12)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(200, 0))
        self.pushButton_12.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_12.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_40.addWidget(self.pushButton_12, 0, Qt.AlignHCenter)

        self.pushButton_44 = QPushButton(self.verticalWidget12)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setMinimumSize(QSize(200, 0))
        self.pushButton_44.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_44.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_40.addWidget(self.pushButton_44, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.verticalWidget12)


        self.verticalLayout_24.addWidget(self.horizontalWidget5)

        self.label_5 = QLabel(self.DH_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.DH_page)
        self.SSL_page = QWidget()
        self.SSL_page.setObjectName(u"SSL_page")
        self.verticalLayout_37 = QVBoxLayout(self.SSL_page)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalWidget_13 = QWidget(self.SSL_page)
        self.horizontalWidget_13.setObjectName(u"horizontalWidget_13")
        self.horizontalWidget_13.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_42 = QHBoxLayout(self.horizontalWidget_13)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalWidget_24 = QWidget(self.horizontalWidget_13)
        self.verticalWidget_24.setObjectName(u"verticalWidget_24")
        self.verticalWidget_24.setMinimumSize(QSize(0, 0))
        self.verticalWidget_24.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_76 = QVBoxLayout(self.verticalWidget_24)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.plainTextEdit_67 = QPlainTextEdit(self.verticalWidget_24)
        self.plainTextEdit_67.setObjectName(u"plainTextEdit_67")
        self.plainTextEdit_67.setMaximumSize(QSize(16777215, 400))
        self.plainTextEdit_67.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_76.addWidget(self.plainTextEdit_67)

        self.plainTextEdit_68 = QPlainTextEdit(self.verticalWidget_24)
        self.plainTextEdit_68.setObjectName(u"plainTextEdit_68")
        self.plainTextEdit_68.setMaximumSize(QSize(16777215, 100))
        self.plainTextEdit_68.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_76.addWidget(self.plainTextEdit_68)


        self.horizontalLayout_42.addWidget(self.verticalWidget_24)

        self.verticalWidget_25 = QWidget(self.horizontalWidget_13)
        self.verticalWidget_25.setObjectName(u"verticalWidget_25")
        self.verticalWidget_25.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_77 = QVBoxLayout(self.verticalWidget_25)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.plainTextEdit_69 = QPlainTextEdit(self.verticalWidget_25)
        self.plainTextEdit_69.setObjectName(u"plainTextEdit_69")
        self.plainTextEdit_69.setMaximumSize(QSize(16777215, 300))
        self.plainTextEdit_69.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_77.addWidget(self.plainTextEdit_69)

        self.formWidget_13 = QWidget(self.verticalWidget_25)
        self.formWidget_13.setObjectName(u"formWidget_13")
        self.formWidget_13.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_43 = QHBoxLayout(self.formWidget_13)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.lineEdit_21 = QLineEdit(self.formWidget_13)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(230, 0))
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_43.addWidget(self.lineEdit_21)

        self.lineEdit_22 = QLineEdit(self.formWidget_13)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_43.addWidget(self.lineEdit_22)


        self.verticalLayout_77.addWidget(self.formWidget_13)

        self.formWidget_14 = QWidget(self.verticalWidget_25)
        self.formWidget_14.setObjectName(u"formWidget_14")
        self.formWidget_14.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_44 = QHBoxLayout(self.formWidget_14)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.pushButton_47 = QPushButton(self.formWidget_14)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(0, 20))
        self.pushButton_47.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_44.addWidget(self.pushButton_47)

        self.pushButton_48 = QPushButton(self.formWidget_14)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(0, 20))
        self.pushButton_48.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_44.addWidget(self.pushButton_48)


        self.verticalLayout_77.addWidget(self.formWidget_14)

        self.pushButton_49 = QPushButton(self.verticalWidget_25)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMinimumSize(QSize(200, 0))
        self.pushButton_49.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_49.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_77.addWidget(self.pushButton_49, 0, Qt.AlignHCenter)

        self.pushButton_50 = QPushButton(self.verticalWidget_25)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMinimumSize(QSize(200, 0))
        self.pushButton_50.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_50.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.verticalLayout_77.addWidget(self.pushButton_50, 0, Qt.AlignHCenter)


        self.horizontalLayout_42.addWidget(self.verticalWidget_25)


        self.verticalLayout_37.addWidget(self.horizontalWidget_13)

        self.label_7 = QLabel(self.SSL_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.SSL_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


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


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


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
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
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
        self.pushButton_2.clicked.connect(MainWindow.DES_decrypt)
        self.pushButton_3.clicked.connect(MainWindow.DES_encrypt)
        self.pushButton_8.clicked.connect(MainWindow.Affine_encrypt)
        self.pushButton_9.clicked.connect(MainWindow.Affine_decrypt)
        self.pushButton_7.clicked.connect(MainWindow.RC4_encrypt)
        self.pushButton_6.clicked.connect(MainWindow.RC4_decrypt)
        self.pushButton_10.clicked.connect(MainWindow.RC4_encrypt)
        self.pushButton_11.clicked.connect(MainWindow.RC4_decrypt)
        self.pushButton_25.clicked.connect(MainWindow.RSA_gen_key)
        self.pushButton_5.clicked.connect(MainWindow.RSA_pubkey_encrypt)
        self.pushButton_15.clicked.connect(MainWindow.RSA_pubkey_decrypt)
        self.pushButton_16.clicked.connect(MainWindow.RSA_privkey_encrypt)
        self.pushButton_4.clicked.connect(MainWindow.RSA_pubkey_decrypt)
        self.pushButton_13.clicked.connect(MainWindow.DH_connect)
        self.pushButton_14.clicked.connect(MainWindow.DH_listen)
        self.pushButton_12.clicked.connect(MainWindow.DH_disconnect)
        self.pushButton_44.clicked.connect(MainWindow.DH_send)
        self.pushButton_47.clicked.connect(MainWindow.SSL_connect)
        self.pushButton_48.clicked.connect(MainWindow.SSL_listen)
        self.pushButton_49.clicked.connect(MainWindow.SSL_disconnect)
        self.pushButton_50.clicked.connect(MainWindow.SSL_send)

        self.stackedWidget.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Crypto Lab", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u89e3\u5bc6\u7b97\u6cd5\u7efc\u5408\u670d\u52a1\u7cfb\u7edf", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_fangshe.setText(QCoreApplication.translate("MainWindow", u"\u4eff\u5c04\u52a0\u5bc6", None))
        self.btn_liu.setText(QCoreApplication.translate("MainWindow", u"RC4\u52a0\u5bc6", None))
        self.btn_liu_2.setText(QCoreApplication.translate("MainWindow", u"LFSR\u52a0\u5bc6", None))
        self.btn_duichen.setText(QCoreApplication.translate("MainWindow", u"DES\u5bf9\u79f0\u52a0\u5bc6", None))
        self.btn_feiduichen.setText(QCoreApplication.translate("MainWindow", u"RSA\u975e\u5bf9\u79f0\u52a0\u5bc6", None))
        self.btn_DH.setText(QCoreApplication.translate("MainWindow", u"DH\u8ba4\u8bc1\u534f\u8bae\u4ee5\u53ca\u589e\u5f3a", None))
        self.btn_SSL.setText(QCoreApplication.translate("MainWindow", u"SSL\u6f14\u793a", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u4e2a\u52a0\u89e3\u5bc6\u7efc\u5408\u670d\u52a1\u83dc\u5355\u5f0f\u5c55\u793a\u754c\u9762,\u5305\u62ec\u591a\u79cd\u52a0\u5bc6\u7b97\u6cd5\u4ee5\u53ca\u534f\u8bae", None))
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

        self.plainTextEdit_13.setPlainText(QCoreApplication.translate("MainWindow", u"\u4eff\u5c04\u5bc6\u7801\u52a0\u5bc6/\u89e3\u5bc6\n"
"\u4eff\u5c04\u5bc6\u7801\u662f\u4e00\u79cd\u8868\u5355\u4ee3\u6362\u5bc6\u7801\uff0c\u5b57\u6bcd\u8868\u7684\u6bcf\u4e2a\u5b57\u6bcd\u76f8\u5e94\u7684\u503c\u4f7f\u7528\u4e00\u4e2a\u7b80\u5355\u7684\u6570\u5b66\u51fd\u6570\u5bf9\u5e94\u4e00\u4e2a\u6570\u503c\uff0c\u518d\u628a\u5bf9\u5e94\u6570\u503c\u8f6c\u6362\u6210\u5b57\u6bcd\u3002\n"
"\n"
"A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z\n"
"0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25\n"
"\u52a0\u5bc6\u51fd\u6570\uff1aE(x) = (ax + b) (mod m)\uff0c\u5176\u4e2d a\u4e0eb\u4e92\u8d28\uff0cm\u662f\u7f16\u7801\u7cfb\u7edf\u4e2d\u5b57\u6bcd\u7684\u4e2a\u6570\uff08\u901a\u5e38\u90fd\u662f26\uff09\u3002\n"
"\n"
"\u89e3\u5bc6\u51fd\u6570\uff1aD(x) = a^{-1} (x - b) (mod m)\uff0c\u5176\u4e2d a^{-1} \u662f a \u5728Z_{m}\u7fa4\u7684\u4e58\u6cd5\u9006\u5143\u3002", None))
        self.plainTextEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5f85\u52a0\u89e3\u5bc6\u5185\u5bb9", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u94a51, \u5fc5\u987b\u4e0e26\u4e92\u7d20", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u94a52, \u8303\u56f4\u5fc5\u987b\u4f4d\u4e8e [0, 26)", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u52a0  \u5bc6", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u89e3  \u5bc6", None))
        self.plainTextEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"result", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"fangshe", None))
        self.plainTextEdit_10.setPlainText(QCoreApplication.translate("MainWindow", u"RC4 \uf075 \u79cd\u5b50\u5bc6\u94a5\u53ef\u914d\u7f6e", None))
        self.plainTextEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5f85\u52a0\u89e3\u5bc6\u5185\u5bb9", None))
        self.plainTextEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"key", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"RC4 \u52a0  \u5bc6", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"RC4 \u89e3  \u5bc6", None))
        self.plainTextEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u6216\u8005\u89e3\u5bc6\u7684\u7ed3\u679c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RC4", None))
        self.plainTextEdit_17.setPlainText(QCoreApplication.translate("MainWindow", u"LSFR encryption \uf075	\u79cd\u5b50\u5bc6\u94a5\u53ef\u914d\u7f6e", None))
        self.plainTextEdit_17.setPlaceholderText("")
        self.plainTextEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5f85\u52a0\u89e3\u5bc6\u5185\u5bb9", None))
        self.plainTextEdit_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"key", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"LSFR \u52a0  \u5bc6", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"LSFR \u89e3  \u5bc6", None))
        self.plainTextEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u6216\u8005\u89e3\u5bc6\u7684\u7ed3\u679c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"LSFR", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"     DES\u52a0\u5bc6/\u89e3\u5bc6 \uf075\u52a0\u5bc6\u5bc6\u94a5\u53ef\u914d\u7f6e\n"
"\n"
"    3DES\uff08Triple Des\uff09\u52a0\u5bc6\u89e3\u5bc6\u5728\u7ebf\u5de5\u5177\u3002\u652f\u63013DES\u53cc\u500d\u548c\u4e09\u500d\u7684\u5bc6\u94a5\u3002\u5bc6\u94a5\u957f\u5ea6\u5206\u522b\u4e3a\u652f\u6301\u4e3a128/192\u4f4d\u3002\u53cc\u500d\u5bc6\u94a5\u53ef\u7528\u4e09\u500d\u5bc6\u94a5\u66ff\u6362\uff0c\u53cc\u500d\u5bc6\u94a5\u7684\u524d64\u4f4d+\u540e64\u4f4d+\u524d64\u4f4d\u7b49\u4e8e\u66ff\u4ee3\u7684\u4e09\u500d\u5bc6\u94a5\u3002\u5bc6\u94a5\u957f\u5ea6\u4e0d\u8db3\u65f6\uff0c\u5c06\u4ee50x00\u586b\u5145\u3002IV\u4e5f\u4e00\u6837\uff0c\u4ee5\u6b64\u65b9\u5f0f\u586b\u5145\u3002\u8d85\u51fa\u90e8\u5206\u5c06\u88ab\u5ffd\u7565\u3002\u5982\u679c\u6ca1\u6709\u7279\u522b\u6307\u660e\u5e73\u53f0\u5c06\u4f7f\u7528UTF8\u7f16\u7801\u5904\u7406\u6570\u636e\uff08\u5982KEY/IV\uff09\u3002\u672c\u5de5\u5177\u672a\u4f5c\u5168\u9762\u6d4b\u8bd5\uff0c\u5982\u679c\u53d1\u73b0\u95ee\u9898\u8bf7\u7ed9\u4e88\u53cd\u9988\u3002", None))
        self.plainTextEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9700\u8981\u52a0\u5bc6\u6216\u8005\u89e3\u5bc6\u7684\u5185\u5bb9", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u79d8\u94a5", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u5bc6", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u6216\u8005\u89e3\u5bc6\u7684\u7ed3\u679c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DES", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("MainWindow", u"RSA\u52a0\u5bc6\u7b97\u6cd5\u662f\u4e00\u79cd\u975e\u5bf9\u79f0\u52a0\u5bc6\u7b97\u6cd5\u3002\n"
"\n"
"\u52a0\u5bc6\u7684\u660e\u6587\u592a\u957f\u5219\u4f1a\u51fa\u9519\uff0c\u89e3\u51b3\u65b9\u6cd5\uff1a\u52a0\u5bc6\u7684\u65f6\u5019117\u4e2a\u5b57\u7b26\u52a0\u5bc6\u4e00\u6b21\uff0c\u7136\u540e\u628a\u6240\u6709\u7684\u5bc6\u6587\u62fc\u63a5\u6210\u4e00\u4e2a\u5bc6\u6587\uff1b\u89e3\u5bc6\u7684\u65f6\u5019\u9700\u8981128\u4e2a\u5b57\u7b26\u89e3\u5bc6\u4e00\u4e0b\uff0c\u7136\u540e\u62fc\u63a5\u6210\u6570\u636e\u3002", None))
        self.plainTextEdit_26.setPlaceholderText(QCoreApplication.translate("MainWindow", u"d \u79c1\u94a5\u4e4b\u4e00", None))
        self.plainTextEdit_27.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n \u79c1\u94a5\u4e4b\u4e00", None))
        self.plainTextEdit_25.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e \u516c\u94a5\u4e4b\u4e00", None))
        self.plainTextEdit_24.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n \u516c\u94a5\u4e4b\u4e00", None))
        self.plainTextEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u660e\u6587", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"RSA \u5bc6\u94a5\u751f\u6210", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"RSA \u516c\u94a5\u52a0\u5bc6", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"RSA \u516c\u94a5\u89e3\u5bc6", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"RSA \u79c1\u94a5\u52a0\u5bc6", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"RSA \u79c1\u94a5\u89e3\u5bc6", None))
        self.plainTextEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u6587", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"RSA", None))
        self.plainTextEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"output", None))
        self.plainTextEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input", None))
        self.plainTextEdit_20.setPlainText(QCoreApplication.translate("MainWindow", u"\uf06eD-H\u8ba4\u8bc1\u534f\u8bae\u53ca\u589e\u5f3a\n"
"\n"
"\uf075\u6709\u4e24\u4e2a\u53c2\u4e0e\u5b9e\u4f53(C/S\u6a21\u5f0f)\uff0c\u5fc5\u987b\u6709\u7f51\u7edc\u901a\u4fe1\u90e8\u5206\n"
"\n"
"\uf075\u5b9e\u73b0\u6d88\u606f\u5b8c\u6574\u6027\u9a8c\u8bc1\u53ca\u6765\u6e90\u9a8c\u8bc1\u7684\u589e\u5f3a\u8bbe\u8ba1\n"
"  \uf06c\u6563\u5217\u51fd\u6570SHA-1\u6216MD5\uff0c\u6570\u5b57\u7b7e\u540dRSA\n"
"", None))
        self.plainTextEdit_20.setPlaceholderText("")
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ip", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"port", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"connect", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"listen", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"refuse / stop connect", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"send", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DH", None))
        self.plainTextEdit_67.setPlaceholderText(QCoreApplication.translate("MainWindow", u"output", None))
        self.plainTextEdit_68.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input", None))
        self.plainTextEdit_69.setPlainText(QCoreApplication.translate("MainWindow", u"SSL ", None))
        self.plainTextEdit_69.setPlaceholderText("")
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ip", None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"port", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"connect", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"listen", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"refuse / stop connect", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"send", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SSL", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Wanderson M. Pimenta", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

