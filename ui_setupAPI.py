# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/setupAPI.ui'
#
# Created: Mon Mar 27 13:50:47 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_setupAPI(object):
    def setupUi(self, setupAPI):
        setupAPI.setObjectName("setupAPI")
        setupAPI.resize(374, 188)
        self.verticalLayout = QtGui.QVBoxLayout(setupAPI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.apiFileLocationDisplay = QtGui.QLineEdit(setupAPI)
        self.apiFileLocationDisplay.setDragEnabled(True)
        self.apiFileLocationDisplay.setReadOnly(True)
        self.apiFileLocationDisplay.setObjectName("apiFileLocationDisplay")
        self.verticalLayout.addWidget(self.apiFileLocationDisplay)
        self.groupBox = QtGui.QGroupBox(setupAPI)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.portSpin = QtGui.QSpinBox(self.groupBox)
        self.portSpin.setMinimum(1000)
        self.portSpin.setMaximum(10000)
        self.portSpin.setProperty("value", 1234)
        self.portSpin.setObjectName("portSpin")
        self.verticalLayout_2.addWidget(self.portSpin)
        self.verticalLayout.addWidget(self.groupBox)
        self.selectAPIFileButton = QtGui.QPushButton(setupAPI)
        self.selectAPIFileButton.setObjectName("selectAPIFileButton")
        self.verticalLayout.addWidget(self.selectAPIFileButton)
        self.addAPIEntryButton = QtGui.QPushButton(setupAPI)
        self.addAPIEntryButton.setObjectName("addAPIEntryButton")
        self.verticalLayout.addWidget(self.addAPIEntryButton)

        self.retranslateUi(setupAPI)
        QtCore.QMetaObject.connectSlotsByName(setupAPI)

    def retranslateUi(self, setupAPI):
        setupAPI.setWindowTitle(QtGui.QApplication.translate("setupAPI", "Setup api.ini", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("setupAPI", "Listener Port Number", None, QtGui.QApplication.UnicodeUTF8))
        self.selectAPIFileButton.setText(QtGui.QApplication.translate("setupAPI", "Select Hex Install Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.addAPIEntryButton.setText(QtGui.QApplication.translate("setupAPI", "Add Listener to Hex\'s api.ini", None, QtGui.QApplication.UnicodeUTF8))

