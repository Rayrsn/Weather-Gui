import sys
from PySide2.QtCore import *
from PySide2.QtGui import * 
from PySide2.QtWidgets import *

from ui_weather_gui import Ui_MainWindow

def start_UI():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

start_UI()
