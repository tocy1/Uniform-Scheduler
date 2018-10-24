# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:54:28 2018

@author: Uzoma
"""

from PyQt5 import QtGui, QtCore,QtWidgets
#from PySid import QtGui, QtCore
import sys

class Example(QtWidgets.QWidget):

      def __init__(self):
          super(Example, self).__init__()
          self.initUI()

      def initUI(self):

          self.qbtn = QtWidgets.QPushButton('Press', self)
          self.qbtn.clicked.connect(self.button_disable)
          self.qbtn.resize(self.qbtn.sizeHint())
          self.setGeometry(300, 300, 250, 150)
          self.setWindowTitle('Button Disable')
          self.show()

      def button_disable(self):
          self.qbtn.setEnabled(False)
          QtWidgets.QApplication.processEvents()

          for i in range(1, 100000000):
             pass
          print("finished")
          self.qbtn.setEnabled(True)

if __name__ == '__main__':
     app = QtWidgets.QApplication(sys.argv)
     ex = Example()
     sys.exit(app.exec_())
