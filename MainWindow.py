import sys
import time
import json
import platform
import os

from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from PySide.QtGui import *
from PySide.QtCore import *
from ui_MainWindow import Ui_MainWindow
from HexHandler import HexHandler
from HexAPI import HexAPI

#Child Windows
from setupAPI import setupAPI

UserHome = os.path.expanduser("~")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.HexAPI = HexAPI()
        self.ourServer = ServerThread()
        
        self.assignWidgets()
        
        self.setupAPIWindow = setupAPI(self)
        
        self.show()
    
    def assignWidgets(self):
        self.serverToggleButton.clicked.connect(self.serverTogglePushed)
        self.outputPathButton.clicked.connect(self.outputPathPushed)
        
        self.outputPathDisplay.setText(self.HexAPI.config.get("HexDeck", "outputpath"))
        self.showReservesBox.setChecked(self.HexAPI.config.getboolean("HexDeck", "showreserves"))
        self.showReservesBox.stateChanged.connect(self.reservesCheckBoxChecked)
        
        self.actionAdd_API_Entry.triggered.connect(self.showSetupAPI)
    
    def showSetupAPI(self):
        self.setupAPIWindow.start()
        self.setupAPIWindow.show()
    
    def reservesCheckBoxChecked(self):
        self.HexAPI.setConfigValue("HexDeck", "showreserves", self.showReservesBox.isChecked())
    
    def serverTogglePushed(self):
        if self.ourServer.isRunning():
            self.serverToggleButton.setEnabled(False)
            self.ourServer.terminate()
            while self.ourServer.isRunning():
                time.sleep(0.01)
                continue
            self.serverToggleButton.setText('Start API Listener')
            self.serverToggleButton.setEnabled(True)
        else:
            self.ourServer.setupServer(int(self.HexAPI.getConfigValue("General", "port")))
            self.ourServer.start()
            self.serverToggleButton.setEnabled(False)
            while not self.ourServer.isRunning():
                time.sleep(0.01)
                continue
            self.serverToggleButton.setText('Stop API Listener')
            #Stopping the server doesn't currently work nicely. Fix that at some point
            #self.serverToggleButton.setEnabled(True)
            
    def outputPathPushed(self):
        outputDir = QFileDialog.getExistingDirectory(self, 'Select a location to output your deck images to:', self.HexAPI.config.get("HexDeck", "outputpath"))
        if outputDir:
            self.HexAPI.setConfigValue("HexDeck", "outputpath", outputDir)
            self.outputPathDisplay.setText(outputDir)

class ServerThread(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
    
    def setupServer(self, portNumber):
        print("Starting listener on port number %s"%portNumber)
        self.listener = HTTPServer(('', portNumber), HexHandler)
    
    def run(self):
        self.listener.serve_forever()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
