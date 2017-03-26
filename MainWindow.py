import sys
import json
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from PySide.QtGui import *
from PySide.QtCore import *
from ui_MainWindow import Ui_MainWindow
from HexHandler import HexHandler

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()
        
        self.listener = HTTPServer(('', PORT), HexHandler)
    
    def assignWidgets(self):
        self.startServerButton.clicked.connect(self.startPushed)
        self.stopServerButton.clicked.connect(self.stopPushed)
    
    def startPushed(self):
        self.listener.serve_forever()
    
    def stopPushed(self):
        self.listener.socket.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
