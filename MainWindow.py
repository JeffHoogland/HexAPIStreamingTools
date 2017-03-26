import sys
import time
import json
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from PySide.QtGui import *
from PySide.QtCore import *
from ui_MainWindow import Ui_MainWindow
from HexHandler import HexHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()
        
        self.ourServer = ServerThread()
    
    def assignWidgets(self):
        self.serverToggleButton.clicked.connect(self.serverTogglePushed)
    
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
            self.ourServer.start()
            self.serverToggleButton.setEnabled(False)
            while not self.ourServer.isRunning():
                time.sleep(0.01)
                continue
            self.serverToggleButton.setText('Stop API Listener')
            #Stopping the server doesn't currently work nicely. Fix that at some point
            #self.serverToggleButton.setEnabled(True)

class ServerThread(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.listener = HTTPServer(('', 1234), HexHandler)
    
    def run(self):
        self.listener.serve_forever()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
