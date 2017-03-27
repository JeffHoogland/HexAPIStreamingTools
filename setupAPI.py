
import os
import platform

from PySide.QtGui import *
from PySide.QtCore import *

from ui_setupAPI import Ui_setupAPI

UserHome = os.path.expanduser("~")

def findAPIFile():
    if "windows" in platform.platform().lower():
        #This code hard locks on Windows cause that os is poop
        #return None
        likelyAPIPaths = ["C:\Program Files (x86)\HEX", "C:\Program Files\HEX",
            "C:\Program Files (x86)\steam\steamapps\common\HEX SHARDS OF FATE",
            "C:\Program Files\steam\steamapps\common\HEX SHARDS OF FATE"]
    else:
        likelyAPIPaths = [UserHome]
    
    HexDIR = None
    
    for p in likelyAPIPaths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                if "api.ini" in files:
                    filePath = os.path.join(root, "api.ini")
                    if "HEX" not in filePath:
                        pass
                    else:
                        return filePath
                
                if "HEX SHARDS OF FATE" in dirs:
                    HexDIR = os.path.join(root, "HEX SHARDS OF FATE")
                elif "HEX" in dirs:
                    HexDIR = os.path.join(root, "HEX")
    
    if HexDIR:
        #we found a hex directory, but no api.ini file so make a blank one
        filePath = os.path.join(HexDIR, "api.ini")
        
        open(filePath, "a").close()
        return filePath
    else:
        #no hex directory found
        return None
    

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
        if not self.HexAPIFile:
            self.selectAPIFilePushed()
        else:
            self.apiFileLocationDisplay.setText(self.HexAPIFile)
    
    def selectAPIFilePushed(self):
        HexDIR = QFileDialog.getExistingDirectory(self, 'Select the directory that contains your Hex install:', UserHome)
        if HexDIR:
            filePath = os.path.join(HexDIR, "api.ini")
            
            #if the api file doesn't exist, create it
            if not os.path.exists(filePath):
                open(filePath, "a").close()
            
            self.apiFileLocationDisplay.setText(filePath)
            self.HexAPIFile = filePath
    
    def addAPIEntryPushed(self):
        if self.HexAPIFile:
            with open(self.HexAPIFile, 'a+') as APIFile:
                APIFile.write("\n")
                APIFile.write("http://127.0.0.1:1235|All\n")
        else:
            self.selectAPIFilePushed()
