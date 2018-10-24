# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:52:54 2018

@author: Uzoma
"""
import sys
from  PyQt5 import QtGui
class Window (QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Uniform Scheduler")
        self.setWindowicon(QtGui.Qticon("Z.jpg"))
        self.show
        
app=QtGui.QtApplication(sys.argv)
GUI=Window()
sys.exit(sys.argv)
