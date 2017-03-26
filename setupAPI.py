
import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_setupAPI import Ui_setupAPI

UserHome = os.path.expanduser("~")

def findAPIFile():
    likelyAPIPath = UserHome
    
    HexDIR = None
    
    for root, dirs, files in os.walk(likelyAPIPath):
        if "api.ini" in files:
            filePath = os.path.join(root, "api.ini")
            if "HEX SHARDS OF FATE" not in filePath:
                pass
            else:
                return filePath
        
        if "HEX SHARDS OF FATE" in dirs:
            HexDIR = os.path.join(root, "HEX SHARDS OF FATE")
    
    filePath = os.path.join(HexDIR, "api.ini")
    
    open(filePath, "a").close()
    return filePath
    

class setupAPI(QDialog, Ui_setupAPI):
    def __init__(self, parent):
        super(setupAPI, self).__init__(parent)
        self.rent = parent
        self.setupUi(self)
        
        self.HexAPIFile = None
        
        self.assignWidgets()

    def assignWidgets( self ):
        self.selectAPIFileButton.clicked.connect(self.selectAPIFilePushed)
        self.addAPIEntryButton.clicked.connect(self.addAPIEntryPushed)
    
    def start(self):
        self.HexAPIFile = findAPIFile()
        self.apiFileLocationDisplay.setText(self.HexAPIFile)
    
    def selectAPIFilePushed(self):
        filename = QFileDialog.getOpenFileName(self, 'Select your Hex api.ini file:', UserHome, 'INI Files (*.ini)')
        if filename:
            self.apiFileLocationDisplay.setText(filename[0])
            self.HexAPIFile = filename[0]
    
    def addAPIEntryPushed(self):
        with open(self.HexAPIFile, 'a+') as APIFile:
            APIFile.write("http://127.0.0.1:1234|All\n")
