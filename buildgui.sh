#!/bin/bash
rm -f ui_*.py
rm -f ui_*.pyc
pyside-uic GUI/MainWindow.ui > ui_MainWindow.py
pyside-uic GUI/setupAPI.ui > ui_setupAPI.py
