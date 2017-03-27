# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/MainWindow.ui'
#
# Created: Mon Mar 27 13:50:47 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(329, 204)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hexDeckBox = QtGui.QGroupBox(self.centralwidget)
        self.hexDeckBox.setObjectName("hexDeckBox")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.hexDeckBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.outputPathDisplay = QtGui.QLineEdit(self.hexDeckBox)
        self.outputPathDisplay.setFrame(True)
        self.outputPathDisplay.setReadOnly(True)
        self.outputPathDisplay.setObjectName("outputPathDisplay")
        self.verticalLayout_4.addWidget(self.outputPathDisplay)
        self.outputPathButton = QtGui.QPushButton(self.hexDeckBox)
        self.outputPathButton.setObjectName("outputPathButton")
        self.verticalLayout_4.addWidget(self.outputPathButton)
        self.showReservesBox = QtGui.QCheckBox(self.hexDeckBox)
        self.showReservesBox.setChecked(False)
        self.showReservesBox.setObjectName("showReservesBox")
        self.verticalLayout_4.addWidget(self.showReservesBox)
        self.verticalLayout_2.addWidget(self.hexDeckBox)
        self.serverToggleButton = QtGui.QPushButton(self.centralwidget)
        self.serverToggleButton.setObjectName("serverToggleButton")
        self.verticalLayout_2.addWidget(self.serverToggleButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 329, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuSetup = QtGui.QMenu(self.menuBar)
        self.menuSetup.setObjectName("menuSetup")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAdd_API_Entry = QtGui.QAction(MainWindow)
        self.actionAdd_API_Entry.setObjectName("actionAdd_API_Entry")
        self.actionDownload_StackIt = QtGui.QAction(MainWindow)
        self.actionDownload_StackIt.setObjectName("actionDownload_StackIt")
        self.menuSetup.addAction(self.actionAdd_API_Entry)
        self.menuBar.addAction(self.menuSetup.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Hex API Dashboard", None, QtGui.QApplication.UnicodeUTF8))
        self.hexDeckBox.setTitle(QtGui.QApplication.translate("MainWindow", "Hex Deck Image Output Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.outputPathButton.setText(QtGui.QApplication.translate("MainWindow", "Change Output Path", None, QtGui.QApplication.UnicodeUTF8))
        self.showReservesBox.setText(QtGui.QApplication.translate("MainWindow", "Show Reserves", None, QtGui.QApplication.UnicodeUTF8))
        self.serverToggleButton.setText(QtGui.QApplication.translate("MainWindow", "Start API Listener", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSetup.setTitle(QtGui.QApplication.translate("MainWindow", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_API_Entry.setText(QtGui.QApplication.translate("MainWindow", "Add API Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload_StackIt.setText(QtGui.QApplication.translate("MainWindow", "Download StackIt", None, QtGui.QApplication.UnicodeUTF8))

