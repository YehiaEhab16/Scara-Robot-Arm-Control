##########################################################################################
####################### Project: Scara Robot Arm                   #######################
####################### Version: 1.3                               #######################
####################### Author: Yehia Ehab                         #######################
####################### Date : 19/04/2025                          #######################
##########################################################################################

# UI File #

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QAbstractItemView, QPushButton, QRadioButton, QSizePolicy, QSlider, QVBoxLayout
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont,QIcon, QPixmap
import resources

class ScaraUi(object):
    def setupUi(self, Scara):
        if not Scara.objectName():
            Scara.setObjectName(u"Scara")
        Scara.resize(550, 560)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Scara.sizePolicy().hasHeightForWidth())
        Scara.setSizePolicy(sizePolicy)
        Scara.setMinimumSize(QSize(550, 560))
        icon = QIcon()
        icon.addFile(u":/Icons/Icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Scara.setWindowIcon(icon)
        Scara.setStyleSheet(u"QWidget#Scara{\n"
"background-color: \n"
"	qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 rgb(50, 50, 50),\n"
"        stop: 0.5 rgb(30, 30, 30),\n"
"        stop: 1 rgb(50, 50, 50)\n"
"    );\n"
"}\n"
"\n"
"QFrame {\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: transparent;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}\n"
"\n"
" QLineEdit {\n"
"    background-color: rgba(80, 80, 80, 150);\n"
"    border-radius: 10px;\n"
"    padding:2px;\n"
"    border: 2px solid rgba(150, 150, 150, 150);\n"
"    color: silver;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgba(80, 80, 80, 150);\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid grey;\n"
"height: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"backgro"
                        "und: rgb(255, 147, 21);\n"
"width: 10px;\n"
"margin: -5px -1px;\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(255, 147, 21);\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background:  rgba(150, 150, 150,150); \n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.1 rgb(200, 200, 200), stop:1 rgb(255, 147, 21));\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: rgb(255,100,20);\n"
"border-color: rgb(255,100,20);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"background: rgb(255,80,20);\n"
"border-color: rgb(255,80,20);\n"
"}\n"
"\n"
"QRadioButton {\n"
"	color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:  18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/Icons/unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(:/Icons/hover.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/Icons/c"
                        "hecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(:/Icons/checked_hover.png);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:  30 px;\n"
"    height: 30 px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/Labels/power_off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(:/Labels/power_on_hover.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/Labels/power_on.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    image: url(:/Labels/power_off_hover.png);\n"
"}\n"
"\n"
"QProgressBar{\n"
"background-color:transparent;\n"
"border-radius: 7px;\n"
"border: 2px solid rgba(150, 150, 150,150); \n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.1 rgb(200, 200, 200), stop:1 rgb(255, 147, 21));\n"
"}\n"
"\n"
"QMessageBox {\n"
" background-color: \n"
"	qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        "
                        "stop: 0 rgb(50, 50, 50),\n"
"        stop: 0.5 rgb(30, 30, 30),\n"
"        stop: 1 rgb(50, 50, 50)\n"
"    );\n"
"  width: 400px; \n"
"  height: 400px;\n"
"}\n"
"QMessageBox QLabel {\n"
"background-color: transparent;\n"
"color: white;\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"   background-color: rgba(80, 80, 80, 150);\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
" 	border: 2px solid rgba(150, 150, 150,150); \n"
"	font: 12pt \"Segoe UI\";\n"
"	min-width: 50 px;\n"
"	padding: 2 px;\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"  background-color:rgba(255, 144, 0, 50);    \n"
"}\n"
"\n"
"QMessageBox QPushButton:pressed {\n"
"   background-color:rgba(255, 144, 0, 150);\n"
"   border: 2px solid #CCCCCC; \n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color:rgb(30, 30, 30);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border: non"
                        "e;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background: rgb(200, 200, 200);\n"
"    min-height: 5px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"   background: rgb(255, 120, 20);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed\n"
"{\n"
"   background: rgb(255, 80, 0);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image:  url(:/Icons/up_arrow.png);\n"
"    height: 11px;\n"
"    width: 11px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image :url(:/Icons/down_arrow.png);\n"
"    height: 11px;\n"
"    width: 11px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/Icons/up_arrow.png);\n"
"    height: 11px;\n"
""
                        "    width: 11px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/Icons/down_arrow.png);\n"
"    height: 11px;\n"
"    width: 11px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    background-color: rgb(30, 30, 30);\n"
"    height: 14px;\n"
"    margin: 0px 15px 0px 15px;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background: rgb(200, 200, 200);\n"
"    min-width: 5px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover\n"
"{\n"
"   background: rgb(255, 120, 20);\n"
"}\n"
"\n"
"QScrollB"
                        "ar::handle:horizontal:pressed\n"
"{\n"
"   background: rgb(255, 80, 0);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/Icons/left_arrow.png);\n"
"    height: 11px;\n"
"    width: 11px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/Icons/right_arrow.png);\n"
"    height: 11px;\n"
"    width: 11px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/Icons/left_arrow.png);\n"
"    height: 11px;\n"
"    width: 11px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/Icons/right_arrow.png);\n"
"    height: 11px;\n"
"    width: 11px;\n"
""
                        "    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(Scara)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.topFrame = QFrame(Scara)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.communicationFrame = QFrame(self.topFrame)
        self.communicationFrame.setObjectName(u"communicationFrame")
        self.communicationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.communicationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.communicationFrame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.portFrame = QFrame(self.communicationFrame)
        self.portFrame.setObjectName(u"portFrame")
        self.portFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.portFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.portFrame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comLabel = QLabel(self.portFrame)
        self.comLabel.setObjectName(u"comLabel")
        font = QFont()
        font.setPointSize(12)
        self.comLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.comLabel)

        self.portLineEdit = QLineEdit(self.portFrame)
        self.portLineEdit.setObjectName(u"portLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy1)
        self.portLineEdit.setMaximumSize(QSize(80, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.portLineEdit.setFont(font1)
        self.portLineEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.portLineEdit.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.portLineEdit)


        self.horizontalLayout_5.addWidget(self.portFrame)

        self.comButton = QPushButton(self.communicationFrame)
        self.comButton.setObjectName(u"comButton")
        sizePolicy1.setHeightForWidth(self.comButton.sizePolicy().hasHeightForWidth())
        self.comButton.setSizePolicy(sizePolicy1)
        self.comButton.setMinimumSize(QSize(40, 40))
        font2 = QFont()
        font2.setPointSize(1)
        self.comButton.setFont(font2)
        self.comButton.setToolTipDuration(2000)
        self.comButton.setStyleSheet(u"QPushButton:hover {\n"
"    icon: url(:/Labels/light.png);\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:pressed {\n"
"    icon: url(:/Labels/orange.png);\n"
"	background-color: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Labels/red.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comButton.setIcon(icon1)
        self.comButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.comButton)


        self.horizontalLayout_6.addWidget(self.communicationFrame, 0, Qt.AlignmentFlag.AlignLeft)

        self.logoLabel = QLabel(self.topFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMaximumSize(QSize(170, 30))
        font3 = QFont()
        font3.setPointSize(20)
        self.logoLabel.setFont(font3)
        self.logoLabel.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(0, 85, 255);")
        self.logoLabel.setPixmap(QPixmap(u":/Labels/logo.png"))
        self.logoLabel.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.logoLabel)

        self.rndLabel = QLabel(self.topFrame)
        self.rndLabel.setObjectName(u"rndLabel")
        self.rndLabel.setMinimumSize(QSize(0, 40))
        self.rndLabel.setMaximumSize(QSize(70, 16777215))
        self.rndLabel.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.rndLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_4.addWidget(self.topFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.middleFrame = QFrame(Scara)
        self.middleFrame.setObjectName(u"middleFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.middleFrame.sizePolicy().hasHeightForWidth())
        self.middleFrame.setSizePolicy(sizePolicy2)
        self.middleFrame.setStyleSheet(u"QFrame#middleFrame{\n"
"background-color: rgba(55, 55, 55, 120);\n"
"}")
        self.middleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.middleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.middleFrame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 5)
        self.forwardFrame = QFrame(self.middleFrame)
        self.forwardFrame.setObjectName(u"forwardFrame")
        self.forwardFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.forwardFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.forwardFrame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.forwardFrame)

        self.forwardLabel = QLabel(self.middleFrame)
        self.forwardLabel.setObjectName(u"forwardLabel")
        self.forwardLabel.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.forwardLabel.sizePolicy().hasHeightForWidth())
        self.forwardLabel.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(14)
        self.forwardLabel.setFont(font4)
        self.forwardLabel.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 120, 20);")

        self.verticalLayout.addWidget(self.forwardLabel)

        self.jointsFrame = QFrame(self.middleFrame)
        self.jointsFrame.setObjectName(u"jointsFrame")
        sizePolicy2.setHeightForWidth(self.jointsFrame.sizePolicy().hasHeightForWidth())
        self.jointsFrame.setSizePolicy(sizePolicy2)
        self.jointsFrame.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"}")
        self.jointsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.jointsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.jointsFrame)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 0, 0, 0)
        self.radioFrame = QFrame(self.jointsFrame)
        self.radioFrame.setObjectName(u"radioFrame")
        self.radioFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.radioFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.radioFrame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.firstJointRadio = QRadioButton(self.radioFrame)
        self.firstJointRadio.setObjectName(u"firstJointRadio")
        self.firstJointRadio.setFont(font1)
        self.firstJointRadio.setAutoFillBackground(False)
        self.firstJointRadio.setStyleSheet(u"")
        self.firstJointRadio.setCheckable(True)
        self.firstJointRadio.setChecked(False)
        self.firstJointRadio.setAutoRepeat(False)

        self.verticalLayout_6.addWidget(self.firstJointRadio)

        self.secondJointRadio = QRadioButton(self.radioFrame)
        self.secondJointRadio.setObjectName(u"secondJointRadio")
        self.secondJointRadio.setFont(font1)
        self.secondJointRadio.setAutoFillBackground(False)
        self.secondJointRadio.setStyleSheet(u"")
        self.secondJointRadio.setCheckable(True)
        self.secondJointRadio.setChecked(False)
        self.secondJointRadio.setAutoRepeat(False)

        self.verticalLayout_6.addWidget(self.secondJointRadio)

        self.thirdJointRadio = QRadioButton(self.radioFrame)
        self.thirdJointRadio.setObjectName(u"thirdJointRadio")
        self.thirdJointRadio.setFont(font1)
        self.thirdJointRadio.setAutoFillBackground(False)
        self.thirdJointRadio.setStyleSheet(u"")
        self.thirdJointRadio.setCheckable(True)
        self.thirdJointRadio.setChecked(False)
        self.thirdJointRadio.setAutoRepeat(False)

        self.verticalLayout_6.addWidget(self.thirdJointRadio)

        self.zPositionRadio = QRadioButton(self.radioFrame)
        self.zPositionRadio.setObjectName(u"zPositionRadio")
        self.zPositionRadio.setFont(font1)
        self.zPositionRadio.setAutoFillBackground(False)
        self.zPositionRadio.setStyleSheet(u"")
        self.zPositionRadio.setCheckable(True)
        self.zPositionRadio.setChecked(False)
        self.zPositionRadio.setAutoRepeat(False)

        self.verticalLayout_6.addWidget(self.zPositionRadio)


        self.horizontalLayout_9.addWidget(self.radioFrame)

        self.progressFrame = QFrame(self.jointsFrame)
        self.progressFrame.setObjectName(u"progressFrame")
        self.progressFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.progressFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.progressFrame)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.firstJointFrame = QFrame(self.progressFrame)
        self.firstJointFrame.setObjectName(u"firstJointFrame")
        self.firstJointFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstJointFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.firstJointFrame)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.firstJointSlider = QSlider(self.firstJointFrame)
        self.firstJointSlider.setObjectName(u"firstJointSlider")
        self.firstJointSlider.setMinimum(-45)
        self.firstJointSlider.setMaximum(260)
        self.firstJointSlider.setSingleStep(0)
        self.firstJointSlider.setPageStep(0)
        self.firstJointSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_8.addWidget(self.firstJointSlider)

        self.firstJointButtonsFrame = QFrame(self.firstJointFrame)
        self.firstJointButtonsFrame.setObjectName(u"firstJointButtonsFrame")
        self.firstJointButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstJointButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.firstJointButtonsFrame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.firstJointMoveButton = QPushButton(self.firstJointButtonsFrame)
        self.firstJointMoveButton.setObjectName(u"firstJointMoveButton")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.firstJointMoveButton.setIcon(icon2)
        self.firstJointMoveButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.firstJointMoveButton)

        self.firstJointCancelButton = QPushButton(self.firstJointButtonsFrame)
        self.firstJointCancelButton.setObjectName(u"firstJointCancelButton")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.firstJointCancelButton.setIcon(icon3)
        self.firstJointCancelButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.firstJointCancelButton)


        self.horizontalLayout_8.addWidget(self.firstJointButtonsFrame)


        self.verticalLayout_8.addWidget(self.firstJointFrame)

        self.secondJointFrame = QFrame(self.progressFrame)
        self.secondJointFrame.setObjectName(u"secondJointFrame")
        self.secondJointFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondJointFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.secondJointFrame)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.secondJointSlider = QSlider(self.secondJointFrame)
        self.secondJointSlider.setObjectName(u"secondJointSlider")
        self.secondJointSlider.setMinimum(-150)
        self.secondJointSlider.setMaximum(150)
        self.secondJointSlider.setSingleStep(0)
        self.secondJointSlider.setPageStep(0)
        self.secondJointSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_12.addWidget(self.secondJointSlider)

        self.secondJointButtonsFrame = QFrame(self.secondJointFrame)
        self.secondJointButtonsFrame.setObjectName(u"secondJointButtonsFrame")
        self.secondJointButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondJointButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.secondJointButtonsFrame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.secondJointMoveButton = QPushButton(self.secondJointButtonsFrame)
        self.secondJointMoveButton.setObjectName(u"secondJointMoveButton")
        self.secondJointMoveButton.setIcon(icon2)
        self.secondJointMoveButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.secondJointMoveButton)

        self.secondJointCancelButton = QPushButton(self.secondJointButtonsFrame)
        self.secondJointCancelButton.setObjectName(u"secondJointCancelButton")
        self.secondJointCancelButton.setIcon(icon3)
        self.secondJointCancelButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.secondJointCancelButton)


        self.horizontalLayout_12.addWidget(self.secondJointButtonsFrame)


        self.verticalLayout_8.addWidget(self.secondJointFrame)

        self.thirdJointFrame = QFrame(self.progressFrame)
        self.thirdJointFrame.setObjectName(u"thirdJointFrame")
        self.thirdJointFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.thirdJointFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.thirdJointFrame)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.thirdJointSlider = QSlider(self.thirdJointFrame)
        self.thirdJointSlider.setObjectName(u"thirdJointSlider")
        self.thirdJointSlider.setMinimum(-170)
        self.thirdJointSlider.setMaximum(170)
        self.thirdJointSlider.setSingleStep(0)
        self.thirdJointSlider.setPageStep(0)
        self.thirdJointSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_14.addWidget(self.thirdJointSlider)

        self.thirdJointButtonsFrame = QFrame(self.thirdJointFrame)
        self.thirdJointButtonsFrame.setObjectName(u"thirdJointButtonsFrame")
        self.thirdJointButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.thirdJointButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.thirdJointButtonsFrame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.thirdJointMoveButton = QPushButton(self.thirdJointButtonsFrame)
        self.thirdJointMoveButton.setObjectName(u"thirdJointMoveButton")
        self.thirdJointMoveButton.setIcon(icon2)
        self.thirdJointMoveButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_15.addWidget(self.thirdJointMoveButton)

        self.thirdJointCancelButton = QPushButton(self.thirdJointButtonsFrame)
        self.thirdJointCancelButton.setObjectName(u"thirdJointCancelButton")
        self.thirdJointCancelButton.setIcon(icon3)
        self.thirdJointCancelButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_15.addWidget(self.thirdJointCancelButton)


        self.horizontalLayout_14.addWidget(self.thirdJointButtonsFrame)


        self.verticalLayout_8.addWidget(self.thirdJointFrame)

        self.zPositionSliderFrame = QFrame(self.progressFrame)
        self.zPositionSliderFrame.setObjectName(u"zPositionSliderFrame")
        self.zPositionSliderFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.zPositionSliderFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.zPositionSliderFrame)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.zPositionSlider = QSlider(self.zPositionSliderFrame)
        self.zPositionSlider.setObjectName(u"zPositionSlider")
        self.zPositionSlider.setMinimum(0)
        self.zPositionSlider.setMaximum(150)
        self.zPositionSlider.setSingleStep(0)
        self.zPositionSlider.setPageStep(0)
        self.zPositionSlider.setValue(100)
        self.zPositionSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_16.addWidget(self.zPositionSlider)

        self.zPositionButtonsFrame = QFrame(self.zPositionSliderFrame)
        self.zPositionButtonsFrame.setObjectName(u"zPositionButtonsFrame")
        self.zPositionButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.zPositionButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.zPositionButtonsFrame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.zPositionMoveButton = QPushButton(self.zPositionButtonsFrame)
        self.zPositionMoveButton.setObjectName(u"zPositionMoveButton")
        self.zPositionMoveButton.setIcon(icon2)
        self.zPositionMoveButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_17.addWidget(self.zPositionMoveButton)

        self.zPositionCancelButton = QPushButton(self.zPositionButtonsFrame)
        self.zPositionCancelButton.setObjectName(u"zPositionCancelButton")
        self.zPositionCancelButton.setIcon(icon3)
        self.zPositionCancelButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_17.addWidget(self.zPositionCancelButton)


        self.horizontalLayout_16.addWidget(self.zPositionButtonsFrame)


        self.verticalLayout_8.addWidget(self.zPositionSliderFrame)


        self.horizontalLayout_9.addWidget(self.progressFrame)

        self.actualForwardValuesFrame = QFrame(self.jointsFrame)
        self.actualForwardValuesFrame.setObjectName(u"actualForwardValuesFrame")
        self.actualForwardValuesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.actualForwardValuesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.actualForwardValuesFrame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.actualFirstJointValueLabel = QLabel(self.actualForwardValuesFrame)
        self.actualFirstJointValueLabel.setObjectName(u"actualFirstJointValueLabel")
        self.actualFirstJointValueLabel.setFont(font)

        self.verticalLayout_7.addWidget(self.actualFirstJointValueLabel)

        self.actualSecondJointValueLabel = QLabel(self.actualForwardValuesFrame)
        self.actualSecondJointValueLabel.setObjectName(u"actualSecondJointValueLabel")
        self.actualSecondJointValueLabel.setFont(font)

        self.verticalLayout_7.addWidget(self.actualSecondJointValueLabel)

        self.actualThirdJointValueLabel = QLabel(self.actualForwardValuesFrame)
        self.actualThirdJointValueLabel.setObjectName(u"actualThirdJointValueLabel")
        self.actualThirdJointValueLabel.setFont(font)

        self.verticalLayout_7.addWidget(self.actualThirdJointValueLabel)

        self.actualZPositionValueLabel = QLabel(self.actualForwardValuesFrame)
        self.actualZPositionValueLabel.setObjectName(u"actualZPositionValueLabel")
        self.actualZPositionValueLabel.setFont(font)

        self.verticalLayout_7.addWidget(self.actualZPositionValueLabel)


        self.horizontalLayout_9.addWidget(self.actualForwardValuesFrame)

        self.forwadValuesFrame = QFrame(self.jointsFrame)
        self.forwadValuesFrame.setObjectName(u"forwadValuesFrame")
        self.forwadValuesFrame.setStyleSheet(u"QLabel {\n"
"  color: grey;\n"
"}")
        self.forwadValuesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.forwadValuesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.forwadValuesFrame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.firstJointValueLabel = QLabel(self.forwadValuesFrame)
        self.firstJointValueLabel.setObjectName(u"firstJointValueLabel")
        self.firstJointValueLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.firstJointValueLabel)

        self.secondJointValueLabel = QLabel(self.forwadValuesFrame)
        self.secondJointValueLabel.setObjectName(u"secondJointValueLabel")
        self.secondJointValueLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.secondJointValueLabel)

        self.thirdJointValueLabel = QLabel(self.forwadValuesFrame)
        self.thirdJointValueLabel.setObjectName(u"thirdJointValueLabel")
        self.thirdJointValueLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.thirdJointValueLabel)

        self.zPositionValueLabel = QLabel(self.forwadValuesFrame)
        self.zPositionValueLabel.setObjectName(u"zPositionValueLabel")
        self.zPositionValueLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.zPositionValueLabel)


        self.horizontalLayout_9.addWidget(self.forwadValuesFrame)

        self.addButtonFrame = QFrame(self.jointsFrame)
        self.addButtonFrame.setObjectName(u"addButtonFrame")
        self.addButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.addButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.addButtonFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 50, 0, 0)
        self.addButton = QPushButton(self.addButtonFrame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setToolTipDuration(2000)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addButton.setIcon(icon4)
        self.addButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.addButton)


        self.horizontalLayout_9.addWidget(self.addButtonFrame)


        self.verticalLayout.addWidget(self.jointsFrame)

        self.controlFrame = QFrame(self.middleFrame)
        self.controlFrame.setObjectName(u"controlFrame")
        sizePolicy2.setHeightForWidth(self.controlFrame.sizePolicy().hasHeightForWidth())
        self.controlFrame.setSizePolicy(sizePolicy2)
        self.controlFrame.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"}\n"
"QFrame#controlFrame {\n"
"	border-radius: 0 px;\n"
"	border-top: 2px solid rgb(255,120,20);\n"
"}")
        self.controlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.controlFrame)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 0, 0)
        self.controlRadioFrame = QFrame(self.controlFrame)
        self.controlRadioFrame.setObjectName(u"controlRadioFrame")
        self.controlRadioFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlRadioFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.controlRadioFrame)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gripperRadio = QRadioButton(self.controlRadioFrame)
        self.gripperRadio.setObjectName(u"gripperRadio")
        self.gripperRadio.setFont(font)

        self.verticalLayout_14.addWidget(self.gripperRadio)

        self.speedRadio = QRadioButton(self.controlRadioFrame)
        self.speedRadio.setObjectName(u"speedRadio")
        self.speedRadio.setFont(font)

        self.verticalLayout_14.addWidget(self.speedRadio)

        self.accelerationRadio = QRadioButton(self.controlRadioFrame)
        self.accelerationRadio.setObjectName(u"accelerationRadio")
        self.accelerationRadio.setFont(font)

        self.verticalLayout_14.addWidget(self.accelerationRadio)


        self.horizontalLayout.addWidget(self.controlRadioFrame)

        self.controlSlidersFrame = QFrame(self.controlFrame)
        self.controlSlidersFrame.setObjectName(u"controlSlidersFrame")
        self.controlSlidersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlSlidersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.controlSlidersFrame)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gripperSlider = QSlider(self.controlSlidersFrame)
        self.gripperSlider.setObjectName(u"gripperSlider")
        self.gripperSlider.setMaximum(180)
        self.gripperSlider.setSingleStep(0)
        self.gripperSlider.setPageStep(0)
        self.gripperSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_15.addWidget(self.gripperSlider)

        self.speedSlider = QSlider(self.controlSlidersFrame)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setMinimum(500)
        self.speedSlider.setMaximum(4000)
        self.speedSlider.setSingleStep(0)
        self.speedSlider.setPageStep(0)
        self.speedSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_15.addWidget(self.speedSlider)

        self.accelerationSlider = QSlider(self.controlSlidersFrame)
        self.accelerationSlider.setObjectName(u"accelerationSlider")
        self.accelerationSlider.setMinimum(500)
        self.accelerationSlider.setMaximum(2000)
        self.accelerationSlider.setSingleStep(0)
        self.accelerationSlider.setPageStep(0)
        self.accelerationSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_15.addWidget(self.accelerationSlider)


        self.horizontalLayout.addWidget(self.controlSlidersFrame)

        self.controlValuesFrame = QFrame(self.controlFrame)
        self.controlValuesFrame.setObjectName(u"controlValuesFrame")
        self.controlValuesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlValuesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.controlValuesFrame)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gripperValueLabel = QLabel(self.controlValuesFrame)
        self.gripperValueLabel.setObjectName(u"gripperValueLabel")
        self.gripperValueLabel.setFont(font)

        self.verticalLayout_16.addWidget(self.gripperValueLabel)

        self.speedValueLabel = QLabel(self.controlValuesFrame)
        self.speedValueLabel.setObjectName(u"speedValueLabel")
        self.speedValueLabel.setFont(font)

        self.verticalLayout_16.addWidget(self.speedValueLabel)

        self.accelerationValueLabel = QLabel(self.controlValuesFrame)
        self.accelerationValueLabel.setObjectName(u"accelerationValueLabel")
        self.accelerationValueLabel.setFont(font)

        self.verticalLayout_16.addWidget(self.accelerationValueLabel)


        self.horizontalLayout.addWidget(self.controlValuesFrame)

        self.subtractButtonFrame = QFrame(self.controlFrame)
        self.subtractButtonFrame.setObjectName(u"subtractButtonFrame")
        self.subtractButtonFrame.setToolTipDuration(2000)
        self.subtractButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.subtractButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.subtractButtonFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 10)
        self.subtractButton = QPushButton(self.subtractButtonFrame)
        self.subtractButton.setObjectName(u"subtractButton")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/subtract.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.subtractButton.setIcon(icon5)
        self.subtractButton.setIconSize(QSize(30, 30))

        self.verticalLayout_11.addWidget(self.subtractButton)


        self.horizontalLayout.addWidget(self.subtractButtonFrame)


        self.verticalLayout.addWidget(self.controlFrame)


        self.verticalLayout_4.addWidget(self.middleFrame)

        self.animationFrame = QFrame(Scara)
        self.animationFrame.setObjectName(u"animationFrame")
        self.animationFrame.setStyleSheet(u"")
        self.animationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.animationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.animationFrame)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.feedbackLabel = QLabel(self.animationFrame)
        self.feedbackLabel.setObjectName(u"feedbackLabel")
        self.feedbackLabel.setFont(font)

        self.horizontalLayout_7.addWidget(self.feedbackLabel)

        self.animationLabel = QLabel(self.animationFrame)
        self.animationLabel.setObjectName(u"animationLabel")
        self.animationLabel.setMaximumSize(QSize(35, 30))

        self.horizontalLayout_7.addWidget(self.animationLabel)


        self.verticalLayout_4.addWidget(self.animationFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.bottomFrame = QFrame(Scara)
        self.bottomFrame.setObjectName(u"bottomFrame")
        sizePolicy2.setHeightForWidth(self.bottomFrame.sizePolicy().hasHeightForWidth())
        self.bottomFrame.setSizePolicy(sizePolicy2)
        self.bottomFrame.setStyleSheet(u"QFrame#bottomFrame{\n"
"background-color: rgba(55, 55, 55, 120);\n"
"}")
        self.bottomFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bottomFrame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 5, 0, 5)
        self.inverseLabel = QLabel(self.bottomFrame)
        self.inverseLabel.setObjectName(u"inverseLabel")
        self.inverseLabel.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.inverseLabel.sizePolicy().hasHeightForWidth())
        self.inverseLabel.setSizePolicy(sizePolicy4)
        self.inverseLabel.setFont(font4)
        self.inverseLabel.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 120, 20);")

        self.verticalLayout_3.addWidget(self.inverseLabel)

        self.positionsFrame = QFrame(self.bottomFrame)
        self.positionsFrame.setObjectName(u"positionsFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.positionsFrame.sizePolicy().hasHeightForWidth())
        self.positionsFrame.setSizePolicy(sizePolicy5)
        self.positionsFrame.setStyleSheet(u"QLabel {\n"
"border-radius: 0px;\n"
"}")
        self.positionsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.positionsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.positionsFrame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 10)
        self.xPositionFrame = QFrame(self.positionsFrame)
        self.xPositionFrame.setObjectName(u"xPositionFrame")
        self.xPositionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.xPositionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.xPositionFrame)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.xPositionLabel = QLabel(self.xPositionFrame)
        self.xPositionLabel.setObjectName(u"xPositionLabel")
        sizePolicy4.setHeightForWidth(self.xPositionLabel.sizePolicy().hasHeightForWidth())
        self.xPositionLabel.setSizePolicy(sizePolicy4)
        self.xPositionLabel.setFont(font)
        self.xPositionLabel.setStyleSheet(u"border-bottom: 2px solid rgb(255,140,20);")

        self.verticalLayout_9.addWidget(self.xPositionLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.xPositionLineEdit = QLineEdit(self.xPositionFrame)
        self.xPositionLineEdit.setObjectName(u"xPositionLineEdit")
        self.xPositionLineEdit.setMaximumSize(QSize(100, 16777215))
        self.xPositionLineEdit.setFont(font)
        self.xPositionLineEdit.setToolTipDuration(2000)
        self.xPositionLineEdit.setMaxLength(4)
        self.xPositionLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.xPositionLineEdit)


        self.horizontalLayout_2.addWidget(self.xPositionFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.yPositionFrame = QFrame(self.positionsFrame)
        self.yPositionFrame.setObjectName(u"yPositionFrame")
        self.yPositionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.yPositionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.yPositionFrame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.yPositionLabel = QLabel(self.yPositionFrame)
        self.yPositionLabel.setObjectName(u"yPositionLabel")
        sizePolicy4.setHeightForWidth(self.yPositionLabel.sizePolicy().hasHeightForWidth())
        self.yPositionLabel.setSizePolicy(sizePolicy4)
        self.yPositionLabel.setFont(font)
        self.yPositionLabel.setStyleSheet(u"border-bottom: 2px solid rgb(255,120,20);")

        self.verticalLayout_10.addWidget(self.yPositionLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.yPositionLineEdit = QLineEdit(self.yPositionFrame)
        self.yPositionLineEdit.setObjectName(u"yPositionLineEdit")
        self.yPositionLineEdit.setMaximumSize(QSize(100, 16777215))
        self.yPositionLineEdit.setFont(font)
        self.yPositionLineEdit.setToolTipDuration(2000)
        self.yPositionLineEdit.setMaxLength(4)
        self.yPositionLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.yPositionLineEdit)


        self.horizontalLayout_2.addWidget(self.yPositionFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.zPositionFrame = QFrame(self.positionsFrame)
        self.zPositionFrame.setObjectName(u"zPositionFrame")
        self.zPositionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.zPositionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.zPositionFrame)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.zPositionLabel = QLabel(self.zPositionFrame)
        self.zPositionLabel.setObjectName(u"zPositionLabel")
        sizePolicy4.setHeightForWidth(self.zPositionLabel.sizePolicy().hasHeightForWidth())
        self.zPositionLabel.setSizePolicy(sizePolicy4)
        self.zPositionLabel.setFont(font)
        self.zPositionLabel.setStyleSheet(u"border-bottom: 2px solid rgb(255,100,20);")

        self.verticalLayout_12.addWidget(self.zPositionLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.zPositionLineEdit = QLineEdit(self.zPositionFrame)
        self.zPositionLineEdit.setObjectName(u"zPositionLineEdit")
        self.zPositionLineEdit.setMaximumSize(QSize(100, 16777215))
        self.zPositionLineEdit.setFont(font)
        self.zPositionLineEdit.setToolTipDuration(2000)
        self.zPositionLineEdit.setMaxLength(3)
        self.zPositionLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.zPositionLineEdit)


        self.horizontalLayout_2.addWidget(self.zPositionFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.moveButton = QPushButton(self.positionsFrame)
        self.moveButton.setObjectName(u"moveButton")
        self.moveButton.setToolTipDuration(2000)
        self.moveButton.setIcon(icon2)
        self.moveButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.moveButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.homeButton = QPushButton(self.positionsFrame)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setToolTipDuration(2000)
        icon6 = QIcon()
        icon6.addFile(u":/Icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeButton.setIcon(icon6)
        self.homeButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.homeButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.loopButton = QPushButton(self.positionsFrame)
        self.loopButton.setObjectName(u"loopButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.loopButton.sizePolicy().hasHeightForWidth())
        self.loopButton.setSizePolicy(sizePolicy6)
        self.loopButton.setToolTipDuration(2000)
        icon7 = QIcon()
        icon7.addFile(u":/Icons/loop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.loopButton.setIcon(icon7)
        self.loopButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.loopButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.saveButton = QPushButton(self.positionsFrame)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setToolTipDuration(2000)
        icon8 = QIcon()
        icon8.addFile(u":/Icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon8)
        self.saveButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.saveButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.clearButton = QPushButton(self.positionsFrame)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setToolTipDuration(2000)
        self.clearButton.setIcon(icon3)
        self.clearButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.clearButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.positionsFrame)

        self.tableFrame = QFrame(self.bottomFrame)
        self.tableFrame.setObjectName(u"tableFrame")
        sizePolicy2.setHeightForWidth(self.tableFrame.sizePolicy().hasHeightForWidth())
        self.tableFrame.setSizePolicy(sizePolicy2)
        self.tableFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.tableFrame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 20, 0)
        self.positionsTable = QTableWidget(self.tableFrame)
        if (self.positionsTable.columnCount() < 7):
            self.positionsTable.setColumnCount(7)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.positionsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        font6.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        self.positionsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6);
        self.positionsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.positionsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.positionsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.positionsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.positionsTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.positionsTable.setObjectName(u"positionsTable")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(12)
        font7.setBold(False)
        self.positionsTable.setFont(font7)
        self.positionsTable.setToolTipDuration(2000)
        self.positionsTable.setStyleSheet(u"QTableWidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(80, 80, 80, 50), stop:1 rgba(255, 255, 255, 50));\n"
"    alternate-background-color: rgba(60, 60, 60, 50); \n"
"	border: 1px solid rgb(30, 30, 30);\n"
"	border-radius: 0 px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(30, 30, 30, 200);\n"
"    color: rgb(255, 120, 20);\n"
"    padding: 2 px;\n"
"    border: 1px solid rgb(30, 30, 30);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"   background-color: rgba(255, 120, 20,100);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	color: white;\n"
"}\n"
"")
        self.positionsTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed)
        self.positionsTable.setAlternatingRowColors(True)
        self.positionsTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.positionsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.positionsTable.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.positionsTable.setCornerButtonEnabled(True)
        self.positionsTable.horizontalHeader().setVisible(True)
        self.positionsTable.horizontalHeader().setDefaultSectionSize(67)
        self.positionsTable.horizontalHeader().setStretchLastSection(True)
        self.positionsTable.verticalHeader().setVisible(False)

        self.horizontalLayout_3.addWidget(self.positionsTable)


        self.verticalLayout_3.addWidget(self.tableFrame)


        self.verticalLayout_4.addWidget(self.bottomFrame)


        self.retranslateUi(Scara)

        QMetaObject.connectSlotsByName(Scara)
    # setupUi

    def retranslateUi(self, Scara):
        Scara.setWindowTitle(QCoreApplication.translate("Scara", u"Scara Robot Arm", None))
        self.comLabel.setText(QCoreApplication.translate("Scara", u"COM:", None))
        self.portLineEdit.setInputMask("")
        self.portLineEdit.setText("")
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("Scara", u"Ex: 9", None))
#if QT_CONFIG(tooltip)
        self.comButton.setToolTip(QCoreApplication.translate("Scara", u"Toggle Connection", None))
#endif // QT_CONFIG(tooltip)
        self.comButton.setText("")
        self.logoLabel.setText("")
        self.rndLabel.setText("")
        self.forwardLabel.setText(QCoreApplication.translate("Scara", u"Forward Kinematics", None))
        self.firstJointRadio.setText(QCoreApplication.translate("Scara", u"First Joint", None))
        self.secondJointRadio.setText(QCoreApplication.translate("Scara", u"Second Joint", None))
        self.thirdJointRadio.setText(QCoreApplication.translate("Scara", u"Third Joint", None))
        self.zPositionRadio.setText(QCoreApplication.translate("Scara", u"Z Position", None))
        self.firstJointMoveButton.setText("")
        self.firstJointCancelButton.setText("")
        self.secondJointMoveButton.setText("")
        self.secondJointCancelButton.setText("")
        self.thirdJointMoveButton.setText("")
        self.thirdJointCancelButton.setText("")
        self.zPositionMoveButton.setText("")
        self.zPositionCancelButton.setText("")
        self.actualFirstJointValueLabel.setText(QCoreApplication.translate("Scara", u"0", None))
        self.actualSecondJointValueLabel.setText(QCoreApplication.translate("Scara", u"0", None))
        self.actualThirdJointValueLabel.setText(QCoreApplication.translate("Scara", u"0", None))
        self.actualZPositionValueLabel.setText(QCoreApplication.translate("Scara", u"100", None))
        self.firstJointValueLabel.setText(QCoreApplication.translate("Scara", u"0", None))
        self.secondJointValueLabel.setText(QCoreApplication.translate("Scara", u"0", None))
        self.thirdJointValueLabel.setText(QCoreApplication.translate("Scara", u"0", None))
        self.zPositionValueLabel.setText(QCoreApplication.translate("Scara", u"100", None))
#if QT_CONFIG(tooltip)
        self.addButton.setToolTip(QCoreApplication.translate("Scara", u"Increment", None))
#endif // QT_CONFIG(tooltip)
        self.addButton.setText("")
        self.gripperRadio.setText(QCoreApplication.translate("Scara", u"Gripper", None))
        self.speedRadio.setText(QCoreApplication.translate("Scara", u"Speed", None))
        self.accelerationRadio.setText(QCoreApplication.translate("Scara", u"Acceleration", None))
        self.gripperValueLabel.setText(QCoreApplication.translate("Scara", u"0", None))
        self.speedValueLabel.setText(QCoreApplication.translate("Scara", u"500", None))
        self.accelerationValueLabel.setText(QCoreApplication.translate("Scara", u"500", None))
#if QT_CONFIG(tooltip)
        self.subtractButtonFrame.setToolTip(QCoreApplication.translate("Scara", u"Decrement", None))
#endif // QT_CONFIG(tooltip)
        self.subtractButton.setText("")
        self.feedbackLabel.setText(QCoreApplication.translate("Scara", u"Moving to desired position ...", None))
        self.animationLabel.setText("")
        self.inverseLabel.setText(QCoreApplication.translate("Scara", u"Inverse Kinematics", None))
        self.xPositionLabel.setText(QCoreApplication.translate("Scara", u"X Position:", None))
#if QT_CONFIG(tooltip)
        self.xPositionLineEdit.setToolTip(QCoreApplication.translate("Scara", u"Enter value from -365 to 365", None))
#endif // QT_CONFIG(tooltip)
        self.xPositionLineEdit.setText(QCoreApplication.translate("Scara", u"365", None))
        self.xPositionLineEdit.setPlaceholderText(QCoreApplication.translate("Scara", u"X", None))
        self.yPositionLabel.setText(QCoreApplication.translate("Scara", u"Y Position:", None))
#if QT_CONFIG(tooltip)
        self.yPositionLineEdit.setToolTip(QCoreApplication.translate("Scara", u"Enter value from -365 to 365", None))
#endif // QT_CONFIG(tooltip)
        self.yPositionLineEdit.setText(QCoreApplication.translate("Scara", u"0", None))
        self.yPositionLineEdit.setPlaceholderText(QCoreApplication.translate("Scara", u"Y", None))
        self.zPositionLabel.setText(QCoreApplication.translate("Scara", u"Z Position:", None))
#if QT_CONFIG(tooltip)
        self.zPositionLineEdit.setToolTip(QCoreApplication.translate("Scara", u"Enter value from 0 to 150", None))
#endif // QT_CONFIG(tooltip)
        self.zPositionLineEdit.setText(QCoreApplication.translate("Scara", u"100", None))
        self.zPositionLineEdit.setPlaceholderText(QCoreApplication.translate("Scara", u"Z", None))
#if QT_CONFIG(tooltip)
        self.moveButton.setToolTip(QCoreApplication.translate("Scara", u"Move to position", None))
#endif // QT_CONFIG(tooltip)
        self.moveButton.setText("")
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("Scara", u"Move to home position", None))
#endif // QT_CONFIG(tooltip)
        self.homeButton.setText("")
#if QT_CONFIG(tooltip)
        self.loopButton.setToolTip(QCoreApplication.translate("Scara", u"Loop on selected positions", None))
#endif // QT_CONFIG(tooltip)
        self.loopButton.setText("")
#if QT_CONFIG(tooltip)
        self.saveButton.setToolTip(QCoreApplication.translate("Scara", u"Save position", None))
#endif // QT_CONFIG(tooltip)
        self.saveButton.setText("")
#if QT_CONFIG(tooltip)
        self.clearButton.setToolTip(QCoreApplication.translate("Scara", u"Clear all positions", None))
#endif // QT_CONFIG(tooltip)
        self.clearButton.setText("")
        ___qtablewidgetitem = self.positionsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Scara", u"Order", None));
        ___qtablewidgetitem1 = self.positionsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Scara", u"X", None));
        ___qtablewidgetitem2 = self.positionsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Scara", u"Y", None));
        ___qtablewidgetitem3 = self.positionsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Scara", u"Z", None));
        ___qtablewidgetitem4 = self.positionsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Scara", u"Gripper", None));
        ___qtablewidgetitem5 = self.positionsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Scara", u"Speed", None));
        ___qtablewidgetitem6 = self.positionsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Scara", u"Accel.", None));
#if QT_CONFIG(tooltip)
        self.positionsTable.setToolTip(QCoreApplication.translate("Scara", u"Double click to remove saved position or type to edit text in a cell", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

