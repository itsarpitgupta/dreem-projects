# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui',
# licensing of 'ui_mainwindow.ui' applies.
#
# Created: Sun Aug 18 09:16:02 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

from gui.MplWidget import MplWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(958, 607)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setObjectName("MplWidget")
        self.gridLayout_11.addWidget(self.MplWidget, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setMinimumSize(QtCore.QSize(50, 10))
        self.splitter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.splitter.setLineWidth(20)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setMinimumSize(QtCore.QSize(0, 276))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.getconnected = QtWidgets.QWidget()
        self.getconnected.setObjectName("getconnected")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.getconnected)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.getconnected)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_5.addWidget(self.pushButton_11, 2, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_5.addWidget(self.pushButton_12, 3, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_5.addWidget(self.pushButton_13, 4, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_5.addWidget(self.pushButton_9, 0, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_5.addWidget(self.pushButton_10, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 5, 1, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_2.setObjectName("listWidget_2")
        QtWidgets.QListWidgetItem(self.listWidget_2)
        self.gridLayout_5.addWidget(self.listWidget_2, 0, 0, 6, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.getconnected)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_7.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_7.addWidget(self.pushButton_15)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.gridLayout_6.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.getconnected)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.gridLayout.addLayout(self.verticalLayout_9, 0, 0, 4, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_11, 0, 2, 3, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_10.addWidget(self.lineEdit_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_10.addWidget(self.lineEdit_4)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_10.addWidget(self.lineEdit_6)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 3, 3, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 3, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 94, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.getconnected)
        self.setupimage = QtWidgets.QWidget()
        self.setupimage.setObjectName("setupimage")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.setupimage)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_4 = QtWidgets.QGroupBox(self.setupimage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_7.addWidget(self.pushButton_16, 0, 0, 1, 2)
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_7.addWidget(self.pushButton_17, 1, 0, 1, 2)
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_7.addWidget(self.pushButton_18, 2, 0, 2, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 4, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.setupimage)
        self.groupBox_5.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_6 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_9.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_9.setHorizontalSpacing(5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_18 = QtWidgets.QLabel(self.frame_6)
        self.label_18.setObjectName("label_18")
        self.gridLayout_9.addWidget(self.label_18, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setObjectName("label_12")
        self.gridLayout_9.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        self.label_15.setObjectName("label_15")
        self.gridLayout_9.addWidget(self.label_15, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_9.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setObjectName("label_14")
        self.gridLayout_9.addWidget(self.label_14, 2, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_9.addWidget(self.spinBox_2, 2, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_9.addWidget(self.spinBox, 1, 1, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_9.addWidget(self.spinBox_3, 3, 1, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_9.addWidget(self.spinBox_5, 5, 1, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_9.addWidget(self.spinBox_4, 4, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_6)
        self.label_19.setObjectName("label_19")
        self.gridLayout_9.addWidget(self.label_19, 7, 0, 1, 1)
        self.spinBox_7 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_7.setObjectName("spinBox_7")
        self.gridLayout_9.addWidget(self.spinBox_7, 7, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_9.addWidget(self.comboBox_2, 6, 1, 1, 1)
        self.gridLayout_8.addWidget(self.frame_6, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_5, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.setupimage)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.groupBox_6 = QtWidgets.QGroupBox(self.page)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_6)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout_12.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.page)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_7)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_13.addWidget(self.plainTextEdit, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout.addWidget(self.pushButton_20)
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout.addWidget(self.pushButton_19)
        self.gridLayout_13.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem5, 1, 1, 1, 1)
        self.gridLayout_14.addWidget(self.groupBox_7, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem6, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setMaximumSize(QtCore.QSize(524287, 300))
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 111, 304))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setFloating(False)
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.dockWidgetContents_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 1, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Select a Camera", None, -1))
        self.pushButton_11.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh", None, -1))
        self.pushButton_12.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))
        self.pushButton_13.setText(QtWidgets.QApplication.translate("MainWindow", "Camera", None, -1))
        self.pushButton_9.setText(QtWidgets.QApplication.translate("MainWindow", "Connect", None, -1))
        self.pushButton_10.setText(QtWidgets.QApplication.translate("MainWindow", "Disconnect", None, -1))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.item(0).setText(
            QtWidgets.QApplication.translate("MainWindow", "arpit-java pc emulator", None, -1))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Create Job", None, -1))
        self.pushButton_14.setText(QtWidgets.QApplication.translate("MainWindow", "New Job", None, -1))
        self.pushButton_15.setText(QtWidgets.QApplication.translate("MainWindow", "Open Job", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Connected to:", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Model Number:", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Frimware Version:", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("MainWindow", "Current Job:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "MAC Address:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "IP Address:", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("MainWindow", "Serial Version:", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Load Image", None, -1))
        self.pushButton_16.setText(QtWidgets.QApplication.translate("MainWindow", "Trigger", None, -1))
        self.pushButton_17.setText(QtWidgets.QApplication.translate("MainWindow", "Load Image", None, -1))
        self.pushButton_18.setText(QtWidgets.QApplication.translate("MainWindow", "Live Video", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "Camera Settings", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("MainWindow", "Focus Controls", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "Trigger", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("MainWindow", "Gain", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("MainWindow", "Exposure (mesc)", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "Trigger Delay(msec)", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("MainWindow", "Number Of Rows", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("MainWindow", "Trigger Interval (mesc)", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("MainWindow", "Focus Position", None, -1))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "Tools", None, -1))
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Locate", None, -1))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Patterns",
                                                                                             None, -1))
        self.treeWidget.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Edge", None,
                                                                                             -1))
        self.treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "OCR", None, -1))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Dot Matrix",
                                                                                             None, -1))
        self.treeWidget.topLevelItem(1).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow",
                                                                                             "Barcode scanner", None,
                                                                                             -1))
        self.groupBox_7.setTitle(QtWidgets.QApplication.translate("MainWindow", "Directions", None, -1))
        self.plainTextEdit.setPlainText(QtWidgets.QApplication.translate("MainWindow",
                                                                         "afakdsfjaksdlfj kldasjf kljads kldajf kaldsfj kladsjf klasdfj kasdjf klsadjf klasjdf klasdjfkl asdjf klasdjf asdfjaksdfj kladsfj klasdfj kasdfj kasjdfk adfjkl adsfj kasdjf kasdfj kasdf.",
                                                                         None, -1))
        self.pushButton_20.setText(QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))
        self.pushButton_19.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.dockWidget.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Application Steps", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "1. Start", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Get Connected", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Set Up Image", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "2. Set up Tools", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Locate Part", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "Inspect Part", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "3. Configure Result", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "Inputs/Outputs", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "Communication", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "4. Finish", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_8.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.dockWidget_2.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Palettle", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3),
                                    QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4),
                                    QtWidgets.QApplication.translate("MainWindow", "Results", None, -1))
