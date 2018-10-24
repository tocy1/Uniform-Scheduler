# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:34:51 2018

@author: Uzoma
"""

import sys
from PyQt5.QtCore    import Qt, QRectF
from PyQt5.QtGui     import QPainter
from PyQt5.QtWidgets import QCalendarWidget, QApplication

class CalendarWidget(QCalendarWidget):
    def paintCell(self, painter, rect, date):
        painter.setRenderHint(QPainter.Antialiasing, True)
        #if (date.day() == 1) or (date.day() == 15):
            #painter.save()
            
        if  self.clicked[QDate]:
            
            painter.drawRect(rect)
            painter.setPen(Qt.blue)
            painter.drawText(QRectF(rect), Qt.TextSingleLine|Qt.AlignCenter, str(date.day()))
            painter.restore()
        else:
            QCalendarWidget.paintCell(self, painter, rect, date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CalendarWidget()
    w.show()
    sys.exit(app.exec_())
