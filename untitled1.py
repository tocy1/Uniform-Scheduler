# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:56:49 2018

@author: Seamfix
"""
import sys
from PyQt5.QtCore    import Qt, QRectF
from PyQt5.QtGui     import QPainter,QPalette,QColor
from PyQt5.QtWidgets import QCalendarWidget, QApplication
class dateCalendar(QCalendarWidget):
    def __init__(self, parent = None):
        super(dateCalendar, self).__init__(parent)
        self.color = QColor(self.palette().color(QPalette.Highlight))
        self.color.setAlpha(150)
        #self.selectionChanged.connect(self.updateCells)
        self.dateList = []

    def paintCell(self, painter, rect, date):
        #calling original paintCell to draw the actual calendar
        QCalendarWidget.paintCell(self, painter, rect, date)

        #highlight a particular date
        if date in self.dateList:
            painter.fillRect(rect, self.color)

    def selectDates(self, qdatesList):
        self.dateList = qdatesList
        print(self.dateList)
        #this redraws the calendar with your updated date list
        self.updateCells()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = dateCalendar()
    w.show()
    sys.exit(app.exec_())
