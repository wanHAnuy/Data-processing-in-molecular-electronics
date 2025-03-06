# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpinBox,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1487, 669)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
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
        self.gridLayout_5 = QGridLayout(self.styleSheet)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
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
        font1.setFamilies([u"Segoe UI Semibold"])
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
        font2.setFamilies([u"Segoe UI"])
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
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-fire.png)")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png)")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setToolTipDuration(0)
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-fingerprint.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_iv = QPushButton(self.topMenu)
        self.btn_iv.setObjectName(u"btn_iv")
        sizePolicy.setHeightForWidth(self.btn_iv.sizePolicy().hasHeightForWidth())
        self.btn_iv.setSizePolicy(sizePolicy)
        self.btn_iv.setMinimumSize(QSize(0, 45))
        self.btn_iv.setFont(font)
        self.btn_iv.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_iv.setLayoutDirection(Qt.LeftToRight)
        self.btn_iv.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-dog.png)")

        self.verticalLayout_8.addWidget(self.btn_iv)

        self.btn_psd = QPushButton(self.topMenu)
        self.btn_psd.setObjectName(u"btn_psd")
        self.btn_psd.setMinimumSize(QSize(0, 45))
        self.btn_psd.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-4k.png)")

        self.verticalLayout_8.addWidget(self.btn_psd)


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
        font3.setFamilies([u"Segoe UI"])
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
        self.verticalLayout_26 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(150, 0))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout_28 = QVBoxLayout(self.widgets)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.progressBar = QProgressBar(self.widgets)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 5))
        self.progressBar.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_28.addWidget(self.progressBar)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit = QLineEdit(self.widgets)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_9.addWidget(self.lineEdit)

        self.ivMode = QCheckBox(self.widgets)
        self.ivMode.setObjectName(u"ivMode")
        self.ivMode.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_9.addWidget(self.ivMode)

        self.open_file_button = QPushButton(self.widgets)
        self.open_file_button.setObjectName(u"open_file_button")
        self.open_file_button.setMinimumSize(QSize(80, 30))
        self.open_file_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_file_button.setAutoFillBackground(False)

        self.horizontalLayout_9.addWidget(self.open_file_button)

        self.choice_merge = QPushButton(self.widgets)
        self.choice_merge.setObjectName(u"choice_merge")
        self.choice_merge.setMinimumSize(QSize(80, 30))
        self.choice_merge.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.choice_merge)

        self.Redraw_Button = QPushButton(self.widgets)
        self.Redraw_Button.setObjectName(u"Redraw_Button")
        self.Redraw_Button.setMinimumSize(QSize(80, 30))
        self.Redraw_Button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.Redraw_Button)


        self.verticalLayout_28.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.clusters = QSpinBox(self.widgets)
        self.clusters.setObjectName(u"clusters")
        self.clusters.setMinimumSize(QSize(0, 30))
        self.clusters.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.clusters.setMinimum(2)
        self.clusters.setValue(4)

        self.gridLayout_2.addWidget(self.clusters, 4, 2, 1, 1)

        self.label_4 = QLabel(self.widgets)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.widgets)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.comboBox_3, 1, 2, 1, 1)

        self.single__savepushButton = QPushButton(self.widgets)
        self.single__savepushButton.setObjectName(u"single__savepushButton")
        self.single__savepushButton.setMinimumSize(QSize(0, 30))
        self.single__savepushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.single__savepushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.single__savepushButton, 1, 5, 1, 1)

        self.label_3 = QLabel(self.widgets)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.run = QPushButton(self.widgets)
        self.run.setObjectName(u"run")
        self.run.setMinimumSize(QSize(120, 30))
        self.run.setCursor(QCursor(Qt.PointingHandCursor))
        self.run.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.run, 2, 5, 1, 1)

        self.pushButton = QPushButton(self.widgets)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.pushButton, 7, 5, 1, 1)

        self.save = QPushButton(self.widgets)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(0, 30))
        self.save.setCursor(QCursor(Qt.PointingHandCursor))
        self.save.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.save, 4, 5, 1, 1)

        self.single_spinBox = QSpinBox(self.widgets)
        self.single_spinBox.setObjectName(u"single_spinBox")
        self.single_spinBox.setMinimumSize(QSize(0, 30))
        self.single_spinBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.single_spinBox.setMinimum(1)
        self.single_spinBox.setMaximum(99999)
        self.single_spinBox.setValue(1)

        self.gridLayout_2.addWidget(self.single_spinBox, 7, 2, 1, 1)

        self.label_6 = QLabel(self.widgets)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)

        self.comboBox = QComboBox(self.widgets)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.comboBox, 2, 2, 1, 1)

        self.single_runpushButton = QPushButton(self.widgets)
        self.single_runpushButton.setObjectName(u"single_runpushButton")
        self.single_runpushButton.setMinimumSize(QSize(0, 30))
        self.single_runpushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.single_runpushButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.single_runpushButton, 0, 5, 1, 1)

        self.label_10 = QLabel(self.widgets)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_2 = QLabel(self.widgets)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.widgets)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 30))
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_2.setIconSize(QSize(16, 16))
        self.comboBox_2.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox_2, 0, 2, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_2)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_52 = QLabel(self.widgets)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_16.addWidget(self.label_52)

        self.red_set = QSpinBox(self.widgets)
        self.red_set.setObjectName(u"red_set")
        self.red_set.setMaximum(10000000)
        self.red_set.setValue(2000)

        self.horizontalLayout_16.addWidget(self.red_set)

        self.checkBox = QCheckBox(self.widgets)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 30))
        self.checkBox.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_16.addWidget(self.checkBox)


        self.verticalLayout_23.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label = QLabel(self.widgets)
        self.label.setObjectName(u"label")

        self.horizontalLayout_13.addWidget(self.label)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_41 = QLabel(self.widgets)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_7.addWidget(self.label_41, 2, 4, 1, 1)

        self.lineEdit_10 = QLineEdit(self.widgets)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_7.addWidget(self.lineEdit_10, 2, 3, 1, 1)

        self.label_39 = QLabel(self.widgets)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_7.addWidget(self.label_39, 2, 2, 1, 1)

        self.lineEdit_8 = QLineEdit(self.widgets)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_7.addWidget(self.lineEdit_8, 0, 3, 1, 1)

        self.label_7 = QLabel(self.widgets)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widgets)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_7.addWidget(self.lineEdit_6, 1, 1, 1, 1)

        self.label_17 = QLabel(self.widgets)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_29 = QLabel(self.widgets)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_7.addWidget(self.label_29, 0, 4, 1, 1)

        self.lineEdit_12 = QLineEdit(self.widgets)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_7.addWidget(self.lineEdit_12, 1, 5, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widgets)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_7.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.label_22 = QLabel(self.widgets)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_7.addWidget(self.label_22, 1, 2, 1, 1)

        self.lineEdit_13 = QLineEdit(self.widgets)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_7.addWidget(self.lineEdit_13, 2, 5, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widgets)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_7.addWidget(self.lineEdit_7, 1, 3, 1, 1)

        self.lineEdit_11 = QLineEdit(self.widgets)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_7.addWidget(self.lineEdit_11, 0, 5, 1, 1)

        self.label_8 = QLabel(self.widgets)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.widgets)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_7.addWidget(self.lineEdit_9, 2, 1, 1, 1)

        self.label_30 = QLabel(self.widgets)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 1, 4, 1, 1)

        self.label_38 = QLabel(self.widgets)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_7.addWidget(self.label_38, 2, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_7)


        self.verticalLayout_23.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.widgets)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_50 = QLabel(self.widgets)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_8.addWidget(self.label_50, 0, 5, 1, 1)

        self.lineEdit_14 = QLineEdit(self.widgets)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_8.addWidget(self.lineEdit_14, 0, 1, 1, 1)

        self.label_51 = QLabel(self.widgets)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_8.addWidget(self.label_51, 1, 0, 1, 1)

        self.label_48 = QLabel(self.widgets)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_8.addWidget(self.label_48, 1, 2, 1, 1)

        self.label_49 = QLabel(self.widgets)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_8.addWidget(self.label_49, 0, 2, 1, 1)

        self.label_46 = QLabel(self.widgets)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_8.addWidget(self.label_46, 1, 4, 1, 1)

        self.label_47 = QLabel(self.widgets)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_8.addWidget(self.label_47, 0, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.widgets)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_8.addWidget(self.lineEdit_19, 1, 3, 1, 1)

        self.lineEdit_15 = QLineEdit(self.widgets)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_8.addWidget(self.lineEdit_15, 1, 1, 1, 1)

        self.lineEdit_18 = QLineEdit(self.widgets)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_8.addWidget(self.lineEdit_18, 1, 5, 1, 1)

        self.lineEdit_16 = QLineEdit(self.widgets)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_8.addWidget(self.lineEdit_16, 0, 3, 1, 1)

        self.label_53 = QLabel(self.widgets)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_8.addWidget(self.label_53, 0, 4, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_8)


        self.verticalLayout_23.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_23)


        self.verticalLayout_28.addLayout(self.horizontalLayout_12)

        self.scrollArea_2 = QScrollArea(self.widgets)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1449, 222))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_png2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_png2.setObjectName(u"label_png2")

        self.verticalLayout_22.addWidget(self.label_png2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_28.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_15 = QVBoxLayout(self.new_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.progressBar_3 = QProgressBar(self.new_page)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setMaximumSize(QSize(16777215, 5))
        self.progressBar_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.progressBar_3.setValue(0)
        self.progressBar_3.setTextVisible(False)

        self.verticalLayout_15.addWidget(self.progressBar_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_3 = QLineEdit(self.new_page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.lineEdit_3)

        self.open_file_button_3 = QPushButton(self.new_page)
        self.open_file_button_3.setObjectName(u"open_file_button_3")
        self.open_file_button_3.setMinimumSize(QSize(80, 30))
        self.open_file_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_file_button_3.setAutoFillBackground(False)

        self.horizontalLayout_11.addWidget(self.open_file_button_3)

        self.mergeSaveButton2 = QPushButton(self.new_page)
        self.mergeSaveButton2.setObjectName(u"mergeSaveButton2")
        self.mergeSaveButton2.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_11.addWidget(self.mergeSaveButton2)

        self.save_Button_3 = QPushButton(self.new_page)
        self.save_Button_3.setObjectName(u"save_Button_3")
        self.save_Button_3.setMinimumSize(QSize(80, 30))
        self.save_Button_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.save_Button_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.row_5 = QFrame(self.new_page)
        self.row_5.setObjectName(u"row_5")
        self.row_5.setMinimumSize(QSize(60, 30))
        self.row_5.setFrameShape(QFrame.StyledPanel)
        self.row_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.row_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(6)
        self.label_19 = QLabel(self.row_5)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_9.addWidget(self.label_19, 3, 0, 1, 1)

        self.label_21 = QLabel(self.row_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(150, 0))
        self.label_21.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_9.addWidget(self.label_21, 1, 0, 1, 1)

        self.color_style_1d = QComboBox(self.row_5)
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.addItem("")
        self.color_style_1d.setObjectName(u"color_style_1d")
        self.color_style_1d.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_style_1d.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_9.addWidget(self.color_style_1d, 1, 1, 1, 1)

        self.color_style_2d = QComboBox(self.row_5)
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.addItem("")
        self.color_style_2d.setObjectName(u"color_style_2d")
        self.color_style_2d.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_style_2d.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_9.addWidget(self.color_style_2d, 3, 1, 1, 1)

        self.label_12 = QLabel(self.row_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_9.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_20 = QLabel(self.row_5)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_9.addWidget(self.label_20, 0, 1, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_9)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_16 = QLabel(self.row_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(60, 30))

        self.gridLayout_16.addWidget(self.label_16, 1, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.row_5)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(60, 30))
        self.spinBox_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setValue(2)

        self.gridLayout_16.addWidget(self.spinBox_2, 3, 1, 1, 1)

        self.label_15 = QLabel(self.row_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(60, 30))

        self.gridLayout_16.addWidget(self.label_15, 3, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.row_5)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimumSize(QSize(60, 30))
        self.spinBox_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.spinBox_3.setMaximum(99999)
        self.spinBox_3.setValue(200)

        self.gridLayout_16.addWidget(self.spinBox_3, 1, 1, 1, 1)

        self.label_18 = QLabel(self.row_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_16.addWidget(self.label_18, 0, 0, 1, 1)

        self.div_clu_pushButton = QPushButton(self.row_5)
        self.div_clu_pushButton.setObjectName(u"div_clu_pushButton")
        self.div_clu_pushButton.setMinimumSize(QSize(60, 30))
        self.div_clu_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_16.addWidget(self.div_clu_pushButton, 3, 2, 1, 1)

        self.divide_pushButton = QPushButton(self.row_5)
        self.divide_pushButton.setObjectName(u"divide_pushButton")
        self.divide_pushButton.setMinimumSize(QSize(200, 30))
        self.divide_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_16.addWidget(self.divide_pushButton, 1, 2, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.row_5)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.doubleSpinBox.setMinimum(-9.000000000000000)
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.010000000000000)
        self.doubleSpinBox.setValue(-5.000000000000000)

        self.gridLayout_16.addWidget(self.doubleSpinBox, 0, 1, 1, 1)

        self.peak_pushButton = QPushButton(self.row_5)
        self.peak_pushButton.setObjectName(u"peak_pushButton")
        self.peak_pushButton.setMinimumSize(QSize(80, 30))
        self.peak_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_16.addWidget(self.peak_pushButton, 0, 2, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_16)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.run_cov_pushButton = QPushButton(self.row_5)
        self.run_cov_pushButton.setObjectName(u"run_cov_pushButton")
        self.run_cov_pushButton.setMinimumSize(QSize(80, 30))
        self.run_cov_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_12.addWidget(self.run_cov_pushButton, 1, 0, 1, 1)

        self.Peak_Subsection = QPushButton(self.row_5)
        self.Peak_Subsection.setObjectName(u"Peak_Subsection")
        self.Peak_Subsection.setMinimumSize(QSize(80, 30))
        self.Peak_Subsection.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_12.addWidget(self.Peak_Subsection, 2, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.row_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_17.addWidget(self.label_13)

        self.lineEdit_20 = QLineEdit(self.row_5)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.horizontalLayout_17.addWidget(self.lineEdit_20)


        self.gridLayout_12.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_12)


        self.gridLayout_6.addWidget(self.row_5, 0, 1, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_6)

        self.scrollArea = QScrollArea(self.new_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1367, 353))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_sub = QLabel(self.scrollAreaWidgetContents)
        self.label_sub.setObjectName(u"label_sub")

        self.verticalLayout_20.addWidget(self.label_sub)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.new_page)
        self.dl_page = QWidget()
        self.dl_page.setObjectName(u"dl_page")
        self.verticalLayout_16 = QVBoxLayout(self.dl_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.progressBar_4 = QProgressBar(self.dl_page)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setMinimumSize(QSize(800, 0))
        self.progressBar_4.setMaximumSize(QSize(16777215, 5))
        self.progressBar_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.progressBar_4.setValue(0)
        self.progressBar_4.setTextVisible(False)

        self.verticalLayout_16.addWidget(self.progressBar_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_4 = QLineEdit(self.dl_page)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_7.addWidget(self.lineEdit_4)

        self.open_file_button_4 = QPushButton(self.dl_page)
        self.open_file_button_4.setObjectName(u"open_file_button_4")
        self.open_file_button_4.setMinimumSize(QSize(80, 30))
        self.open_file_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_file_button_4.setAutoFillBackground(False)

        self.horizontalLayout_7.addWidget(self.open_file_button_4)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_2 = QLineEdit(self.dl_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.open_file_Button_6 = QPushButton(self.dl_page)
        self.open_file_Button_6.setObjectName(u"open_file_Button_6")
        self.open_file_Button_6.setMinimumSize(QSize(80, 30))
        self.open_file_Button_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.open_file_Button_6)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.single_find_pushButton = QPushButton(self.dl_page)
        self.single_find_pushButton.setObjectName(u"single_find_pushButton")
        self.single_find_pushButton.setMinimumSize(QSize(120, 30))
        self.single_find_pushButton.setMaximumSize(QSize(120, 30))
        self.single_find_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.single_find_pushButton, 3, 8, 1, 1)

        self.Correlation_find_pushButton = QPushButton(self.dl_page)
        self.Correlation_find_pushButton.setObjectName(u"Correlation_find_pushButton")
        self.Correlation_find_pushButton.setMinimumSize(QSize(120, 30))
        self.Correlation_find_pushButton.setMaximumSize(QSize(120, 30))
        self.Correlation_find_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Correlation_find_pushButton, 0, 8, 1, 1)

        self.Stable_sort_mean = QPushButton(self.dl_page)
        self.Stable_sort_mean.setObjectName(u"Stable_sort_mean")
        self.Stable_sort_mean.setMinimumSize(QSize(120, 30))
        self.Stable_sort_mean.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.Stable_sort_mean, 3, 4, 1, 1)

        self.label_40 = QLabel(self.dl_page)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(80, 30))
        self.label_40.setMaximumSize(QSize(999, 999))

        self.gridLayout.addWidget(self.label_40, 3, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.dl_page)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMinimumSize(QSize(80, 30))
        self.spinBox_6.setMaximumSize(QSize(999, 999))
        self.spinBox_6.setMinimum(0)
        self.spinBox_6.setMaximum(999)
        self.spinBox_6.setValue(2)

        self.gridLayout.addWidget(self.spinBox_6, 3, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.dl_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(120, 30))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)

        self.pushButton_3 = QPushButton(self.dl_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(120, 30))
        self.pushButton_3.setMaximumSize(QSize(120, 30))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_3, 3, 9, 1, 1)

        self.pushButton_2 = QPushButton(self.dl_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 30))
        self.pushButton_2.setMaximumSize(QSize(120, 30))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_2, 0, 9, 1, 1)

        self.label_11 = QLabel(self.dl_page)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 1)

        self.label_9 = QLabel(self.dl_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 30))

        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)

        self.spinBox = QSpinBox(self.dl_page)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(80, 30))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999999)
        self.spinBox.setValue(1)

        self.gridLayout.addWidget(self.spinBox, 3, 3, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.dl_page)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMinimumSize(QSize(80, 30))
        self.doubleSpinBox_3.setMaximum(1.000000000000000)
        self.doubleSpinBox_3.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_3, 0, 3, 1, 1)

        self.radioButton = QRadioButton(self.dl_page)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.dl_page)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout)

        self.scrollArea_7 = QScrollArea(self.dl_page)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setMaximumSize(QSize(99999, 99999))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1367, 350))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_42 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_17.addWidget(self.label_42)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_16.addWidget(self.scrollArea_7)

        self.label_23 = QLabel(self.dl_page)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_16.addWidget(self.label_23)

        self.stackedWidget.addWidget(self.dl_page)
        self.psd_page = QWidget()
        self.psd_page.setObjectName(u"psd_page")
        self.verticalLayout = QVBoxLayout(self.psd_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar_6 = QProgressBar(self.psd_page)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setMinimumSize(QSize(800, 0))
        self.progressBar_6.setMaximumSize(QSize(16777215, 5))
        self.progressBar_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.progressBar_6.setValue(0)
        self.progressBar_6.setTextVisible(False)

        self.verticalLayout.addWidget(self.progressBar_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_17 = QLineEdit(self.psd_page)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 30))
        self.lineEdit_17.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_10.addWidget(self.lineEdit_17)

        self.open_file_button_5 = QPushButton(self.psd_page)
        self.open_file_button_5.setObjectName(u"open_file_button_5")
        self.open_file_button_5.setMinimumSize(QSize(80, 30))
        self.open_file_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_file_button_5.setAutoFillBackground(False)

        self.horizontalLayout_10.addWidget(self.open_file_button_5)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.spinBox_15 = QSpinBox(self.psd_page)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setMinimumSize(QSize(0, 30))
        self.spinBox_15.setMaximum(10000)
        self.spinBox_15.setValue(30)

        self.gridLayout_10.addWidget(self.spinBox_15, 5, 3, 1, 1)

        self.label_66 = QLabel(self.psd_page)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_10.addWidget(self.label_66, 5, 0, 1, 1)

        self.spinBox_13 = QSpinBox(self.psd_page)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMinimumSize(QSize(0, 30))
        self.spinBox_13.setMinimum(1)
        self.spinBox_13.setMaximum(999)
        self.spinBox_13.setValue(20)

        self.gridLayout_10.addWidget(self.spinBox_13, 3, 7, 1, 1)

        self.spinBox_16 = QSpinBox(self.psd_page)
        self.spinBox_16.setObjectName(u"spinBox_16")
        self.spinBox_16.setMinimumSize(QSize(0, 30))
        self.spinBox_16.setMinimum(1)
        self.spinBox_16.setMaximum(10000)
        self.spinBox_16.setValue(30)

        self.gridLayout_10.addWidget(self.spinBox_16, 5, 1, 1, 1)

        self.spinBox_14 = QSpinBox(self.psd_page)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setMinimumSize(QSize(0, 30))
        self.spinBox_14.setMinimum(1)
        self.spinBox_14.setMaximum(999999999)

        self.gridLayout_10.addWidget(self.spinBox_14, 0, 7, 1, 1)

        self.label_60 = QLabel(self.psd_page)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_10.addWidget(self.label_60, 0, 4, 1, 1)

        self.label_61 = QLabel(self.psd_page)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_10.addWidget(self.label_61, 5, 2, 1, 1)

        self.label_59 = QLabel(self.psd_page)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_10.addWidget(self.label_59, 3, 4, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.psd_page)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox_2.setMinimum(-9.000000000000000)
        self.doubleSpinBox_2.setMaximum(9.000000000000000)
        self.doubleSpinBox_2.setValue(-5.000000000000000)

        self.gridLayout_10.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.psd_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(120, 30))

        self.gridLayout_10.addWidget(self.pushButton_4, 0, 9, 1, 1)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.psd_page)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")
        self.doubleSpinBox_16.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox_16.setMinimum(-9.000000000000000)
        self.doubleSpinBox_16.setMaximum(9.000000000000000)
        self.doubleSpinBox_16.setValue(-2.000000000000000)

        self.gridLayout_10.addWidget(self.doubleSpinBox_16, 3, 1, 1, 1)

        self.label_56 = QLabel(self.psd_page)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(80, 30))

        self.gridLayout_10.addWidget(self.label_56, 3, 2, 1, 1)

        self.spinBox_11 = QSpinBox(self.psd_page)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setMinimumSize(QSize(0, 30))
        self.spinBox_11.setMaximum(999999999)
        self.spinBox_11.setValue(3000)

        self.gridLayout_10.addWidget(self.spinBox_11, 0, 3, 1, 1)

        self.label_58 = QLabel(self.psd_page)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_10.addWidget(self.label_58, 0, 0, 1, 1)

        self.label_54 = QLabel(self.psd_page)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(80, 30))
        self.label_54.setMaximumSize(QSize(999, 999))

        self.gridLayout_10.addWidget(self.label_54, 3, 0, 1, 1)

        self.label_55 = QLabel(self.psd_page)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_10.addWidget(self.label_55, 0, 2, 1, 1)

        self.spinBox_12 = QSpinBox(self.psd_page)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setMinimumSize(QSize(80, 30))
        self.spinBox_12.setMinimum(1)
        self.spinBox_12.setMaximum(999999)
        self.spinBox_12.setValue(20000)

        self.gridLayout_10.addWidget(self.spinBox_12, 3, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.psd_page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(120, 30))
        self.pushButton_7.setMaximumSize(QSize(120, 30))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.pushButton_7, 5, 7, 1, 1)

        self.pushButton_6 = QPushButton(self.psd_page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(120, 30))

        self.gridLayout_10.addWidget(self.pushButton_6, 5, 9, 1, 1)

        self.Show_N_list = QPushButton(self.psd_page)
        self.Show_N_list.setObjectName(u"Show_N_list")
        self.Show_N_list.setMinimumSize(QSize(120, 30))
        self.Show_N_list.setMaximumSize(QSize(120, 30))
        self.Show_N_list.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.Show_N_list, 3, 9, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_10)

        self.scrollArea_8 = QScrollArea(self.psd_page)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setMaximumSize(QSize(99999, 99999))
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1367, 375))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_57 = QLabel(self.scrollAreaWidgetContents_8)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_19.addWidget(self.label_57)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout.addWidget(self.scrollArea_8)

        self.stackedWidget.addWidget(self.psd_page)
        self.IV_page = QWidget()
        self.IV_page.setObjectName(u"IV_page")
        self.IV_page.setEnabled(True)
        self.verticalLayout_27 = QVBoxLayout(self.IV_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.progressBar_5 = QProgressBar(self.IV_page)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setMinimumSize(QSize(800, 0))
        self.progressBar_5.setMaximumSize(QSize(16777215, 5))
        self.progressBar_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.progressBar_5.setValue(0)
        self.progressBar_5.setTextVisible(False)

        self.verticalLayout_27.addWidget(self.progressBar_5)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_iv = QLineEdit(self.IV_page)
        self.lineEdit_iv.setObjectName(u"lineEdit_iv")
        self.lineEdit_iv.setMinimumSize(QSize(0, 30))
        self.lineEdit_iv.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.lineEdit_iv, 0, 0, 1, 1)

        self.open_file_button_iv = QPushButton(self.IV_page)
        self.open_file_button_iv.setObjectName(u"open_file_button_iv")
        self.open_file_button_iv.setMinimumSize(QSize(80, 30))
        self.open_file_button_iv.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_file_button_iv.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.open_file_button_iv, 0, 2, 1, 1)

        self.run_file_button_iv = QPushButton(self.IV_page)
        self.run_file_button_iv.setObjectName(u"run_file_button_iv")
        self.run_file_button_iv.setMinimumSize(QSize(80, 30))
        self.run_file_button_iv.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_file_button_iv.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.run_file_button_iv, 0, 3, 1, 1)

        self.checkBox_2 = QCheckBox(self.IV_page)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_3.addWidget(self.checkBox_2, 0, 1, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_25 = QLabel(self.IV_page)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(80, 30))

        self.gridLayout_4.addWidget(self.label_25, 0, 4, 1, 1)

        self.label_27 = QLabel(self.IV_page)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(80, 30))

        self.gridLayout_4.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_24 = QLabel(self.IV_page)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(80, 30))

        self.gridLayout_4.addWidget(self.label_24, 1, 2, 1, 1)

        self.label_14 = QLabel(self.IV_page)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 1, 4, 1, 1)

        self.iv_cluster_way_test = QComboBox(self.IV_page)
        self.iv_cluster_way_test.addItem("")
        self.iv_cluster_way_test.addItem("")
        self.iv_cluster_way_test.addItem("")
        self.iv_cluster_way_test.addItem("")
        self.iv_cluster_way_test.setObjectName(u"iv_cluster_way_test")
        self.iv_cluster_way_test.setMinimumSize(QSize(0, 30))
        self.iv_cluster_way_test.setCursor(QCursor(Qt.PointingHandCursor))
        self.iv_cluster_way_test.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.iv_cluster_way_test, 0, 5, 1, 1)

        self.Chose_data_and_change_to_cluster_text = QComboBox(self.IV_page)
        self.Chose_data_and_change_to_cluster_text.addItem("")
        self.Chose_data_and_change_to_cluster_text.addItem("")
        self.Chose_data_and_change_to_cluster_text.addItem("")
        self.Chose_data_and_change_to_cluster_text.setObjectName(u"Chose_data_and_change_to_cluster_text")
        self.Chose_data_and_change_to_cluster_text.setMinimumSize(QSize(0, 30))
        self.Chose_data_and_change_to_cluster_text.setCursor(QCursor(Qt.PointingHandCursor))
        self.Chose_data_and_change_to_cluster_text.setAutoFillBackground(False)
        self.Chose_data_and_change_to_cluster_text.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.Chose_data_and_change_to_cluster_text.setIconSize(QSize(16, 16))
        self.Chose_data_and_change_to_cluster_text.setFrame(True)

        self.gridLayout_4.addWidget(self.Chose_data_and_change_to_cluster_text, 0, 3, 1, 1)

        self.label_28 = QLabel(self.IV_page)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(80, 30))

        self.gridLayout_4.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_26 = QLabel(self.IV_page)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(80, 30))

        self.gridLayout_4.addWidget(self.label_26, 0, 2, 1, 1)

        self.spinBox_4 = QSpinBox(self.IV_page)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimumSize(QSize(80, 30))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(999999)
        self.spinBox_4.setValue(1)

        self.gridLayout_4.addWidget(self.spinBox_4, 1, 5, 1, 1)

        self.spinBox_7 = QSpinBox(self.IV_page)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMinimumSize(QSize(80, 30))
        self.spinBox_7.setMaximumSize(QSize(999, 999))
        self.spinBox_7.setMinimum(0)
        self.spinBox_7.setMaximum(999)
        self.spinBox_7.setValue(2)

        self.gridLayout_4.addWidget(self.spinBox_7, 1, 1, 1, 1)

        self.label_33 = QLabel(self.IV_page)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_4.addWidget(self.label_33, 2, 4, 1, 1)

        self.Chose_data_text = QComboBox(self.IV_page)
        self.Chose_data_text.addItem("")
        self.Chose_data_text.addItem("")
        self.Chose_data_text.addItem("")
        self.Chose_data_text.addItem("")
        self.Chose_data_text.addItem("")
        self.Chose_data_text.addItem("")
        self.Chose_data_text.addItem("")
        self.Chose_data_text.addItem("")
        self.Chose_data_text.setObjectName(u"Chose_data_text")
        self.Chose_data_text.setCursor(QCursor(Qt.PointingHandCursor))
        self.Chose_data_text.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.Chose_data_text, 0, 1, 1, 1)

        self.label_31 = QLabel(self.IV_page)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_4.addWidget(self.label_31, 2, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.IV_page)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMinimumSize(QSize(80, 30))
        self.spinBox_5.setMaximum(1000)
        self.spinBox_5.setValue(15)

        self.gridLayout_4.addWidget(self.spinBox_5, 1, 3, 1, 1)

        self.label_32 = QLabel(self.IV_page)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_4.addWidget(self.label_32, 2, 2, 1, 1)

        self.spinBox_8 = QSpinBox(self.IV_page)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMinimumSize(QSize(0, 30))
        self.spinBox_8.setMaximum(9999)
        self.spinBox_8.setValue(120)

        self.gridLayout_4.addWidget(self.spinBox_8, 3, 1, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox_5.setMinimum(-99.000000000000000)
        self.doubleSpinBox_5.setSingleStep(0.100000000000000)
        self.doubleSpinBox_5.setValue(-2.500000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_5, 2, 3, 1, 1)

        self.spinBox_10 = QSpinBox(self.IV_page)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setMinimumSize(QSize(0, 30))
        self.spinBox_10.setMaximum(999999999)
        self.spinBox_10.setValue(10000)

        self.gridLayout_4.addWidget(self.spinBox_10, 3, 5, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox_4.setMinimum(-10.000000000000000)
        self.doubleSpinBox_4.setMaximum(10.000000000000000)
        self.doubleSpinBox_4.setSingleStep(0.100000000000000)
        self.doubleSpinBox_4.setValue(0.100000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_4, 2, 1, 1, 1)

        self.spinBox_9 = QSpinBox(self.IV_page)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMinimumSize(QSize(0, 30))
        self.spinBox_9.setMaximum(99999)
        self.spinBox_9.setValue(80)

        self.gridLayout_4.addWidget(self.spinBox_9, 3, 3, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox_6.setMinimum(-99.000000000000000)
        self.doubleSpinBox_6.setSingleStep(0.100000000000000)
        self.doubleSpinBox_6.setValue(-5.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_6, 2, 5, 1, 1)

        self.Single_pre_iv = QPushButton(self.IV_page)
        self.Single_pre_iv.setObjectName(u"Single_pre_iv")
        self.Single_pre_iv.setMinimumSize(QSize(120, 30))
        self.Single_pre_iv.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.Single_pre_iv, 0, 10, 1, 1)

        self.saveall_iv = QPushButton(self.IV_page)
        self.saveall_iv.setObjectName(u"saveall_iv")
        self.saveall_iv.setMinimumSize(QSize(120, 30))
        self.saveall_iv.setMaximumSize(QSize(120, 30))
        self.saveall_iv.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.saveall_iv, 3, 10, 1, 1)

        self.Draw_his_iv = QPushButton(self.IV_page)
        self.Draw_his_iv.setObjectName(u"Draw_his_iv")
        self.Draw_his_iv.setMinimumSize(QSize(120, 30))
        self.Draw_his_iv.setMaximumSize(QSize(120, 30))
        self.Draw_his_iv.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.Draw_his_iv, 1, 10, 1, 1)

        self.Cluster_run_iv = QPushButton(self.IV_page)
        self.Cluster_run_iv.setObjectName(u"Cluster_run_iv")
        self.Cluster_run_iv.setMinimumSize(QSize(120, 30))
        self.Cluster_run_iv.setMaximumSize(QSize(120, 30))
        self.Cluster_run_iv.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.Cluster_run_iv, 2, 10, 1, 1)

        self.label_35 = QLabel(self.IV_page)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_4.addWidget(self.label_35, 3, 2, 1, 1)

        self.label_36 = QLabel(self.IV_page)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_4.addWidget(self.label_36, 3, 4, 1, 1)

        self.label_34 = QLabel(self.IV_page)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_4.addWidget(self.label_34, 3, 0, 1, 1)

        self.label_43 = QLabel(self.IV_page)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_4.addWidget(self.label_43, 0, 6, 1, 1)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setMinimum(-99.000000000000000)
        self.doubleSpinBox_8.setValue(-3.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_8, 0, 8, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setMinimum(-99.000000000000000)
        self.doubleSpinBox_7.setSingleStep(1.000000000000000)
        self.doubleSpinBox_7.setValue(3.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_7, 0, 9, 1, 1)

        self.label_44 = QLabel(self.IV_page)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_4.addWidget(self.label_44, 1, 6, 1, 1)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")
        self.doubleSpinBox_10.setMinimum(-99.000000000000000)
        self.doubleSpinBox_10.setValue(-8.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_10, 1, 8, 1, 1)

        self.label_45 = QLabel(self.IV_page)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_4.addWidget(self.label_45, 2, 6, 1, 1)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setMinimum(-33.000000000000000)
        self.doubleSpinBox_11.setValue(-7.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_11, 2, 8, 1, 1)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")
        self.doubleSpinBox_9.setMinimum(-99.000000000000000)
        self.doubleSpinBox_9.setValue(0.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_9, 1, 9, 1, 1)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")
        self.doubleSpinBox_12.setMinimum(-99.000000000000000)
        self.doubleSpinBox_12.setSingleStep(1.000000000000000)
        self.doubleSpinBox_12.setValue(-1.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_12, 2, 9, 1, 1)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")
        self.doubleSpinBox_14.setMinimum(-99.000000000000000)
        self.doubleSpinBox_14.setMaximum(99999999.000000000000000)
        self.doubleSpinBox_14.setValue(100.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_14, 3, 9, 1, 1)

        self.label_37 = QLabel(self.IV_page)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_4.addWidget(self.label_37, 3, 6, 1, 1)

        self.doubleSpinBox_13 = QDoubleSpinBox(self.IV_page)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")
        self.doubleSpinBox_13.setMinimum(-99999999.000000000000000)
        self.doubleSpinBox_13.setValue(-100.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_13, 3, 8, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_4)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.scrollArea_5 = QScrollArea(self.IV_page)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1365, 334))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_iv = QLabel(self.scrollAreaWidgetContents_5)
        self.label_iv.setObjectName(u"label_iv")

        self.verticalLayout_25.addWidget(self.label_iv)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_18.addWidget(self.scrollArea_5)


        self.verticalLayout_27.addLayout(self.verticalLayout_18)

        self.stackedWidget.addWidget(self.IV_page)

        self.verticalLayout_26.addWidget(self.stackedWidget)


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
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
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


        self.gridLayout_5.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(2)
        self.Chose_data_and_change_to_cluster_text.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Injunction", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Data processing APP", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home page", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Cluster cacu", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"Subsection cacu", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Find trance", None))
        self.btn_iv.setText(QCoreApplication.translate("MainWindow", u"IV analyse", None))
        self.btn_psd.setText(QCoreApplication.translate("MainWindow", u"PSD", None))
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
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha, and the source of UI created by Wanderson M. Pimenta.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; marg"
                        "in-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Application Created by: Wang Haoyu</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span"
                        "></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Injunction - Dedicated to molecular electronics", None))
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
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Common cluster analysis, drag to enter the address, the file format is single_trance.npz", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.ivMode.setText(QCoreApplication.translate("MainWindow", u"IV MODE", None))
        self.open_file_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.choice_merge.setText(QCoreApplication.translate("MainWindow", u"Merge Save", None))
        self.Redraw_Button.setText(QCoreApplication.translate("MainWindow", u"Redraw", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cluster num(or max num for find):", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"No dimensionality reduction\uff08just for kmeans\uff09", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"t-SNE", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"PCA", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"UMAP", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"MPVC(lemmers)", None))

        self.single__savepushButton.setText(QCoreApplication.translate("MainWindow", u"Single save", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select cluster type:", None))
        self.run.setText(QCoreApplication.translate("MainWindow", u"Clustering run", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CH_scan", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Clustering save", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Select a curve(same as Single_trace):", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Kmeans\uff08Recommended\uff09", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Gaussian Mixture Model", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"KShape", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"TimeSeriesKMeans\uff08Recommended\uff09", None))

        self.single_runpushButton.setText(QCoreApplication.translate("MainWindow", u"Single preview", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dimensionality reduction:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Single curve data preprocessing method:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Raw data", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Tailor data", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Tailor & 1 D HIS (recommended)", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Tailor & 2 D HIS", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Tailor data & interpolation", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Tailor data & interpolation & length", None))

        self.label_52.setText(QCoreApplication.translate("MainWindow", u"2D max", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Finished once and want to use the class on other", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Polt Figure \n"
"parameter", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"bin:", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"1.2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Distance from", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"-6.5", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"bin:", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"120", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"-0.2", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"180", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Conductance from", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"bin:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Length from", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Preprocess \n"
"parameter", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"with con  ", None))
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Conductance from", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"bin:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Distance from", None))
        self.lineEdit_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"-6", None))
        self.lineEdit_18.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.lineEdit_16.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"same", None))
        self.label_png2.setText(QCoreApplication.translate("MainWindow", u"Clustering figureInstructions:\n"
"\n"
"1. Drag the file or click 'OPEN' to identify the file, click the button to start the calculation\n"
"\n"
"2. Various data preprocessing methods, it is recommended to try a variety of combinations (so that the feature separation is high)\n"
"\n"
"Note: The processed curves are used for clustering, and the original data used for drawing ensures reliability. The pre-processed data does not participate in the final drawing results, but only provides classification basis\n"
"\n"
"3. All saved files are stored in the source data folder by default, including all drawing data\n"
"\n"
"4. The drawing parameters are all parameters of the histogram, where bin represents the number of histogram boxes and -1 represents the pre-set distance cutoff -- from 0 to the average length +0.2nm (due to large changes in the experiment).\n"
"", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Correlation analysis and length redrawing, data redrawing after clustering", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.open_file_button_3.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.mergeSaveButton2.setText(QCoreApplication.translate("MainWindow", u"Merge Save", None))
        self.save_Button_3.setText(QCoreApplication.translate("MainWindow", u"Save\uff08all\uff09", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"2D_his_style_set", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"1D_his_style_set", None))
        self.color_style_1d.setItemText(0, QCoreApplication.translate("MainWindow", u"olivedrab", None))
        self.color_style_1d.setItemText(1, QCoreApplication.translate("MainWindow", u"mediumpurple", None))
        self.color_style_1d.setItemText(2, QCoreApplication.translate("MainWindow", u"black", None))
        self.color_style_1d.setItemText(3, QCoreApplication.translate("MainWindow", u"orchid", None))
        self.color_style_1d.setItemText(4, QCoreApplication.translate("MainWindow", u"lightslategray", None))
        self.color_style_1d.setItemText(5, QCoreApplication.translate("MainWindow", u"chocolate", None))
        self.color_style_1d.setItemText(6, QCoreApplication.translate("MainWindow", u"palegreen", None))
        self.color_style_1d.setItemText(7, QCoreApplication.translate("MainWindow", u"darkgoldenrod", None))
        self.color_style_1d.setItemText(8, QCoreApplication.translate("MainWindow", u"darkgoldenrod", None))
        self.color_style_1d.setItemText(9, QCoreApplication.translate("MainWindow", u"antiquewhite", None))
        self.color_style_1d.setItemText(10, QCoreApplication.translate("MainWindow", u"darkslategrey", None))
        self.color_style_1d.setItemText(11, QCoreApplication.translate("MainWindow", u"antiquewhite", None))
        self.color_style_1d.setItemText(12, QCoreApplication.translate("MainWindow", u"slategrey", None))
        self.color_style_1d.setItemText(13, QCoreApplication.translate("MainWindow", u"lightsteelblue", None))
        self.color_style_1d.setItemText(14, QCoreApplication.translate("MainWindow", u"violet", None))
        self.color_style_1d.setItemText(15, QCoreApplication.translate("MainWindow", u"Green", None))
        self.color_style_1d.setItemText(16, QCoreApplication.translate("MainWindow", u"Gray", None))
        self.color_style_1d.setItemText(17, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.color_style_1d.setItemText(18, QCoreApplication.translate("MainWindow", u"Red", None))
        self.color_style_1d.setItemText(19, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.color_style_1d.setItemText(20, QCoreApplication.translate("MainWindow", u"Purple", None))

        self.color_style_2d.setItemText(0, QCoreApplication.translate("MainWindow", u"afmhot", None))
        self.color_style_2d.setItemText(1, QCoreApplication.translate("MainWindow", u"terrain_r", None))
        self.color_style_2d.setItemText(2, QCoreApplication.translate("MainWindow", u"gnuplot", None))
        self.color_style_2d.setItemText(3, QCoreApplication.translate("MainWindow", u"jet", None))
        self.color_style_2d.setItemText(4, QCoreApplication.translate("MainWindow", u"gray_r", None))
        self.color_style_2d.setItemText(5, QCoreApplication.translate("MainWindow", u"magma", None))
        self.color_style_2d.setItemText(6, QCoreApplication.translate("MainWindow", u"viridis", None))
        self.color_style_2d.setItemText(7, QCoreApplication.translate("MainWindow", u"coolwarm", None))
        self.color_style_2d.setItemText(8, QCoreApplication.translate("MainWindow", u"ocean_r", None))
        self.color_style_2d.setItemText(9, QCoreApplication.translate("MainWindow", u"PRGn", None))
        self.color_style_2d.setItemText(10, QCoreApplication.translate("MainWindow", u"hot", None))
        self.color_style_2d.setItemText(11, QCoreApplication.translate("MainWindow", u"cividis", None))
        self.color_style_2d.setItemText(12, QCoreApplication.translate("MainWindow", u"plasma", None))
        self.color_style_2d.setItemText(13, QCoreApplication.translate("MainWindow", u"flag", None))
        self.color_style_2d.setItemText(14, QCoreApplication.translate("MainWindow", u"twilight", None))
        self.color_style_2d.setItemText(15, QCoreApplication.translate("MainWindow", u"tab20c", None))
        self.color_style_2d.setItemText(16, QCoreApplication.translate("MainWindow", u"hsv", None))
        self.color_style_2d.setItemText(17, QCoreApplication.translate("MainWindow", u"gnuplot2", None))
        self.color_style_2d.setItemText(18, QCoreApplication.translate("MainWindow", u"inferno", None))
        self.color_style_2d.setItemText(19, QCoreApplication.translate("MainWindow", u"cool", None))
        self.color_style_2d.setItemText(20, QCoreApplication.translate("MainWindow", u"spring", None))
        self.color_style_2d.setItemText(21, QCoreApplication.translate("MainWindow", u"Accent", None))
        self.color_style_2d.setItemText(22, QCoreApplication.translate("MainWindow", u"Blues", None))
        self.color_style_2d.setItemText(23, QCoreApplication.translate("MainWindow", u"BrBG", None))
        self.color_style_2d.setItemText(24, QCoreApplication.translate("MainWindow", u"BuGn", None))
        self.color_style_2d.setItemText(25, QCoreApplication.translate("MainWindow", u"BuPu", None))
        self.color_style_2d.setItemText(26, QCoreApplication.translate("MainWindow", u"CMRmap", None))
        self.color_style_2d.setItemText(27, QCoreApplication.translate("MainWindow", u"Dark2", None))
        self.color_style_2d.setItemText(28, QCoreApplication.translate("MainWindow", u"GnBu", None))
        self.color_style_2d.setItemText(29, QCoreApplication.translate("MainWindow", u"Greens", None))
        self.color_style_2d.setItemText(30, QCoreApplication.translate("MainWindow", u"Greys", None))
        self.color_style_2d.setItemText(31, QCoreApplication.translate("MainWindow", u"OrRd", None))
        self.color_style_2d.setItemText(32, QCoreApplication.translate("MainWindow", u"Oranges", None))
        self.color_style_2d.setItemText(33, QCoreApplication.translate("MainWindow", u"Paired", None))
        self.color_style_2d.setItemText(34, QCoreApplication.translate("MainWindow", u"Pastel1", None))
        self.color_style_2d.setItemText(35, QCoreApplication.translate("MainWindow", u"Pastel2", None))
        self.color_style_2d.setItemText(36, QCoreApplication.translate("MainWindow", u"PiYG", None))
        self.color_style_2d.setItemText(37, QCoreApplication.translate("MainWindow", u"PuBuGn", None))
        self.color_style_2d.setItemText(38, QCoreApplication.translate("MainWindow", u"PuOr", None))
        self.color_style_2d.setItemText(39, QCoreApplication.translate("MainWindow", u"PuRd", None))
        self.color_style_2d.setItemText(40, QCoreApplication.translate("MainWindow", u"Purples", None))
        self.color_style_2d.setItemText(41, QCoreApplication.translate("MainWindow", u"RdBu", None))
        self.color_style_2d.setItemText(42, QCoreApplication.translate("MainWindow", u"RdGy", None))
        self.color_style_2d.setItemText(43, QCoreApplication.translate("MainWindow", u"RdPu", None))
        self.color_style_2d.setItemText(44, QCoreApplication.translate("MainWindow", u"RdYlBu", None))
        self.color_style_2d.setItemText(45, QCoreApplication.translate("MainWindow", u"RdYlGn", None))
        self.color_style_2d.setItemText(46, QCoreApplication.translate("MainWindow", u"Reds", None))
        self.color_style_2d.setItemText(47, QCoreApplication.translate("MainWindow", u"Set1", None))
        self.color_style_2d.setItemText(48, QCoreApplication.translate("MainWindow", u"Set2", None))
        self.color_style_2d.setItemText(49, QCoreApplication.translate("MainWindow", u"Set3", None))
        self.color_style_2d.setItemText(50, QCoreApplication.translate("MainWindow", u"Spectral", None))
        self.color_style_2d.setItemText(51, QCoreApplication.translate("MainWindow", u"Wistia", None))
        self.color_style_2d.setItemText(52, QCoreApplication.translate("MainWindow", u"YlGn", None))
        self.color_style_2d.setItemText(53, QCoreApplication.translate("MainWindow", u"YlGnBu", None))
        self.color_style_2d.setItemText(54, QCoreApplication.translate("MainWindow", u"YlOrBr", None))
        self.color_style_2d.setItemText(55, QCoreApplication.translate("MainWindow", u"YlOrRd", None))
        self.color_style_2d.setItemText(56, QCoreApplication.translate("MainWindow", u"autumn", None))
        self.color_style_2d.setItemText(57, QCoreApplication.translate("MainWindow", u"binary", None))
        self.color_style_2d.setItemText(58, QCoreApplication.translate("MainWindow", u"bone", None))
        self.color_style_2d.setItemText(59, QCoreApplication.translate("MainWindow", u"brg", None))
        self.color_style_2d.setItemText(60, QCoreApplication.translate("MainWindow", u"bwr", None))
        self.color_style_2d.setItemText(61, QCoreApplication.translate("MainWindow", u"cividis", None))
        self.color_style_2d.setItemText(62, QCoreApplication.translate("MainWindow", u"cool", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Plot style: (all figure)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Use coolwarm in cov", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"The number of curves in each packet", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Clustering num of Subsection", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"length value when conductance is", None))
        self.div_clu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Subsection and clustering", None))
        self.divide_pushButton.setText(QCoreApplication.translate("MainWindow", u"Subsection and calculation", None))
        self.peak_pushButton.setText(QCoreApplication.translate("MainWindow", u"Length_run", None))
        self.run_cov_pushButton.setText(QCoreApplication.translate("MainWindow", u"covariance_run (bin and range same with Conductance)", None))
        self.Peak_Subsection.setText(QCoreApplication.translate("MainWindow", u"Length_Subsection and calculation (b or r same with Con)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"cov_max_value: \u00b1", None))
        self.lineEdit_20.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_sub.setText(QCoreApplication.translate("MainWindow", u"Subsection and calculation figure\n"
"\n"
"peak_run is used to redraw the length image and fit the Gaussian curve,\n"
"\n"
"Select the peak position to find the length of that position", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Select a single curve and search for values similar to it", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.open_file_button_4.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Search in other single_trance, which does not support dragging  ", None))
        self.open_file_Button_6.setText(QCoreApplication.translate("MainWindow", u"Open_S", None))
        self.single_find_pushButton.setText(QCoreApplication.translate("MainWindow", u"Minkowski_find", None))
        self.Correlation_find_pushButton.setText(QCoreApplication.translate("MainWindow", u"Correlation_find", None))
        self.Stable_sort_mean.setText(QCoreApplication.translate("MainWindow", u"FN", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Minkowski parameter:", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Abs_sort_mean", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save_all", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sort range", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Select a curve", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Gaussian fit curve", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Mean fit curve", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Select the single line to match on the first page and calculate directly\n"
"\n"
"You can choose to approximate a single curve,\n"
"\n"
"You can also import single curves of other packets in the second input box,\n"
"\n"
"Mean fitting is performed by default, and you can choose histogram Gaussian fitting", None))
        self.label_23.setText("")
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"Chose the fix-junction data for processing", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.open_file_button_5.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"bins_y", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"preview_num", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"bins_x", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"N_CacuTime", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Preview_cut part", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"frequence", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"logG_low", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"logG_high", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"windowsize", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Show_psd_list", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Show_N_list.setText(QCoreApplication.translate("MainWindow", u"1st_step_N_list", None))
        self.label_57.setText("")
        self.lineEdit_iv.setText(QCoreApplication.translate("MainWindow", u"Open IV result floder", None))
        self.lineEdit_iv.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.open_file_button_iv.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.run_file_button_iv.setText(QCoreApplication.translate("MainWindow", u"Base_Run", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"DeCapicity", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Cluster_way", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Cluster_num", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Smoothing_coefficient", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Select a curve", None))
        self.iv_cluster_way_test.setItemText(0, QCoreApplication.translate("MainWindow", u"Kmeans\uff08Recommended\uff09", None))
        self.iv_cluster_way_test.setItemText(1, QCoreApplication.translate("MainWindow", u"Gaussian Mixture Model", None))
        self.iv_cluster_way_test.setItemText(2, QCoreApplication.translate("MainWindow", u"KShape", None))
        self.iv_cluster_way_test.setItemText(3, QCoreApplication.translate("MainWindow", u"TimeSeriesKMeans\uff08Recommended\uff09", None))

        self.Chose_data_and_change_to_cluster_text.setItemText(0, QCoreApplication.translate("MainWindow", u"Raw data", None))
        self.Chose_data_and_change_to_cluster_text.setItemText(1, QCoreApplication.translate("MainWindow", u"1 D HIS", None))
        self.Chose_data_and_change_to_cluster_text.setItemText(2, QCoreApplication.translate("MainWindow", u"2 D HIS", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Chose_data", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Chose_data_and_change_to_cluster", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"peak_end", None))
        self.Chose_data_text.setItemText(0, QCoreApplication.translate("MainWindow", u"For_LogI(nA)", None))
        self.Chose_data_text.setItemText(1, QCoreApplication.translate("MainWindow", u"For_log(dI_dV)", None))
        self.Chose_data_text.setItemText(2, QCoreApplication.translate("MainWindow", u"For_LogG", None))
        self.Chose_data_text.setItemText(3, QCoreApplication.translate("MainWindow", u"Rev_LogI(nA)", None))
        self.Chose_data_text.setItemText(4, QCoreApplication.translate("MainWindow", u"Rev_log(dI_dV)", None))
        self.Chose_data_text.setItemText(5, QCoreApplication.translate("MainWindow", u"Rev_LogG", None))
        self.Chose_data_text.setItemText(6, QCoreApplication.translate("MainWindow", u"For_I", None))
        self.Chose_data_text.setItemText(7, QCoreApplication.translate("MainWindow", u"Rev_I", None))

        self.label_31.setText(QCoreApplication.translate("MainWindow", u"bias_base", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"peak_start", None))
        self.Single_pre_iv.setText(QCoreApplication.translate("MainWindow", u"Single_pre", None))
        self.saveall_iv.setText(QCoreApplication.translate("MainWindow", u"Save_IV", None))
        self.Draw_his_iv.setText(QCoreApplication.translate("MainWindow", u"Draw_1d_his", None))
        self.Cluster_run_iv.setText(QCoreApplication.translate("MainWindow", u"Cluster_run", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"bin2d_his", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"2D_his_Max_set", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"bin1d_his", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"logI", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"log(dI/dV)", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"logG", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"I(E-6mA)", None))
        self.label_iv.setText(QCoreApplication.translate("MainWindow", u"   First, enter or open the VSCAN test results folder, click Base_Run, and the following images will be displayed:\n"
"                 Forward Scan, Reverse Scan,\n"
"                 Super position, \n"
"                 Forward Scan(log(dI/dV)) & smoothing, \n"
"                 Reverse Scan(log(dI/dV)) & smoothing, \n"
"                 Conductance(LogG), (no filtering when \n"
"                 smoothing parameter is 200+);\n"
"   Then select the data that has just been calculated for clustering or Draw1dhis,only the color parameter of figure is same", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Wang Haoyu  Tianjin", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.8.1", None))
    # retranslateUi

