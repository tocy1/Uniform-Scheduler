
    
from PyQt5.QtWidgets import QMainWindow,QApplication,QProgressBar,QPushButton,Qcheckbox
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon 
import sys
class Example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowIcon(QIcon("cc.png"))
            self.initUI()
           
            
        def initUI(self):
            self.pbar=QProgressBar(self)
            self.pbar.setGeometry(30,40,200,25)
            self.btn=QPushButton('Start',self)
            self.btn.move(40,80)
            self.btn.clicked.connect(self.doAction)
            self.timer=QBasicTimer()
            self.step=0
            self.setGeometry(300,300,280,170)
            self.setWindowTitle('Home')
            self.statusBar().showMessage("Ready")
    
            self.resize(500,300)
            self.show()
        def timerEvent(self,e):
            if self.step>=100:
                self.timer.stop()
                self.btn.setText('Finished')
                return
            self.step=self.step+1
            self.pbar.setValue(self.step)
        def doAction(self):
                if self.timer.isActive():
                    self.timer.stop()
                    self.btn.setText('Start')
                else:
                    self.timer.start(100,self)
                    self.btn.setText('Stop')
if __name__=='__main__':
            app=QApplication(sys.argv)
            ex=Example()
            sys.exit(app.exec_())