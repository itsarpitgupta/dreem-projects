# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui',
# licensing of 'ui_mainwindow.ui' applies.
#
# Created: Sat Aug 24 20:23:06 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

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
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setMinimumSize(QtCore.QSize(50, 10))
        self.splitter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.splitter.setLineWidth(20)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setMinimumSize(QtCore.QSize(0, 276))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 296))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 786, 292))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.getconnected_2 = QtWidgets.QWidget()
        self.getconnected_2.setObjectName("getconnected_2")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.getconnected_2)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.groupBox_8 = QtWidgets.QGroupBox(self.getconnected_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_17.addWidget(self.pushButton_21, 2, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_17.addWidget(self.pushButton_22, 3, 1, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_17.addWidget(self.pushButton_23, 4, 1, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_17.addWidget(self.pushButton_24, 0, 1, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_17.addWidget(self.pushButton_25, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem, 5, 1, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_8)
        self.listWidget_3.setObjectName("listWidget_3")
        QtWidgets.QListWidgetItem(self.listWidget_3)
        self.gridLayout_17.addWidget(self.listWidget_3, 0, 0, 6, 1)
        self.gridLayout_16.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.getconnected_2)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout_8.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_8.addWidget(self.pushButton_27)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.gridLayout_16.addWidget(self.groupBox_9, 0, 1, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.getconnected_2)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_20 = QtWidgets.QLabel(self.groupBox_10)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_12.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.groupBox_10)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_12.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.groupBox_10)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_12.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.groupBox_10)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_12.addWidget(self.label_23)
        self.gridLayout.addLayout(self.verticalLayout_12, 0, 0, 4, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 0, 1, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_24 = QtWidgets.QLabel(self.groupBox_10)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_13.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.groupBox_10)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_13.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.groupBox_10)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_13.addWidget(self.label_26)
        self.gridLayout.addLayout(self.verticalLayout_13, 0, 2, 3, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_14.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_14.addWidget(self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_14.addWidget(self.lineEdit_11)
        self.gridLayout.addLayout(self.verticalLayout_14, 0, 3, 3, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 1, 1, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_13.setEnabled(False)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 2, 1, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_14.setEnabled(False)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 3, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 94, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_10, 0, 2, 1, 1)
        self.stackedWidget_2.addWidget(self.getconnected_2)
        self.setupimage_2 = QtWidgets.QWidget()
        self.setupimage_2.setObjectName("setupimage_2")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.setupimage_2)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.groupBox_11 = QtWidgets.QGroupBox(self.setupimage_2)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_19.addWidget(self.pushButton_28, 0, 0, 1, 2)
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_19.addWidget(self.pushButton_29, 1, 0, 1, 2)
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_19.addWidget(self.pushButton_30, 2, 0, 2, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem3, 4, 0, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_11, 0, 0, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.setupimage_2)
        self.groupBox_12.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.frame_6 = QtWidgets.QFrame(self.groupBox_12)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_21.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_21.setHorizontalSpacing(5)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setObjectName("label_27")
        self.gridLayout_21.addWidget(self.label_27, 6, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.frame_6)
        self.label_28.setObjectName("label_28")
        self.gridLayout_21.addWidget(self.label_28, 0, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame_6)
        self.label_29.setObjectName("label_29")
        self.gridLayout_21.addWidget(self.label_29, 5, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame_6)
        self.label_30.setObjectName("label_30")
        self.gridLayout_21.addWidget(self.label_30, 3, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_21.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.frame_6)
        self.label_31.setObjectName("label_31")
        self.gridLayout_21.addWidget(self.label_31, 1, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame_6)
        self.label_32.setObjectName("label_32")
        self.gridLayout_21.addWidget(self.label_32, 4, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.frame_6)
        self.label_33.setObjectName("label_33")
        self.gridLayout_21.addWidget(self.label_33, 2, 0, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_21.addWidget(self.spinBox_6, 2, 1, 1, 1)
        self.spinBox_8 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_8.setObjectName("spinBox_8")
        self.gridLayout_21.addWidget(self.spinBox_8, 1, 1, 1, 1)
        self.spinBox_9 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_9.setObjectName("spinBox_9")
        self.gridLayout_21.addWidget(self.spinBox_9, 3, 1, 1, 1)
        self.spinBox_10 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_10.setObjectName("spinBox_10")
        self.gridLayout_21.addWidget(self.spinBox_10, 5, 1, 1, 1)
        self.spinBox_11 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_11.setObjectName("spinBox_11")
        self.gridLayout_21.addWidget(self.spinBox_11, 4, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.frame_6)
        self.label_34.setObjectName("label_34")
        self.gridLayout_21.addWidget(self.label_34, 7, 0, 1, 1)
        self.spinBox_12 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_12.setObjectName("spinBox_12")
        self.gridLayout_21.addWidget(self.spinBox_12, 7, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_21.addWidget(self.comboBox_4, 6, 1, 1, 1)
        self.gridLayout_20.addWidget(self.frame_6, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_12, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem4, 0, 2, 1, 1)
        self.stackedWidget_2.addWidget(self.setupimage_2)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.groupBox_13 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.groupBox_13)
        self.treeWidget_2.setDragEnabled(True)
        self.treeWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.treeWidget_2.setAnimated(True)
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout_23.addWidget(self.treeWidget_2, 0, 0, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_13, 0, 0, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_14)
        self.plainTextEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit_2.setLineWidth(0)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_24.addWidget(self.plainTextEdit_2, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_31 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_2.addWidget(self.pushButton_31)
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout_2.addWidget(self.pushButton_32)
        self.gridLayout_24.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem5, 1, 1, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_14, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem6, 0, 2, 1, 1)
        self.stackedWidget_2.addWidget(self.page_2)
        self.gridLayout_25.addWidget(self.stackedWidget_2, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.splitter, 1, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_11.addWidget(self.graphicsView, 0, 0, 1, 1)
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
        self.progressBar = QtWidgets.QProgressBar(self.dockWidgetContents_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 1, 0, 1, 1)
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
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_8.setTitle(QtWidgets.QApplication.translate("MainWindow", "Select a Camera", None, -1))
        self.pushButton_21.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh", None, -1))
        self.pushButton_22.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))
        self.pushButton_23.setText(QtWidgets.QApplication.translate("MainWindow", "Camera", None, -1))
        self.pushButton_24.setText(QtWidgets.QApplication.translate("MainWindow", "Connect", None, -1))
        self.pushButton_25.setText(QtWidgets.QApplication.translate("MainWindow", "Disconnect", None, -1))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "arpit-java pc emulator", None, -1))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.groupBox_9.setTitle(QtWidgets.QApplication.translate("MainWindow", "Create Job", None, -1))
        self.pushButton_26.setText(QtWidgets.QApplication.translate("MainWindow", "New Job", None, -1))
        self.pushButton_27.setText(QtWidgets.QApplication.translate("MainWindow", "Open Job", None, -1))
        self.groupBox_10.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("MainWindow", "Connected to:", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("MainWindow", "Model Number:", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("MainWindow", "Frimware Version:", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("MainWindow", "Current Job:", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("MainWindow", "MAC Address:", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("MainWindow", "IP Address:", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("MainWindow", "Serial Version:", None, -1))
        self.groupBox_11.setTitle(QtWidgets.QApplication.translate("MainWindow", "Load Image", None, -1))
        self.pushButton_28.setText(QtWidgets.QApplication.translate("MainWindow", "Trigger", None, -1))
        self.pushButton_29.setText(QtWidgets.QApplication.translate("MainWindow", "Load Image", None, -1))
        self.pushButton_30.setText(QtWidgets.QApplication.translate("MainWindow", "Live Video", None, -1))
        self.groupBox_12.setTitle(QtWidgets.QApplication.translate("MainWindow", "Camera Settings", None, -1))
        self.label_27.setText(QtWidgets.QApplication.translate("MainWindow", "Focus Controls", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("MainWindow", "Trigger", None, -1))
        self.label_29.setText(QtWidgets.QApplication.translate("MainWindow", "Gain", None, -1))
        self.label_30.setText(QtWidgets.QApplication.translate("MainWindow", "Exposure (mesc)", None, -1))
        self.label_31.setText(QtWidgets.QApplication.translate("MainWindow", "Trigger Delay(msec)", None, -1))
        self.label_32.setText(QtWidgets.QApplication.translate("MainWindow", "Number Of Rows", None, -1))
        self.label_33.setText(QtWidgets.QApplication.translate("MainWindow", "Trigger Interval (mesc)", None, -1))
        self.label_34.setText(QtWidgets.QApplication.translate("MainWindow", "Focus Position", None, -1))
        self.groupBox_13.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.treeWidget_2.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "Tools", None, -1))
        self.treeWidget_2.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Locate", None, -1))
        self.treeWidget_2.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Patterns", None, -1))
        self.treeWidget_2.topLevelItem(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Edge", None, -1))
        self.treeWidget_2.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "OCR", None, -1))
        self.treeWidget_2.topLevelItem(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Dot Matrix", None, -1))
        self.treeWidget_2.topLevelItem(1).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Barcode scanner", None, -1))
        self.groupBox_14.setTitle(QtWidgets.QApplication.translate("MainWindow", "Directions", None, -1))
        self.plainTextEdit_2.setPlainText(QtWidgets.QApplication.translate("MainWindow", "afakdsfjaksdlfj kldasjf kljads kldajf kaldsfj kladsjf klasdfj kasdjf klsadjf klasjdf klasdjfkl asdjf klasdjf asdfjaksdfj kladsfj klasdfj kasdfj kasjdfk adfjkl adsfj kasdjf kasdfj kasdf.", None, -1))
        self.pushButton_31.setText(QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))
        self.pushButton_32.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))
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
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtWidgets.QApplication.translate("MainWindow", "Results", None, -1))

