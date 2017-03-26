# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/setupAPI.ui'
#
# Created: Sun Mar 26 09:04:33 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_setupAPI(object):
    def setupUi(self, setupAPI):
        setupAPI.setObjectName("setupAPI")
        setupAPI.resize(400, 137)
        self.verticalLayout = QtGui.QVBoxLayout(setupAPI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(setupAPI)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.apiFileLocationDisplay = QtGui.QLineEdit(self.frame)
        self.apiFileLocationDisplay.setDragEnabled(True)
        self.apiFileLocationDisplay.setReadOnly(True)
        self.apiFileLocationDisplay.setObjectName("apiFileLocationDisplay")
        self.verticalLayout_3.addWidget(self.apiFileLocationDisplay)
        self.selectAPIFileButton = QtGui.QPushButton(self.frame)
        self.selectAPIFileButton.setObjectName("selectAPIFileButton")
        self.verticalLayout_3.addWidget(self.selectAPIFileButton)
        self.addAPIEntryButton = QtGui.QPushButton(self.frame)
        self.addAPIEntryButton.setObjectName("addAPIEntryButton")
        self.verticalLayout_3.addWidget(self.addAPIEntryButton)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(setupAPI)
        QtCore.QMetaObject.connectSlotsByName(setupAPI)

    def retranslateUi(self, setupAPI):
        setupAPI.setWindowTitle(QtGui.QApplication.translate("setupAPI", "Setup api.ini", None, QtGui.QApplication.UnicodeUTF8))
        self.selectAPIFileButton.setText(QtGui.QApplication.translate("setupAPI", "Select API File", None, QtGui.QApplication.UnicodeUTF8))
        self.addAPIEntryButton.setText(QtGui.QApplication.translate("setupAPI", "Add Listener to Hex\'s api.ini", None, QtGui.QApplication.UnicodeUTF8))

