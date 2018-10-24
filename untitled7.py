# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:47:58 2018

@author: Seamfix
"""

from PyQt5.QtWidgets import (QWidget, QCalendarWidget, 
    QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate,QRectF
from PyQt5.QtGui     import QPainter
import sys
#from datetime import datetime
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        self.datelist=[]
    def initUI(self):      
        
        vbox = QVBoxLayout(self)

        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.clicked[QDate].connect(self.showDate)
        
        vbox.addWidget(self.cal)
        
        self.lbl = QLabel(self)
        date = self.cal.selectedDate()
        self.lbl.setText(date.toString())
        
        vbox.addWidget(self.lbl)
        
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
        
        
    def showDate(self,date):     
        
        self.lbl.setText(date.toString())
        self.datelist.append(date.toString())
        
        #elf.paintCell
        print(self.datelist)
    #def paintCell(self, painter, rect,date):
        painter.setRenderHint(QPainter.Antialiasing, True)
        #if (date.day() == 1) or (date.day() == 15):
    
            #date1 = datetime.strptime(dat, '%A %B %d %Y')
            #painter.save()
        painter.drawRect(rect)
        painter.setPen(Qt.blue)
        painter.drawText(QRectF(rect), Qt.TextSingleLine|Qt.AlignCenter, str(date.day()))
        #painter.restore()
        self.cal.paintCell (self, painter,rect,date)
        self.updateCells()
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())