from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PyQt5.QtCore import Qt, QUrl

from file import *

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        Form = QtWidgets.QMainWindow()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 450)
        MainWindow.setWindowIcon(QtGui.QIcon("pid.png"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 450))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QScrollArea {\n"
                                 "background: rgba(255, 255, 255, 0)\n"
                                 "}\n"
                                 "\n"
                                 "QScrollArea QWidget {\n"
                                 "background: rgba(255, 255, 255, 0)\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox, QScrollArea {\n"
                                 "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
                                 "stop:0 rgba(255, 255, 255, 100),\n"
                                 "stop:1 rgba(255, 255, 255, 30) );\n"
                                 "border-radius: 10px;\n"
                                 "border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
                                 "stop:0 rgba(255, 255, 255, 255),\n"
                                 "stop:1 rgba(255, 255, 255, 30) );\n"
                                 "}\n"
                                 "\n"
                                 "QScrollArea QWidget QGroupBox {\n"
                                 "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
                                 "stop:0 rgba(255, 180, 181, 50),\n"
                                 "stop:1 rgba(255, 94, 97, 5) );\n"
                                 "border-radius: 10px;\n"
                                 "border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
                                 "stop:0 rgba(255, 180, 181, 150),\n"
                                 "stop:1 rgba(255, 94, 97, 10) );\n"
                                 "}\n"
                                 "\n"
                                 "QScrollArea QWidget QProgressBar {\n"
                                 "background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
                                 "stop: 0 #fff,\n"
                                 "stop: 0.7 #ddd,\n"
                                 "stop: 1 #eee );\n"
                                 "}\n"
                                 "\n"
                                 "QScrollArea QWidget QLabel {\n"
                                 "font-family: Helvetica;\n"
                                 "font-size: 16px;\n"
                                 "font-weight: italic;\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "}\n"
                                 "\n"
                                 "QScrollArea QWidget QPushButton {\n"
                                 "    color: black;\n"
                                 "    background: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0, y2:0,\n"
                                 "stop:0 rgba(255, 62, 65, 200),\n"
                                 "stop:1 rgba(255, 255, 255, 100) );\n"
                                 "    border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
                                 "stop:0 rgba(255, 180, 181, 255),\n"
                                 "stop:1 rgba(255, 94, 97, 30) );\n"
                                 "    padding-top: 5px;\n"
                                 "    padding-bottom: 5px;\n"
                                 "    padding-left: 5px;\n"
                                 "    padding-right: 5px;\n"
                                 "    border-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollArea QWidget QPushButton:hover {\n"
                                 "background: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0, y2:0,\n"
                                 "stop:0 rgba(255, 62, 65, 150),\n"
                                 "stop:1 rgba(255, 255, 255, 50) );\n"
                                 "}\n"
                                 "\n"
                                 "QScrollArea QWidget QPushButton:pressed {\n"
                                 "    border-width: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox {\n"
                                 "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
                                 "stop:0 rgba(255, 255, 255, 190),\n"
                                 "stop:1 rgba(255, 255, 255, 80) );\n"
                                 "border-radius: 10px;\n"
                                 "border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
                                 "stop:0 rgba(255, 255, 255, 255),\n"
                                 "stop:1 rgba(255, 255, 255, 30) );\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow {\n"
                                 "background: QLinearGradient(spread:pad, x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "stop: 1 #e31313,\n"
                                 "stop: 0.62 #fff,\n"
                                 "stop: 0.23 #fff,\n"
                                 "stop: 0 #e31313 );\n"
                                 "width: 30px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollArea QScrollBar {\n"
                                 "background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
                                 "stop: 1 #ff2023,\n"
                                 "stop: 0.5 #ffffff,\n"
                                 "stop: 0 #ff393c );\n"
                                 "width: 25px;\n"
                                 "border-radius: 15px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:vertical {\n"
                                 "    border: none;\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "    width: 14px;\n"
                                 "    margin: 15px 0 15px 0;\n"
                                 "    border-radius: 0px;\n"
                                 " }\n"
                                 "\n"
                                 "/*  HANDLE BAR VERTICAL */\n"
                                 "QScrollBar::handle:vertical {    \n"
                                 "    background-color: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
                                 "stop: 1 #ff2023,\n"
                                 "stop: 0.5 #ffffff,\n"
                                 "stop: 0 #ff393c );\n"
                                 "    min-height: 30px;\n"
                                 "}\n"
                                 "\n"
                                 "/* BTN TOP - SCROLLBAR */\n"
                                 "QScrollBar::sub-line:vertical {\n"
                                 "    border: none;\n"
                                 "    background-color: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
                                 "stop: 1 #ff2023,\n"
                                 "stop: 0.5 #ffffff,\n"
                                 "stop: 0 #ff393c );\n"
                                 "    height: 15px;\n"
                                 "    border-top-left-radius: 7px;\n"
                                 "    border-top-right-radius: 7px;\n"
                                 "    subcontrol-position: top;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "/* BTN BOTTOM - SCROLLBAR */\n"
                                 "QScrollBar::add-line:vertical {\n"
                                 "    border: none;\n"
                                 "    background-color: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
                                 "stop: 1 #ff2023,\n"
                                 "stop: 0.5 #ffffff,\n"
                                 "stop: 0 #ff393c );;\n"
                                 "    height: 15px;\n"
                                 "    border-bottom-left-radius: 7px;\n"
                                 "    border-bottom-right-radius: 7px;\n"
                                 "    subcontrol-position: bottom;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar {\n"
                                 "border: 1px solid black;\n"
                                 "text-align: center;\n"
                                 "padding: 1px;\n"
                                 "border-radius: 5px;\n"
                                 "border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
                                 "stop:0 rgba(255, 180, 181, 200),\n"
                                 "stop:1 rgba(255, 94, 97, 120) );\n"
                                 "background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
                                 "stop: 0 #fff,\n"
                                 "stop: 0.7 #ddd,\n"
                                 "stop: 1 #eee );\n"
                                 "width: 15px;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar::chunk {\n"
                                 "background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
                                 "stop: 0 #ff051e,\n"
                                 "stop: 0.7 #ffffff,\n"
                                 "stop: 1 #ff585b );\n"
                                 "border-radius: 2px;\n"
                                 "border: 1px solid black;\n"
                                 "}\n"
                                 "\n"
                                 "#progressBar_all {\n"
                                 "border-width: 5px;\n"
                                 "}")
        formLayout = QtWidgets.QFormLayout()

        links = []

        labelList = []
        barList = []
        buttonList = []

        class ListBoxWidget(QtWidgets.QScrollArea):
            def __init__(self, parent=None):
                super().__init__(parent)
                self.setAcceptDrops(True)
                self.linksBefore = 0

            def dragEnterEvent(self, event):
                if event.mimeData().hasUrls:
                    event.accept()
                else:
                    event.ignore()

            def dragMoveEvent(self, event):
                if event.mimeData().hasUrls():
                    event.setDropAction(Qt.CopyAction)
                    event.accept()
                else:
                    event.ignore()

            def dropEvent(self, event):
                if event.mimeData().hasUrls():
                    event.setDropAction(Qt.CopyAction)
                    event.accept()

                    self.linksBefore = len(links)

                    for url in event.mimeData().urls():
                        if url.isLocalFile():
                            links.append(str(url.toLocalFile()))
                        else:
                            links.append(str(url.toString()))

                    for i in range(self.linksBefore, len(links)):
                        groupBox = QtWidgets.QGroupBox()
                        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                                           QtWidgets.QSizePolicy.Fixed)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(groupBox.sizePolicy().hasHeightForWidth())
                        groupBox.setSizePolicy(sizePolicy)
                        groupBox.setMinimumSize(QtCore.QSize(0, 50))
                        groupBox.setMaximumSize(QtCore.QSize(16777215, 50))
                        groupBox.setSizeIncrement(QtCore.QSize(0, 0))
                        groupBox.setBaseSize(QtCore.QSize(0, 30))
                        groupBox.setTitle("")
                        groupBox.setObjectName("groupBox" + str(i))
                        horizontalLayout_3 = QtWidgets.QHBoxLayout(groupBox)
                        horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
                        label = QtWidgets.QLabel(groupBox)
                        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Fixed)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
                        label.setSizePolicy(sizePolicy)
                        label.setMinimumSize(QtCore.QSize(50, 30))
                        label.setMaximumSize(QtCore.QSize(999999, 30))
                        font = QtGui.QFont()
                        font.setFamily("Helvetica")
                        font.setPointSize(-1)
                        font.setUnderline(False)
                        label.setFont(font)
                        label.setAlignment(
                            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                        label.setObjectName("label" + str(i))
                        progressBar = QtWidgets.QProgressBar(groupBox)
                        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Fixed)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(progressBar.sizePolicy().hasHeightForWidth())
                        progressBar.setSizePolicy(sizePolicy)
                        progressBar.setMinimumSize(QtCore.QSize(150, 0))
                        progressBar.setMaximumSize(QtCore.QSize(150, 40))
                        progressBar.setProperty("value", 24)
                        progressBar.setObjectName("progressBar" + str(i))
                        pushButton = QtWidgets.QPushButton(groupBox)
                        pushButton.setEnabled(True)

                        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Fixed)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
                        pushButton.setSizePolicy(sizePolicy)
                        pushButton.setMinimumSize(QtCore.QSize(70, 20))
                        pushButton.setMaximumSize(QtCore.QSize(70, 40))
                        pushButton.setStyleSheet("")
                        pushButton.setObjectName("pushButton" + str(i))

                        pushButton.setText("Открыть")

                        label.setText(os.path.basename(links[i]))
                        labelList.append(label)
                        barList.append(progressBar)
                        buttonList.append(pushButton)

                        horizontalLayout_3.addWidget(labelList[i])
                        horizontalLayout_3.addWidget(barList[i])
                        horizontalLayout_3.addWidget(buttonList[i])

                        formLayout.addRow(groupBox)

                else:
                    event.ignore()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar_all = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_all.sizePolicy().hasHeightForWidth())
        self.progressBar_all.setSizePolicy(sizePolicy)
        self.progressBar_all.setStyleSheet("")
        self.progressBar_all.setProperty("value", 24)
        self.progressBar_all.setObjectName("progressBar_all")
        self.gridLayout.addWidget(self.progressBar_all, 2, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 5, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pid_left = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pid_left.sizePolicy().hasHeightForWidth())
        self.pid_left.setSizePolicy(sizePolicy)
        self.pid_left.setText("")
        self.pid_left.setPixmap(QtGui.QPixmap("pid.png"))
        self.pid_left.setScaledContents(False)
        self.pid_left.setObjectName("pid_left")
        self.verticalLayout.addWidget(self.pid_left)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.pid_right = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pid_right.sizePolicy().hasHeightForWidth())
        self.pid_right.setSizePolicy(sizePolicy)
        self.pid_right.setText("")
        self.pid_right.setPixmap(QtGui.QPixmap("pid.png"))
        self.pid_right.setScaledContents(False)
        self.pid_right.setObjectName("pid_right")
        self.verticalLayout_4.addWidget(self.pid_right)
        spacerItem3 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 6, 1, 2)

        self.scrollArea = ListBoxWidget(self.centralwidget) ###

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(482, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 476, 331))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.scrollAreaWidgetContents.setLayout(formLayout) ###

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализатор"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    MainWindow.show()
    sys.exit(app.exec_())
